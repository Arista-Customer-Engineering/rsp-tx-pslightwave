#!/usr/bin/env python3
"""Assemble the complete TRANSIT.yml with 200 prefixes and RCF."""

import sys
sys.path.insert(0, "inventories")
from gen_transit_routes import CARRIERS, VRF_NAME


def rcf_content():
    lines = []
    for carrier_key, data in CARRIERS.items():
        vrf = VRF_NAME[carrier_key]
        func_name = f"SET_ORIGIN_{vrf}"
        lines.append(f"function {func_name}() -> bool {{")
        first = True
        for asn, origin in data["origins"].items():
            pl_name = f'PL_{origin["name"]}_{asn}'
            kw = "if" if first else "elif"
            lines.append(f'   {kw} match(source.prefix, prefix_list_v4("{pl_name}")) {{')
            lines.append(f"      set(source.as_path, [{asn}]);")
            lines.append(f"      return true;")
            lines.append(f"   }}")
            first = False
        lines.append(f"   return false;")
        lines.append(f"}}")
        lines.append("")
    return "\n".join(lines)


def static_routes_yaml():
    lines = []
    lines.append("  - vrf: OOB")
    lines.append("    prefix: 0.0.0.0/0")
    lines.append("    next_hop: 192.168.128.254")
    for carrier_key, data in CARRIERS.items():
        vrf = VRF_NAME[carrier_key]
        for asn, origin in data["origins"].items():
            lines.append(f"  # {origin['name']} (AS{asn})")
            for pfx in origin["prefixes"]:
                lines.append(f"  - vrf: {vrf}")
                lines.append(f'    prefix: {pfx}')
                lines.append(f'    interface: "null0"')
    return "\n".join(lines)


def prefix_lists_yaml():
    lines = []
    for _carrier, data in CARRIERS.items():
        for asn, origin in data["origins"].items():
            lines.append(f'  - name: PL_{origin["name"]}_{asn}')
            lines.append(f"    sequence_numbers:")
            seq = 10
            for pfx in origin["prefixes"]:
                lines.append(f"      - sequence: {seq}")
                lines.append(f'        action: "permit {pfx}"')
                seq += 10
    return "\n".join(lines)


# The full carrier mesh BGP config for a given carrier
def bgp_vrf_yaml(carrier_key, data):
    vrf = VRF_NAME[carrier_key]
    carrier_as = data["as"]
    func_name = f"SET_ORIGIN_{vrf}"

    # Map carrier to SP uplink info
    sp_map = {
        "ARELION": ("198.51.100.1", "2601::1", "CYWE-A", "100.64.255.1"),
        "COGENT": ("198.51.100.3", "2602::1", "CYWE-B", "100.64.255.2"),
        "LUMEN": ("198.51.100.5", "2603::1", "FIBT-B", "100.64.255.3"),
        "NTT_VRF": ("198.51.100.7", "2604::1", "TSHL-A", "100.64.255.4"),
        "GTT": ("198.51.100.9", "2605::1", "CYGA-A", "100.64.255.5"),
    }
    sp_ipv4, sp_ipv6, sp_node, router_id = sp_map[carrier_key]

    # Build mesh neighbor list — carrier position scheme:
    # 1=ARELION, 2=COGENT, 3=LUMEN, 4=NTT, 5=GTT
    carrier_pos = {"ARELION": 1, "COGENT": 2, "LUMEN": 3, "NTT_VRF": 4, "GTT": 5}
    carrier_info = {
        "ARELION": ("1299", "ARELION"),
        "COGENT": ("174", "COGENT"),
        "LUMEN": ("3356", "LUMEN"),
        "NTT_VRF": ("2914", "NTT"),
        "GTT": ("3257", "GTT"),
    }
    my_pos = carrier_pos[carrier_key]

    mesh_neighbors = []
    mesh_activate = []
    for other_key, (other_as, other_name) in carrier_info.items():
        if other_key == carrier_key:
            continue
        other_pos = carrier_pos[other_key]
        lo = min(my_pos, other_pos)
        hi = max(my_pos, other_pos)
        vlan = lo * 10 + hi
        if my_pos < other_pos:
            my_ip_suffix = "0"
            peer_ip_suffix = "1"
        else:
            my_ip_suffix = "1"
            peer_ip_suffix = "0"
        peer_ip = f"10.99.{vlan}.{peer_ip_suffix}"
        mesh_neighbors.append(
            f"        - ip_address: {peer_ip}\n"
            f"          remote_as: '{other_as}'\n"
            f"          local_as: '{carrier_as}'\n"
            f'          description: "{other_name} (AS{other_as})"\n'
            f"          shutdown: false"
        )
        mesh_activate.append(
            f"          - ip_address: {peer_ip}\n"
            f"            activate: true"
        )

    lines = f"""    - name: {vrf}
      router_id: {router_id}
      redistribute:
        connected:
          enabled: true
        static:
          enabled: true
          rcf: "{func_name}()"
      neighbors:
        # SP uplink
        - ip_address: {sp_ipv4}
          remote_as: '394437'
          local_as: '{carrier_as}'
          description: "{sp_node} (AS394437)"
          shutdown: false
        - ip_address: {sp_ipv6}
          remote_as: '394437'
          local_as: '{carrier_as}'
          description: "{sp_node} (AS394437) IPv6"
          shutdown: false
        # Carrier mesh
{chr(10).join(mesh_neighbors)}
      address_family_ipv4:
        neighbors:
          - ip_address: {sp_ipv4}
            activate: true
{chr(10).join(mesh_activate)}
      address_family_ipv6:
        neighbors:
          - ip_address: {sp_ipv6}
            activate: true"""
    return lines


