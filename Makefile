VENV           := .venv
PYTHON         := $(VENV)/bin/python
ANSIBLE_GALAXY := $(VENV)/bin/ansible-galaxy
AVD_DIR        := collections/ansible_collections/arista/avd
CLAB           ?= containerlab
CLAB_TOPO      ?= sp.clab.yml
INVENTORY      := inventories/inventory.yml
UV_RUN         := uv run --python $(PYTHON)
# The sonic-com/arista.eos fork (multiline-RCF-via-eAPI support, needed for
# the FILTER_CGNAT_IMPORTS() control-function push) declares the same
# version number as the official Galaxy release it's based on. ansible-galaxy
# resolves collections by name+version, not source, so installing it via
# `-r requirements.yml` lets the resolver silently substitute the vanilla
# Galaxy copy - even with --force. It must be force-installed on its own,
# with --no-deps, *after* the main requirements.yml install, so it always
# wins.
EOS_FORK_URL   := git+https://github.com/sonic-com/arista.eos.git,bugfix/accept-multiline-input-via-eapi

# TODO(cgnat-toggle): add a CGNAT=on|off variable here that toggles whether
# the CG-NAT appliances (ALPHA-CG-NAT/BETA-CG-NAT, and their peer groups in
# services_internet.yml/services_cg_nat.yml) are in the path at all, vs. a
# simpler direct route between INTERNET and CGNAT for quick iteration -
# rewriting the relevant group_vars YAML before `build`/`deploy` run.

.PHONY: install-uv install build deploy cv-deploy clab clab-persistent destroy destroy-persistent clean

install-uv:
	@command -v uv >/dev/null 2>&1 || curl -LsSf https://astral.sh/uv/install.sh | sh

install: install-uv
	@[ -d $(VENV) ] || uv venv $(VENV)
	uv pip install --python $(PYTHON) 'ansible-core>=2.16.0,<2.21.0'
	$(ANSIBLE_GALAXY) collection install --upgrade -r requirements.yml -p collections/
	$(ANSIBLE_GALAXY) collection install --force --no-deps -p collections/ $(EOS_FORK_URL)
	@# Workaround: AVD 6.4.0 Galaxy package omits plugin_utils/constants.py
	@test -f $(AVD_DIR)/plugins/plugin_utils/constants.py || \
		printf 'from ansible.release import __version__ as ansible_version\nANSIBLE_ABOVE_2_19 = ansible_version.startswith(("2.2", "2.19"))\n' \
		> $(AVD_DIR)/plugins/plugin_utils/constants.py
	uv pip install --python $(PYTHON) -r $(AVD_DIR)/requirements.txt

build: install
	$(UV_RUN) ansible-playbook playbooks/build.yml -i $(INVENTORY)

deploy: install
	$(UV_RUN) ansible-playbook playbooks/deploy.yml -i $(INVENTORY)

cv-deploy: install
	$(UV_RUN) ansible-playbook playbooks/cv-deploy.yml -i $(INVENTORY)

# Brings up the containerlab topology. Re-run to apply topology changes to
# an already-running lab; pass RECONFIGURE=1 to force full node recreation
# (needed when a node's startup-config/binds changed, not just links added).
clab:
	$(CLAB) deploy -t $(CLAB_TOPO) $(if $(RECONFIGURE),--reconfigure)

# Same as `clab`, but onboards into a long-running local CloudVision
# instance: generates sp.persistent.clab.yml (deterministic serial + CVP
# onboarding token per node, see addserial.py) and deploys that instead.
clab-persistent:
	uv run --with ruamel.yaml python3 addserial.py .
	$(MAKE) clab CLAB_TOPO=sp.persistent.clab.yml

destroy:
	$(CLAB) destroy -t $(CLAB_TOPO)

destroy-persistent:
	$(CLAB) destroy -t sp.persistent.clab.yml

clean: destroy
	rm -rf $(VENV) collections/ansible_collections
