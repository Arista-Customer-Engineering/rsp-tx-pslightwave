# mpls

## Table of Contents

- [Fabric Switches and Management IP](#fabric-switches-and-management-ip)
  - [Fabric Switches with inband Management IP](#fabric-switches-with-inband-management-ip)
- [Fabric Topology](#fabric-topology)
- [Fabric IP Allocation](#fabric-ip-allocation)
  - [Fabric Point-To-Point Links](#fabric-point-to-point-links)
  - [Point-To-Point Links Node Allocation](#point-to-point-links-node-allocation)
  - [Loopback Interfaces (BGP EVPN Peering)](#loopback-interfaces-bgp-evpn-peering)
  - [Loopback0 Interfaces Node Allocation](#loopback0-interfaces-node-allocation)
  - [ISIS CLNS interfaces](#isis-clns-interfaces)
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| RSP | pe | CLAK-A | 192.168.128.11/24 | 7280SR3 | Provisioned | - |
| RSP | pe | CLAK-B | 192.168.128.12/24 | 7280SR3 | Provisioned | - |
| RSP | rr | CLAK-R | 192.168.128.103/24 | 7280SR3 | Provisioned | - |
| RSP | pe | CORP-A | 192.168.128.3/24 | 7280SR3 | Provisioned | - |
| RSP | pe | CORP-B | 192.168.128.4/24 | 7280SR3 | Provisioned | - |
| RSP | rr | CORP-R | 192.168.128.101/24 | 7280SR3 | Provisioned | - |
| RSP | pe | CYGA-A | 192.168.128.7/24 | 7280SR3 | Provisioned | - |
| RSP | pe | CYGA-B | 192.168.128.8/24 | 7280SR3 | Provisioned | - |
| RSP | pe | CYWE-A | 192.168.128.1/24 | 7280SR3 | Provisioned | - |
| RSP | pe | CYWE-B | 192.168.128.2/24 | 7280SR3 | Provisioned | - |
| RSP | pe | FIBT-A | 192.168.128.5/24 | 7280SR3 | Provisioned | - |
| RSP | pe | FIBT-B | 192.168.128.6/24 | 7280SR3 | Provisioned | - |
| RSP | rr | FIBT-R | 192.168.128.102/24 | 7280SR3 | Provisioned | - |
| RSP | pe | SGRL-A | 192.168.128.20/24 | 7280SR3 | Provisioned | - |
| RSP | pe | TSHL-A | 192.168.128.9/24 | 7280SR3 | Provisioned | - |
| RSP | pe | TSHL-B | 192.168.128.10/24 | 7280SR3 | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | --------- | -------------- |
| pe | CLAK-A | Ethernet25/1 | pe | CYGA-B | Ethernet25/1 |
| pe | CLAK-A | Ethernet26/1 | pe | CLAK-B | Ethernet26/1 |
| pe | CLAK-A | Ethernet28/1 | pe | CLAK-B | Ethernet28/1 |
| pe | CLAK-A | Ethernet29/1 | rr | CLAK-R | Ethernet1 |
| pe | CLAK-B | Ethernet25/1 | pe | TSHL-B | Ethernet25/1 |
| pe | CLAK-B | Ethernet29/1 | rr | CLAK-R | Ethernet2 |
| pe | CORP-A | Ethernet1/1 | pe | SGRL-A | Ethernet28/1 |
| pe | CORP-A | Ethernet25/1 | pe | CYWE-A | Ethernet25/1 |
| pe | CORP-A | Ethernet26/1 | pe | CORP-B | Ethernet26/1 |
| pe | CORP-A | Ethernet28/1 | pe | CORP-B | Ethernet28/1 |
| pe | CORP-A | Ethernet29/1 | rr | CORP-R | Ethernet1 |
| pe | CORP-B | Ethernet25/1 | pe | CYGA-A | Ethernet25/1 |
| pe | CORP-B | Ethernet27/1 | pe | FIBT-A | Ethernet27/1 |
| pe | CORP-B | Ethernet29/1 | rr | CORP-R | Ethernet2 |
| pe | CYGA-A | Ethernet26/1 | pe | CYGA-B | Ethernet26/1 |
| pe | CYGA-A | Ethernet27/1 | pe | CYWE-B | Ethernet27/1 |
| pe | CYGA-A | Ethernet28/1 | pe | CYGA-B | Ethernet28/1 |
| pe | CYWE-A | Ethernet1/1 | pe | SGRL-A | Ethernet27/1 |
| pe | CYWE-A | Ethernet26/1 | pe | CYWE-B | Ethernet26/1 |
| pe | CYWE-A | Ethernet28/1 | pe | CYWE-B | Ethernet28/1 |
| pe | CYWE-B | Ethernet25/1 | pe | FIBT-A | Ethernet25/1 |
| pe | FIBT-A | Ethernet26/1 | pe | FIBT-B | Ethernet26/1 |
| pe | FIBT-A | Ethernet28/1 | pe | FIBT-B | Ethernet28/1 |
| pe | FIBT-A | Ethernet29/1 | rr | FIBT-R | Ethernet1 |
| pe | FIBT-B | Ethernet25/1 | pe | TSHL-A | Ethernet25/1 |
| pe | FIBT-B | Ethernet29/1 | rr | FIBT-R | Ethernet2 |
| pe | TSHL-A | Ethernet26/1 | pe | TSHL-B | Ethernet26/1 |
| pe | TSHL-A | Ethernet28/1 | pe | TSHL-B | Ethernet28/1 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| CLAK-A | Ethernet29/1 | 172.17.0.41/31 | CLAK-R | Ethernet1 | 172.17.0.40/31 |
| CLAK-B | Ethernet29/1 | 172.17.0.43/31 | CLAK-R | Ethernet2 | 172.17.0.42/31 |
| CORP-A | Ethernet29/1 | 172.17.0.33/31 | CORP-R | Ethernet1 | 172.17.0.32/31 |
| CORP-B | Ethernet29/1 | 172.17.0.35/31 | CORP-R | Ethernet2 | 172.17.0.34/31 |
| FIBT-A | Ethernet29/1 | 172.17.0.37/31 | FIBT-R | Ethernet1 | 172.17.0.36/31 |
| FIBT-B | Ethernet29/1 | 172.17.0.39/31 | FIBT-R | Ethernet2 | 172.17.0.38/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 172.16.0.0/24 | 256 | 16 | 6.25 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| RSP | CLAK-A | 172.16.0.11/32 |
| RSP | CLAK-B | 172.16.0.12/32 |
| RSP | CLAK-R | 172.16.0.203/32 |
| RSP | CORP-A | 172.16.0.3/32 |
| RSP | CORP-B | 172.16.0.4/32 |
| RSP | CORP-R | 172.16.0.201/32 |
| RSP | CYGA-A | 172.16.0.7/32 |
| RSP | CYGA-B | 172.16.0.8/32 |
| RSP | CYWE-A | 172.16.0.1/32 |
| RSP | CYWE-B | 172.16.0.2/32 |
| RSP | FIBT-A | 172.16.0.5/32 |
| RSP | FIBT-B | 172.16.0.6/32 |
| RSP | FIBT-R | 172.16.0.202/32 |
| RSP | SGRL-A | 172.16.0.101/32 |
| RSP | TSHL-A | 172.16.0.9/32 |
| RSP | TSHL-B | 172.16.0.10/32 |

### ISIS CLNS interfaces

| POD | Node | CLNS Address |
| --- | ---- | ------------ |
| RSP | CLAK-A | 49.0001.1720.1600.0011.00 |
| RSP | CLAK-B | 49.0001.1720.1600.0012.00 |
| RSP | CLAK-R | 49.0001.1720.1600.0203.00 |
| RSP | CORP-A | 49.0001.1720.1600.0003.00 |
| RSP | CORP-B | 49.0001.1720.1600.0004.00 |
| RSP | CORP-R | 49.0001.1720.1600.0201.00 |
| RSP | CYGA-A | 49.0001.1720.1600.0007.00 |
| RSP | CYGA-B | 49.0001.1720.1600.0008.00 |
| RSP | CYWE-A | 49.0001.1720.1600.0001.00 |
| RSP | CYWE-B | 49.0001.1720.1600.0002.00 |
| RSP | FIBT-A | 49.0001.1720.1600.0005.00 |
| RSP | FIBT-B | 49.0001.1720.1600.0006.00 |
| RSP | FIBT-R | 49.0001.1720.1600.0202.00 |
| RSP | SGRL-A | 49.0001.1720.1600.0101.00 |
| RSP | TSHL-A | 49.0001.1720.1600.0009.00 |
| RSP | TSHL-B | 49.0001.1720.1600.0010.00 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------------ | ------------------- | ------------------ | ------------------ |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
