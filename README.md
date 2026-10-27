# PSLightwave (AS394437) — AVD Lab

A containerlab-based MPLS service provider lab modeled after [PSLightwave](https://pslightwave.com/)'s Houston-area network, built with [Arista AVD](https://avd.arista.com/). The lab features IS-IS Segment Routing, BGP EVPN with MPLS encapsulation, five real-world transit providers (fully meshed), three DIA delivery models, EVPN-VPWS customer services, and partial PE route filtering with RCF — all generated from AVD data models and deployed to cEOS containers.

![PSLightwave Topology](TX-PS%20Lightwave%20-%20AVD%20Export.png)

## Quick Start

```bash
make clab          # bring up the containerlab topology
make build         # generate EOS intended configs from AVD
make deploy        # push configs to all nodes via eAPI
```

Package management is handled by [uv](https://docs.astral.sh/uv/) via the Makefile. `make build` installs everything automatically — `ansible-core`, the AVD collection, and the [`sonic-com/arista.eos`](https://github.com/sonic-com/arista.eos) fork needed for eAPI config pushes.

---

## Topology

### Fabric Nodes — 6 POP Pairs

Two parallel rows of POP pairs connected in a dual-plane mesh. All PE nodes are 7280CR3AK-24D12 (PE_FULL). Local interlinks use Eth26/1 + Eth28/1 port-channels; WAN links use odd interfaces (Eth25/1, Eth27/1) as single-member port-channels.

**Top row** (west → east): CYWE-A/B → FIBT-A/B → TSHL-A/B

**Bottom row** (west → east): CORP-A/B → CYGA-A/B → CLAK-A/B

**Cross-connects**: CYWE-A↔CORP-A, TSHL-B↔CLAK-B (verticals), CYWE-B↔CYGA-A, FIBT-A↔CORP-B (diagonals)

| Node | ID | Loopback0 | Mgmt IP |
|------|----|-----------|---------|
| CYWE-A | 1 | 172.16.0.1/32 | .128.1 |
| CYWE-B | 2 | 172.16.0.2/32 | .128.2 |
| CORP-A | 3 | 172.16.0.3/32 | .128.3 |
| CORP-B | 4 | 172.16.0.4/32 | .128.4 |
| FIBT-A | 5 | 172.16.0.5/32 | .128.5 |
| FIBT-B | 6 | 172.16.0.6/32 | .128.6 |
| CYGA-A | 7 | 172.16.0.7/32 | .128.7 |
| CYGA-B | 8 | 172.16.0.8/32 | .128.8 |
| TSHL-A | 9 | 172.16.0.9/32 | .128.9 |
| TSHL-B | 10 | 172.16.0.10/32 | .128.10 |
| CLAK-A | 11 | 172.16.0.11/32 | .128.11 |
| CLAK-B | 12 | 172.16.0.12/32 | .128.12 |

### Hub Router

| Node | Platform | ID | Mgmt IP |
|------|----------|----|---------|
| SGRL-A | 7020R4-24Y-6QDF (PE_PARTIAL) | 101 | .128.20 |

SGRL-A connects to CYWE-A (Eth27/1 → Eth1/1) and CORP-A (Eth28/1 → Eth1/1) via the HUB profile (IS-IS metric 100000). As a PE_PARTIAL, it does not carry the full internet table — see [Partial PE Routing](#6-partial-pe-routing).

### Route Reflectors

| Node | Platform | ID | Mgmt IP | Peers |
|------|----------|----|---------|-------|
| CORP-R | 7230R-4TX-4S | 201 | .128.101 | CORP-A, CORP-B |
| FIBT-R | 7230R-4TX-4S | 202 | .128.102 | FIBT-A, FIBT-B |
| CLAK-R | 7230R-4TX-4S | 203 | .128.103 | CLAK-A, CLAK-B |

RR links use Ethernet1/2 on the 7230R side and Eth29/1 on the 24D12 side, with the ROUTE_REFLECTORS profile (IS-IS metric 16777214).

### Management Network

| Setting | Value |
|---------|-------|
| Management VRF | `OOB` |
| Subnet | `192.168.128.0/24` |
| Gateway | `192.168.128.254` |

---

## 1. IS-IS Underlay

IS-IS level-2 with Segment Routing MPLS (no LDP). All 22 core links use IS-IS authentication (MD5) and TI-LFA with node protection.

| Parameter | Value |
|-----------|-------|
| IS-IS Instance | `CORE` |
| IS-type | `level-2` |
| Default metric | `1000` (CORE), `100000` (HUB), `16777214` (RR) |
| Authentication | MD5 on all P2P links |
| TI-LFA | Node protection, 10s local convergence delay |

### Verify

```
show isis neighbors
show isis segment-routing prefix-segments
show mpls lfib route
show isis ti-lfa path
```

---

## 2. BGP EVPN Overlay

iBGP (AS 65000) with EVPN address family, MPLS encapsulation, and RT-membership (RTC). PEs peer only with route reflectors (`bgp_mesh_pes: false`).

| Parameter | Value |
|-----------|-------|
| BGP AS | `65000` |
| Route Reflectors | CORP-R, FIBT-R, CLAK-R |
| EVPN encapsulation | MPLS |
| RT-membership (RTC) | Enabled |
| PE mesh | Disabled (RR-only peering) |

### Verify

```
show bgp evpn summary
show bgp rt-membership summary
```

---

## 3. Transit Peering

Five transit providers peer with PSLightwave (AS394437) in the INTERNET VRF. The TRANSIT cEOS node simulates all five carriers, fully meshed with each other over an internal loopback cable (Eth6↔Eth7, 10 peering pairs).

| Provider | ASN | PE | Interface |
|----------|-----|----|-----------|
| Arelion | 1299 | CYWE-A | Ethernet2/1 |
| Cogent | 174 | CYWE-B | Ethernet2/1 |
| Lumen | 3356 | FIBT-B | Ethernet2/1 |
| NTT | 2914 | TSHL-A | Ethernet2/1 |
| GTT | 3257 | CYGA-A | Ethernet2/1 |

All five transit PEs originate a default route (`0.0.0.0/0` via null0, distance 250) into the INTERNET VRF.

### Realistic Route Table

The TRANSIT node injects **200 prefixes** from 39 real-world origin ASNs (Google, Amazon, Cloudflare, Microsoft, Meta, Apple, Netflix, and 32 others) using **RCF functions** for AS-path injection. Each carrier VRF originates ~40 prefixes via `redistribute static rcf SET_ORIGIN_<CARRIER>()`, and the full carrier mesh propagates them to all five carriers with realistic multi-hop AS paths.

From PSLightwave's perspective, a Google prefix (8.8.8.0/24) shows:

| Via | AS Path | Hops |
|-----|---------|------|
| Arelion (CYWE-A) | `1299 15169` | 2 |
| Cogent (CYWE-B) | `174 1299 15169` | 3 |
| Lumen (FIBT-B) | `3356 1299 15169` | 3 |
| NTT (TSHL-A) | `2914 1299 15169` | 3 |
| GTT (CYGA-A) | `3257 1299 15169` | 3 |

### Carrier Failure Simulation

Shut down any carrier's SP uplink to simulate a carrier outage and observe BGP convergence:

```
# On CYWE-A — shut Arelion uplink
configure
interface Ethernet2/1
   shutdown

# Watch reconvergence on any PE
show ip bgp vrf INTERNET 8.8.8.0/24
```

All 40 Arelion-originated prefixes should reconverge to the remaining four carriers.

### Verify

```
show bgp vrf INTERNET summary
show ip route vrf INTERNET summary
show ip bgp vrf INTERNET | count
```

---

## 4. DIA Services

Three Dedicated Internet Access delivery models, demonstrating how PSLightwave serves customers with different connectivity needs:

### 4a. CUST-D — Direct Full-Table eBGP (CYGA-A)

The simplest DIA model. The customer CE peers directly with a full-table PE and receives the entire internet routing table.

| Parameter | Value |
|-----------|-------|
| CE | CUST-D (AS65503) |
| PE | CYGA-A, Ethernet3/1 |
| CE IP | 198.51.100.24/31 |
| PE IP | 198.51.100.25/31 |
| Peer group | `DIA_FULL_TABLE` |

```
# On CYGA-A
show bgp vrf INTERNET neighbor 198.51.100.24
show ip bgp vrf INTERNET neighbor 198.51.100.24 advertised-routes | count
```

### 4b. CUST-B — Dual-Session DIA (SGRL-A + CYWE-A)

For customers behind a PE_PARTIAL hub. CUST-B has two eBGP sessions — one direct to SGRL-A for partial routes, and one multi-hop to a full-table PE (CYWE-A) for the full internet table.

| Session | Peer | Type | Source | Gets |
|---------|------|------|--------|------|
| SGRL-A | 198.51.100.21 | Direct on P2P | Ethernet1 | Partial table (defaults + tagged routes) |
| CYWE-A | 80.100.0.1 (Lo30) | Multi-hop (TTL 5) | `update-source Ethernet1` (198.51.100.20) | Full internet table |

| Parameter | Value |
|-----------|-------|
| CE | CUST-B (AS65501) |
| PE (partial) | SGRL-A, Ethernet2 |
| PE (full table) | CYWE-A, Loopback30 |
| CE IP | 198.51.100.20/31 |
| PE link IP | 198.51.100.21/31 |
| Customer prefix | 80.50.0.0/24 |

SGRL-A redistributes the connected 198.51.100.20/31 into EVPN, giving CYWE-A reachability to CUST-B's interface for the multi-hop session. SGRL-A also advertises CYWE-A's Loopback30 /32 (learned via EVPN) to CUST-B, enabling the full-table session.

```
# On CUST-B
show bgp summary
show ip bgp neighbor 198.51.100.21 received-routes | count
show ip bgp neighbor 80.100.0.1 received-routes | count
```

### 4c. CUST-C — VPWS Stretch to Full-Table PE (SGRL-A → CYWE-A)

For customers that need the full table but are physically connected to a PE_PARTIAL hub. An EVPN-VPWS pseudowire extends L2 from SGRL-A to CYWE-A (a full-table PE), where the eBGP session terminates. A patch panel loop (Eth4/1 ↔ Eth5/1) on CYWE-A bridges the VPWS to an L3 subinterface.

```
CUST-C ──(VLAN 200)──> SGRL-A:Eth3 ──[VPWS]──> CYWE-A:Eth4/1 ──[patch]──> CYWE-A:Eth5/1.200 (INTERNET VRF)
```

| Parameter | Value |
|-----------|-------|
| CE | CUST-C (AS65502) |
| Physical PE | SGRL-A, Ethernet3 |
| VPWS far-end | CYWE-A, Ethernet4/1 |
| Patch panel | CYWE-A Eth4/1 ↔ Eth5/1 |
| L3 interface | CYWE-A Eth5/1.200 |
| CE IP | 198.51.100.22/31 |
| PE IP | 198.51.100.23/31 |
| Peer group | `DIA_FULL_TABLE` |

```
# On CYWE-A
show patch panel
show bgp vrf INTERNET neighbor 198.51.100.22
```

---

## 5. VPWS — CUST-A ↔ CUST-Z

An EVPN-VPWS pseudowire with **multihomed A-side** (ESI LAG) and **single-homed Z-side**.

The A-side physical attachment is defined via `connected_endpoints` (`endpoints_vpws`) with `channel_id: 1`, ensuring both SGRL-A and CORP-A create Port-Channel1 with matching LACP OperKeys. The VPWS `point_to_point_services` references Port-Channel1 by name for the pseudowire binding.

| Side | Nodes | Interfaces | Port-Channel | ESI |
|------|-------|------------|--------------|-----|
| A-side | SGRL-A + CORP-A | Ethernet1 + Ethernet3/1 | Port-Channel1 (`channel_id: 1`) | `2222:0000:0001` |
| Z-side | CLAK-B | Ethernet3/1 | — | — |

VLAN 100 encapsulation. CUST-A and CUST-Z are cEOS nodes.

### Verify

```
# On CUST-A — both links should be bundled
show port-channel 1 detail
show lacp interface detailed

# On SGRL-A or CORP-A
show bgp evpn route-type auto-discovery
show bgp evpn route-type ethernet-segment
show patch panel

# End-to-end
# From CUST-A: ping 192.168.100.2 source 192.168.100.1
```

---

## 6. Partial PE Routing

SGRL-A is a PE_PARTIAL hub that does not carry the full internet table. Route reflectors use RCF-based EVPN export filtering to limit what INTERNET VRF routes reach SGRL-A.

### Architecture

1. **Community tagging at redistribution**: All PEs run `REDISTRIBUTE_INTERNET()` RCF on the INTERNET VRF's `redistribute static` and `redistribute connected`. This tags locally originated routes (defaults, summary pins, customer allocations) with the `PROVIDER` community (`65000:64496`). Transit routes learned via eBGP are NOT tagged.

2. **RR export filtering**: Each RR has a second BGP peer group (`MPLS-OVERLAY-PEERS-PARTIAL`) with `rcf out EXPORT_PARTIAL()`. SGRL-A peers via this group. The RCF allows:
   - Default routes (`0.0.0.0/0`, `::/0`)
   - Routes tagged with `PROVIDER` (`65000:64496`), `CUSTOMERS` (`65000:4000`), or `CACHES` (`65000:2000`)
   - All non-IP-prefix EVPN route types (MAC/IP, IMET, ES)
   - Blocks all other EVPN IP prefix routes (the full transit table)

3. **RT-membership**: The partial peer group uses `default-route-target only`, so SGRL-A's RT subscriptions still flow normally — filtering happens at the RCF level, not at the RT level.

### Community Lists

| Name | Community | Purpose |
|------|-----------|---------|
| PROVIDER | `65000:64496` | Provider-owned routes (connected, statics, defaults) |
| CUSTOMERS | `65000:4000` | Customer routes (placeholder) |
| CACHES | `65000:2000` | CDN/cache routes (placeholder) |

### Verify

```
# On SGRL-A — should see only defaults + tagged routes, NOT the full 200 transit prefixes
show ip bgp vrf INTERNET | count
show ip bgp vrf INTERNET 0.0.0.0/0

# On a full PE (e.g., CYGA-A) — should see all 200+ prefixes
show ip bgp vrf INTERNET | count

# On an RR — verify RCF is compiled and the partial peer group exists
show router general control-functions code compiled
show bgp neighbor 172.16.0.101 | include peer.group

# Verify community tagging on a transit PE
show ip bgp vrf INTERNET 0.0.0.0/0 detail | grep community
```

---

## 7. Accessing Nodes

### cEOS Nodes (EOS CLI)

```bash
docker exec -it clab-sp-CYWE-A Cli
ssh admin@192.168.128.1
```

### Customer CEs

```bash
docker exec -it clab-sp-CUST-A Cli
docker exec -it clab-sp-CUST-B Cli
docker exec -it clab-sp-CUST-Z Cli
```

---

## Project Structure

```
rsp-tx-pslightwave/
  TX-PS Lightwave - AVD Export.png       # Customer topology diagram
  sp.clab.yml                            # Containerlab topology
  sp.clab.yml.annotations.json           # Containerlab graph layout
  Makefile                               # Build, deploy, clab targets
  requirements.yml                       # Ansible collection requirements
  inventories/
    inventory.yml                        # Ansible inventory
    gen_transit_routes.py                # Prefix/RCF generator for TRANSIT
    assemble_transit.py                  # TRANSIT.yml assembly script
    group_vars/
      all.yml                            # Global settings (AAA, NTP, DNS)
      pe_routers.yml                     # PE policies (prefix-lists, route-maps, communities)
      mpls/
        fabric.yml                       # IS-IS, SR, BGP, node definitions, RCF
        core_interfaces.yml              # 22 backbone links (P2P + port-channels)
        services.yml                     # Network services keys
        vrf_inband_mgmt.yml              # Inband management VRF
      services/
        services_internet.yml            # INTERNET VRF (transit + DIA)
        services_vpws.yml                # VPWS pseudowire bindings
        endpoints_vpws.yml               # VPWS physical attachments (connected_endpoints)
        _db_esi.yml                      # ESI allocation database
        _db_pwire_id.yml                 # Pseudowire ID database
        _svi_profiles.yml                # SVI profiles (legacy)
    host_vars/
      TRANSIT.yml                        # 5-carrier simulator (200 prefixes, RCF)
      CUST-A.yml                         # VPWS CE (A-side, dual-homed)
      CUST-B.yml                         # DIA CE (dual-session: SGRL-A + CYWE-A)
      CUST-C.yml                         # DIA CE (VPWS stretch)
      CUST-D.yml                         # DIA CE (direct full table)
      CUST-Z.yml                         # VPWS CE (Z-side, single-homed)
    intended/
      configs/                           # Generated EOS configs (.cfg)
      structured_configs/                # Generated structured YAML
    documentation/                       # Generated device docs
```