if __name__ == "__main__":
    bgp_vrfs = []
    for carrier_key, data in CARRIERS.items():
        vrf = VRF_NAME[carrier_key]
        bgp_vrfs.append(f"    ##################################################################")
        bgp_vrfs.append(f"    # {vrf} (AS{data['as']})")
        bgp_vrfs.append(f"    ##################################################################")
        bgp_vrfs.append(bgp_vrf_yaml(carrier_key, data))

    rcf = rcf_content()

    print(f"""\
---
# TRANSIT simulates five independent Tier-1 transit carriers (Arelion,
# Cogent, Lumen, NTT, GTT) on one cEOS box. Each carrier gets its own
# VRF with an uplink into the SP fabric (Eth1-5). All five carriers are
# fully meshed with each other over the Ethernet6<->Ethernet7 loopback
# cable (10 peering pairs), so routes propagate realistically — shutting
# down one carrier's SP uplink will cause PSLightwave to reconverge
# through the remaining four.
#
# 200 realistic prefixes (40 per carrier) from well-known origin ASNs
# (Google, Cloudflare, AWS, Meta, Apple, etc.) are injected via static
# routes with RCF-based AS-path replacement. The carrier mesh naturally
# builds multi-hop AS paths from PSLightwave's (AS394437) perspective.
#
# Loopback cable VLAN scheme: VLAN {{ij}} for carrier pair i<->j
#   1=ARELION, 2=COGENT, 3=LUMEN, 4=NTT, 5=GTT
#   Eth6 = lower-numbered carrier, Eth7 = higher-numbered carrier
#   IP: 10.99.{{ij}}.0/31 (Eth6=.0, Eth7=.1)
hostname: TRANSIT

aaa_authentication:
  login:
    default: local
    console: local
aaa_authorization:
  exec:
    default: local

ip_routing: true
service_routing_protocols_model: multi-agent

local_users:
  - name: admin
    privilege: 15
    role: network-admin
    sha512_password: $6$n5UzLR7bucITZ.fE$BoS3AU71MBIDlSsWb1NpH0P62l9AyanxImmA.9OKesBuClBXXae3oMf0fm1HA.3rxwzvbkbVl.QarZAHgm7V81
  - name: dave.watkins
    privilege: 15
    role: network-admin
    sha512_password: $6$n5UzLR7bucITZ.fE$BoS3AU71MBIDlSsWb1NpH0P62l9AyanxImmA.9OKesBuClBXXae3oMf0fm1HA.3rxwzvbkbVl.QarZAHgm7V81

management_interfaces:
  - name: Management0
    description: OOB_MANAGEMENT
    shutdown: false
    vrf: OOB
    ip_address: 192.168.128.220/24
    type: oob
    gateway: 192.168.128.254
    eos_cli: |
      no lldp transmit
      no lldp receive

management_api_http:
  enable_https: true
  enable_vrfs:
    - name: OOB

vrfs:
  - name: OOB
    ip_routing: false
  - name: ARELION
    description: "Arelion (AS1299)"
    ip_routing: true
  - name: COGENT
    description: "Cogent (AS174)"
    ip_routing: true
  - name: LUMEN
    description: "Lumen (AS3356)"
    ip_routing: true
  - name: NTT
    description: "NTT (AS2914)"
    ip_routing: true
  - name: GTT
    description: "GTT (AS3257)"
    ip_routing: true

ethernet_interfaces:
  ##################################################################
  # SP fabric uplinks — one per carrier
  ##################################################################
  - name: Ethernet1
    description: "CYWE-A Ethernet2/1 (Arelion uplink)"
    shutdown: false
    vrf: ARELION
    ip_address: 198.51.100.0/31
    ipv6_enable: true
    ipv6_addresses:
      - 2601::0/127
    ipv6_nd:
      ra:
        disabled: true
    switchport:
      enabled: false
  - name: Ethernet2
    description: "CYWE-B Ethernet2/1 (Cogent uplink)"
    shutdown: false
    vrf: COGENT
    ip_address: 198.51.100.2/31
    ipv6_enable: true
    ipv6_addresses:
      - 2602::0/127
    ipv6_nd:
      ra:
        disabled: true
    switchport:
      enabled: false
  - name: Ethernet3
    description: "FIBT-B Ethernet2/1 (Lumen uplink)"
    shutdown: false
    vrf: LUMEN
    ip_address: 198.51.100.4/31
    ipv6_enable: true
    ipv6_addresses:
      - 2603::0/127
    ipv6_nd:
      ra:
        disabled: true
    switchport:
      enabled: false
  - name: Ethernet4
    description: "TSHL-A Ethernet2/1 (NTT uplink)"
    shutdown: false
    vrf: NTT
    ip_address: 198.51.100.6/31
    ipv6_enable: true
    ipv6_addresses:
      - 2604::0/127
    ipv6_nd:
      ra:
        disabled: true
    switchport:
      enabled: false
  - name: Ethernet5
    description: "CYGA-A Ethernet2/1 (GTT uplink)"
    shutdown: false
    vrf: GTT
    ip_address: 198.51.100.8/31
    ipv6_enable: true
    ipv6_addresses:
      - 2605::0/127
    ipv6_nd:
      ra:
        disabled: true
    switchport:
      enabled: false

  ##################################################################
  # Carrier full-mesh — Ethernet6<->Ethernet7 loopback cable
  # 10 peering pairs, Eth6 = lower carrier, Eth7 = higher carrier
  ##################################################################
  - name: Ethernet6
    shutdown: false
    switchport:
      enabled: false
  - name: Ethernet7
    shutdown: false
    switchport:
      enabled: false

  # --- ARELION(1) <-> COGENT(2) — VLAN 12 ---
  - name: Ethernet6.12
    description: "Arelion <-> Cogent"
    shutdown: false
    vrf: ARELION
    encapsulation_vlan:
      client:
        encapsulation: dot1q
        vlan: 12
    ip_address: 10.99.12.0/31
  - name: Ethernet7.12
    description: "Cogent <-> Arelion"
    shutdown: false
    vrf: COGENT
    encapsulation_vlan:
      client:
        encapsulation: dot1q
        vlan: 12
    ip_address: 10.99.12.1/31

  # --- ARELION(1) <-> LUMEN(3) — VLAN 13 ---
  - name: Ethernet6.13
    description: "Arelion <-> Lumen"
    shutdown: false
    vrf: ARELION
    encapsulation_vlan:
      client:
        encapsulation: dot1q
        vlan: 13
    ip_address: 10.99.13.0/31
  - name: Ethernet7.13
    description: "Lumen <-> Arelion"
    shutdown: false
    vrf: LUMEN
    encapsulation_vlan:
      client:
        encapsulation: dot1q
        vlan: 13
    ip_address: 10.99.13.1/31

  # --- ARELION(1) <-> NTT(4) — VLAN 14 ---
  - name: Ethernet6.14
    description: "Arelion <-> NTT"
    shutdown: false
    vrf: ARELION
    encapsulation_vlan:
      client:
        encapsulation: dot1q
        vlan: 14
    ip_address: 10.99.14.0/31
  - name: Ethernet7.14
    description: "NTT <-> Arelion"
    shutdown: false
    vrf: NTT
    encapsulation_vlan:
      client:
        encapsulation: dot1q
        vlan: 14
    ip_address: 10.99.14.1/31

  # --- ARELION(1) <-> GTT(5) — VLAN 15 ---
  - name: Ethernet6.15
    description: "Arelion <-> GTT"
    shutdown: false
    vrf: ARELION
    encapsulation_vlan:
      client:
        encapsulation: dot1q
        vlan: 15
    ip_address: 10.99.15.0/31
  - name: Ethernet7.15
    description: "GTT <-> Arelion"
    shutdown: false
    vrf: GTT
    encapsulation_vlan:
      client:
        encapsulation: dot1q
        vlan: 15
    ip_address: 10.99.15.1/31

  # --- COGENT(2) <-> LUMEN(3) — VLAN 23 ---
  - name: Ethernet6.23
    description: "Cogent <-> Lumen"
    shutdown: false
    vrf: COGENT
    encapsulation_vlan:
      client:
        encapsulation: dot1q
        vlan: 23
    ip_address: 10.99.23.0/31
  - name: Ethernet7.23
    description: "Lumen <-> Cogent"
    shutdown: false
    vrf: LUMEN
    encapsulation_vlan:
      client:
        encapsulation: dot1q
        vlan: 23
    ip_address: 10.99.23.1/31

  # --- COGENT(2) <-> NTT(4) — VLAN 24 ---
  - name: Ethernet6.24
    description: "Cogent <-> NTT"
    shutdown: false
    vrf: COGENT
    encapsulation_vlan:
      client:
        encapsulation: dot1q
        vlan: 24
    ip_address: 10.99.24.0/31
  - name: Ethernet7.24
    description: "NTT <-> Cogent"
    shutdown: false
    vrf: NTT
    encapsulation_vlan:
      client:
        encapsulation: dot1q
        vlan: 24
    ip_address: 10.99.24.1/31

  # --- COGENT(2) <-> GTT(5) — VLAN 25 ---
  - name: Ethernet6.25
    description: "Cogent <-> GTT"
    shutdown: false
    vrf: COGENT
    encapsulation_vlan:
      client:
        encapsulation: dot1q
        vlan: 25
    ip_address: 10.99.25.0/31
  - name: Ethernet7.25
    description: "GTT <-> Cogent"
    shutdown: false
    vrf: GTT
    encapsulation_vlan:
      client:
        encapsulation: dot1q
        vlan: 25
    ip_address: 10.99.25.1/31

  # --- LUMEN(3) <-> NTT(4) — VLAN 34 ---
  - name: Ethernet6.34
    description: "Lumen <-> NTT"
    shutdown: false
    vrf: LUMEN
    encapsulation_vlan:
      client:
        encapsulation: dot1q
        vlan: 34
    ip_address: 10.99.34.0/31
  - name: Ethernet7.34
    description: "NTT <-> Lumen"
    shutdown: false
    vrf: NTT
    encapsulation_vlan:
      client:
        encapsulation: dot1q
        vlan: 34
    ip_address: 10.99.34.1/31

  # --- LUMEN(3) <-> GTT(5) — VLAN 35 ---
  - name: Ethernet6.35
    description: "Lumen <-> GTT"
    shutdown: false
    vrf: LUMEN
    encapsulation_vlan:
      client:
        encapsulation: dot1q
        vlan: 35
    ip_address: 10.99.35.0/31
  - name: Ethernet7.35
    description: "GTT <-> Lumen"
    shutdown: false
    vrf: GTT
    encapsulation_vlan:
      client:
        encapsulation: dot1q
        vlan: 35
    ip_address: 10.99.35.1/31

  # --- NTT(4) <-> GTT(5) — VLAN 45 ---
  - name: Ethernet6.45
    description: "NTT <-> GTT"
    shutdown: false
    vrf: NTT
    encapsulation_vlan:
      client:
        encapsulation: dot1q
        vlan: 45
    ip_address: 10.99.45.0/31
  - name: Ethernet7.45
    description: "GTT <-> NTT"
    shutdown: false
    vrf: GTT
    encapsulation_vlan:
      client:
        encapsulation: dot1q
        vlan: 45
    ip_address: 10.99.45.1/31

##################################################################
# 200 realistic prefixes — 40 per carrier, null-routed statics
# Each prefix is originated by one carrier and learned by all
# others via the Eth6<->Eth7 full mesh.
##################################################################
static_routes:
{static_routes_yaml()}

##################################################################
# Prefix lists — one per origin AS, used by RCF functions
##################################################################
prefix_lists:
{prefix_lists_yaml()}

##################################################################
# RCF — AS-path injection on static redistribution
# Each carrier's function sets the origin AS on its static routes.
# The carrier mesh naturally builds realistic multi-hop AS paths:
#   - Google via Arelion direct:  AS path = 1299 15169
#   - Google via Cogent mesh:     AS path = 174 1299 15169
#   - Google via Lumen mesh:      AS path = 3356 1299 15169
##################################################################
router_general:
  control_functions:
    code_units:
      - name: TRANSIT_ROUTE_ORIGINS
        content: |
{chr(10).join('          ' + line if line else '' for line in rcf.split(chr(10)))}

router_bgp:
  as: '65000'
  router_id: 100.64.255.0
  vrfs:
{chr(10).join(bgp_vrfs)}
""")
