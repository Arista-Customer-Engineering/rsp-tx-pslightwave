# TRANSIT

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
  - [AAA Authentication](#aaa-authentication)
  - [AAA Authorization](#aaa-authorization)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router General](#router-general)
  - [Router BGP](#router-bgp)
- [Filters](#filters)
  - [Prefix-lists](#prefix-lists)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management0 | OOB_MANAGEMENT | oob | OOB | 192.168.128.220/24 | 192.168.128.254 |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway | ND RA Disabled | ND RA RX Accept | ND Managed Config Flag | ND Other Config Flag | ND Cache | ND RA DNS Servers |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ | -------------- | --------------- | ---------------------- | -------------------- | -------- | ----------------- |
| Management0 | OOB_MANAGEMENT | oob | OOB | - | - | - | - | - | - | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management0
   description OOB_MANAGEMENT
   no shutdown
   vrf OOB
   ip address 192.168.128.220/24
   no lldp transmit
   no lldp receive

```

### Management API HTTP

#### Management API HTTP Summary

| HTTP | HTTPS | UNIX-Socket | Default Services | Session Timeout |
| ---- | ----- | ----------- | ---------------- | --------------- |
| False | True | - | - | 1440 minutes |

#### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| OOB | - | - |

#### Management API HTTP Device Configuration

```eos
!
management api http-commands
   protocol https
   no shutdown
   !
   vrf OOB
      no shutdown
```

## Authentication

### Local Users

#### Local Users Summary

| User | Privilege | Role | Disabled | Shell |
| ---- | --------- | ---- | -------- | ----- |
| admin | 15 | network-admin | False | - |
| dave.watkins | 15 | network-admin | False | - |

#### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin secret sha512 <removed>
username dave.watkins privilege 15 role network-admin secret sha512 <removed>
```

### AAA Authentication

#### AAA Authentication Summary

| Type | Sub-type | User Stores |
| ---- | -------- | ---------- |
| Login | default | local |
| Login | console | local |

#### AAA Authentication Device Configuration

```eos
aaa authentication login default local
aaa authentication login console local
!
```

### AAA Authorization

#### AAA Authorization Summary

| Type | User Stores |
| ---- | ----------- |
| Exec | local |

Authorization for configuration commands is disabled.

#### AAA Authorization Device Configuration

```eos
aaa authorization exec default local
!
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |

*Inherited from Port-Channel Interface

##### Flexible Encapsulation Interfaces

| Interface | Description | Vlan ID | Client Encapsulation | Client Inner Encapsulation | Client VLAN | Client Outer VLAN Tag | Client Inner VLAN Tag | Network Encapsulation | Network Inner Encapsulation | Network VLAN | Network Outer VLAN Tag | Network Inner VLAN Tag |
| --------- | ----------- | ------- | -------------------- | -------------------------- | ----------- | --------------------- | --------------------- | --------------------- | --------------------------- | ------------ | ---------------------- | ---------------------- |
| Ethernet6.12 | Arelion <-> Cogent | - | dot1q | - | 12 | - | - | - | - | - | - | - |
| Ethernet6.13 | Arelion <-> Lumen | - | dot1q | - | 13 | - | - | - | - | - | - | - |
| Ethernet6.14 | Arelion <-> NTT | - | dot1q | - | 14 | - | - | - | - | - | - | - |
| Ethernet6.15 | Arelion <-> GTT | - | dot1q | - | 15 | - | - | - | - | - | - | - |
| Ethernet6.23 | Cogent <-> Lumen | - | dot1q | - | 23 | - | - | - | - | - | - | - |
| Ethernet6.24 | Cogent <-> NTT | - | dot1q | - | 24 | - | - | - | - | - | - | - |
| Ethernet6.25 | Cogent <-> GTT | - | dot1q | - | 25 | - | - | - | - | - | - | - |
| Ethernet6.34 | Lumen <-> NTT | - | dot1q | - | 34 | - | - | - | - | - | - | - |
| Ethernet6.35 | Lumen <-> GTT | - | dot1q | - | 35 | - | - | - | - | - | - | - |
| Ethernet6.45 | NTT <-> GTT | - | dot1q | - | 45 | - | - | - | - | - | - | - |
| Ethernet7.12 | Cogent <-> Arelion | - | dot1q | - | 12 | - | - | - | - | - | - | - |
| Ethernet7.13 | Lumen <-> Arelion | - | dot1q | - | 13 | - | - | - | - | - | - | - |
| Ethernet7.14 | NTT <-> Arelion | - | dot1q | - | 14 | - | - | - | - | - | - | - |
| Ethernet7.15 | GTT <-> Arelion | - | dot1q | - | 15 | - | - | - | - | - | - | - |
| Ethernet7.23 | Lumen <-> Cogent | - | dot1q | - | 23 | - | - | - | - | - | - | - |
| Ethernet7.24 | NTT <-> Cogent | - | dot1q | - | 24 | - | - | - | - | - | - | - |
| Ethernet7.25 | GTT <-> Cogent | - | dot1q | - | 25 | - | - | - | - | - | - | - |
| Ethernet7.34 | NTT <-> Lumen | - | dot1q | - | 34 | - | - | - | - | - | - | - |
| Ethernet7.35 | GTT <-> Lumen | - | dot1q | - | 35 | - | - | - | - | - | - | - |
| Ethernet7.45 | GTT <-> NTT | - | dot1q | - | 45 | - | - | - | - | - | - | - |

##### IPv4

| Interface | Description | Channel Group | IP Address | VRF | MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------------- | ---------- | --- | --- | -------- | ------ | ------- |
| Ethernet1 | CYWE-A Ethernet2/1 (Arelion uplink) | - | 198.51.100.0/31 | ARELION | - | False | - | - |
| Ethernet2 | CYWE-B Ethernet2/1 (Cogent uplink) | - | 198.51.100.2/31 | COGENT | - | False | - | - |
| Ethernet3 | FIBT-B Ethernet2/1 (Lumen uplink) | - | 198.51.100.4/31 | LUMEN | - | False | - | - |
| Ethernet4 | TSHL-A Ethernet2/1 (NTT uplink) | - | 198.51.100.6/31 | NTT | - | False | - | - |
| Ethernet5 | CYGA-A Ethernet2/1 (GTT uplink) | - | 198.51.100.8/31 | GTT | - | False | - | - |
| Ethernet6.12 | Arelion <-> Cogent | - | 10.99.12.0/31 | ARELION | - | False | - | - |
| Ethernet6.13 | Arelion <-> Lumen | - | 10.99.13.0/31 | ARELION | - | False | - | - |
| Ethernet6.14 | Arelion <-> NTT | - | 10.99.14.0/31 | ARELION | - | False | - | - |
| Ethernet6.15 | Arelion <-> GTT | - | 10.99.15.0/31 | ARELION | - | False | - | - |
| Ethernet6.23 | Cogent <-> Lumen | - | 10.99.23.0/31 | COGENT | - | False | - | - |
| Ethernet6.24 | Cogent <-> NTT | - | 10.99.24.0/31 | COGENT | - | False | - | - |
| Ethernet6.25 | Cogent <-> GTT | - | 10.99.25.0/31 | COGENT | - | False | - | - |
| Ethernet6.34 | Lumen <-> NTT | - | 10.99.34.0/31 | LUMEN | - | False | - | - |
| Ethernet6.35 | Lumen <-> GTT | - | 10.99.35.0/31 | LUMEN | - | False | - | - |
| Ethernet6.45 | NTT <-> GTT | - | 10.99.45.0/31 | NTT | - | False | - | - |
| Ethernet7.12 | Cogent <-> Arelion | - | 10.99.12.1/31 | COGENT | - | False | - | - |
| Ethernet7.13 | Lumen <-> Arelion | - | 10.99.13.1/31 | LUMEN | - | False | - | - |
| Ethernet7.14 | NTT <-> Arelion | - | 10.99.14.1/31 | NTT | - | False | - | - |
| Ethernet7.15 | GTT <-> Arelion | - | 10.99.15.1/31 | GTT | - | False | - | - |
| Ethernet7.23 | Lumen <-> Cogent | - | 10.99.23.1/31 | LUMEN | - | False | - | - |
| Ethernet7.24 | NTT <-> Cogent | - | 10.99.24.1/31 | NTT | - | False | - | - |
| Ethernet7.25 | GTT <-> Cogent | - | 10.99.25.1/31 | GTT | - | False | - | - |
| Ethernet7.34 | NTT <-> Lumen | - | 10.99.34.1/31 | NTT | - | False | - | - |
| Ethernet7.35 | GTT <-> Lumen | - | 10.99.35.1/31 | GTT | - | False | - | - |
| Ethernet7.45 | GTT <-> NTT | - | 10.99.45.1/31 | GTT | - | False | - | - |

##### IPv6

| Interface | Description | Channel Group | IPv6 Addresses | VRF | MTU | Shutdown | ND RA Disabled | ND RA RX Accept | ND Managed Config Flag | ND Other Config Flag | ND Cache | ND RA DNS Servers | IPv6 ACL In | IPv6 ACL Out |
| --------- | ----------- | ------------- | -------------- | --- | --- | -------- | -------------- | --------------- | ---------------------- | -------------------- | -------- | ----------------- | ----------- | ------------ |
| Ethernet1 | CYWE-A Ethernet2/1 (Arelion uplink) | - | 2601::0/127 | ARELION | - | False | True | - | - | - | - | - | - | - |
| Ethernet2 | CYWE-B Ethernet2/1 (Cogent uplink) | - | 2602::0/127 | COGENT | - | False | True | - | - | - | - | - | - | - |
| Ethernet3 | FIBT-B Ethernet2/1 (Lumen uplink) | - | 2603::0/127 | LUMEN | - | False | True | - | - | - | - | - | - | - |
| Ethernet4 | TSHL-A Ethernet2/1 (NTT uplink) | - | 2604::0/127 | NTT | - | False | True | - | - | - | - | - | - | - |
| Ethernet5 | CYGA-A Ethernet2/1 (GTT uplink) | - | 2605::0/127 | GTT | - | False | True | - | - | - | - | - | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description CYWE-A Ethernet2/1 (Arelion uplink)
   no shutdown
   no switchport
   vrf ARELION
   ip address 198.51.100.0/31
   ipv6 enable
   ipv6 address 2601::0/127
   ipv6 nd ra disabled
!
interface Ethernet2
   description CYWE-B Ethernet2/1 (Cogent uplink)
   no shutdown
   no switchport
   vrf COGENT
   ip address 198.51.100.2/31
   ipv6 enable
   ipv6 address 2602::0/127
   ipv6 nd ra disabled
!
interface Ethernet3
   description FIBT-B Ethernet2/1 (Lumen uplink)
   no shutdown
   no switchport
   vrf LUMEN
   ip address 198.51.100.4/31
   ipv6 enable
   ipv6 address 2603::0/127
   ipv6 nd ra disabled
!
interface Ethernet4
   description TSHL-A Ethernet2/1 (NTT uplink)
   no shutdown
   no switchport
   vrf NTT
   ip address 198.51.100.6/31
   ipv6 enable
   ipv6 address 2604::0/127
   ipv6 nd ra disabled
!
interface Ethernet5
   description CYGA-A Ethernet2/1 (GTT uplink)
   no shutdown
   no switchport
   vrf GTT
   ip address 198.51.100.8/31
   ipv6 enable
   ipv6 address 2605::0/127
   ipv6 nd ra disabled
!
interface Ethernet6
   no shutdown
   no switchport
!
interface Ethernet6.12
   description Arelion <-> Cogent
   no shutdown
   encapsulation vlan
      client dot1q 12
   vrf ARELION
   ip address 10.99.12.0/31
!
interface Ethernet6.13
   description Arelion <-> Lumen
   no shutdown
   encapsulation vlan
      client dot1q 13
   vrf ARELION
   ip address 10.99.13.0/31
!
interface Ethernet6.14
   description Arelion <-> NTT
   no shutdown
   encapsulation vlan
      client dot1q 14
   vrf ARELION
   ip address 10.99.14.0/31
!
interface Ethernet6.15
   description Arelion <-> GTT
   no shutdown
   encapsulation vlan
      client dot1q 15
   vrf ARELION
   ip address 10.99.15.0/31
!
interface Ethernet6.23
   description Cogent <-> Lumen
   no shutdown
   encapsulation vlan
      client dot1q 23
   vrf COGENT
   ip address 10.99.23.0/31
!
interface Ethernet6.24
   description Cogent <-> NTT
   no shutdown
   encapsulation vlan
      client dot1q 24
   vrf COGENT
   ip address 10.99.24.0/31
!
interface Ethernet6.25
   description Cogent <-> GTT
   no shutdown
   encapsulation vlan
      client dot1q 25
   vrf COGENT
   ip address 10.99.25.0/31
!
interface Ethernet6.34
   description Lumen <-> NTT
   no shutdown
   encapsulation vlan
      client dot1q 34
   vrf LUMEN
   ip address 10.99.34.0/31
!
interface Ethernet6.35
   description Lumen <-> GTT
   no shutdown
   encapsulation vlan
      client dot1q 35
   vrf LUMEN
   ip address 10.99.35.0/31
!
interface Ethernet6.45
   description NTT <-> GTT
   no shutdown
   encapsulation vlan
      client dot1q 45
   vrf NTT
   ip address 10.99.45.0/31
!
interface Ethernet7
   no shutdown
   no switchport
!
interface Ethernet7.12
   description Cogent <-> Arelion
   no shutdown
   encapsulation vlan
      client dot1q 12
   vrf COGENT
   ip address 10.99.12.1/31
!
interface Ethernet7.13
   description Lumen <-> Arelion
   no shutdown
   encapsulation vlan
      client dot1q 13
   vrf LUMEN
   ip address 10.99.13.1/31
!
interface Ethernet7.14
   description NTT <-> Arelion
   no shutdown
   encapsulation vlan
      client dot1q 14
   vrf NTT
   ip address 10.99.14.1/31
!
interface Ethernet7.15
   description GTT <-> Arelion
   no shutdown
   encapsulation vlan
      client dot1q 15
   vrf GTT
   ip address 10.99.15.1/31
!
interface Ethernet7.23
   description Lumen <-> Cogent
   no shutdown
   encapsulation vlan
      client dot1q 23
   vrf LUMEN
   ip address 10.99.23.1/31
!
interface Ethernet7.24
   description NTT <-> Cogent
   no shutdown
   encapsulation vlan
      client dot1q 24
   vrf NTT
   ip address 10.99.24.1/31
!
interface Ethernet7.25
   description GTT <-> Cogent
   no shutdown
   encapsulation vlan
      client dot1q 25
   vrf GTT
   ip address 10.99.25.1/31
!
interface Ethernet7.34
   description NTT <-> Lumen
   no shutdown
   encapsulation vlan
      client dot1q 34
   vrf NTT
   ip address 10.99.34.1/31
!
interface Ethernet7.35
   description GTT <-> Lumen
   no shutdown
   encapsulation vlan
      client dot1q 35
   vrf GTT
   ip address 10.99.35.1/31
!
interface Ethernet7.45
   description GTT <-> NTT
   no shutdown
   encapsulation vlan
      client dot1q 45
   vrf GTT
   ip address 10.99.45.1/31
```

## Routing

### Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |
| ARELION | True |
| COGENT | True |
| GTT | True |
| LUMEN | True |
| NTT | True |
| OOB | False |

#### IP Routing Device Configuration

```eos
!
ip routing
ip routing vrf ARELION
ip routing vrf COGENT
ip routing vrf GTT
ip routing vrf LUMEN
ip routing vrf NTT
no ip routing vrf OOB
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| ARELION | False |
| COGENT | False |
| GTT | False |
| LUMEN | False |
| NTT | False |
| OOB | False |

### Static Routes

#### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP | Exit interface | Administrative Distance | Tag | Route Name | Metric |
| --- | ------------------ | ----------- | -------------- | ----------------------- | --- | ---------- | ------ |
| ARELION | 3.0.0.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 3.2.0.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 8.8.4.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 8.8.8.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 12.0.0.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 12.1.0.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 12.2.0.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 15.197.0.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 15.197.1.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 23.32.0.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 23.33.0.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 23.34.0.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 23.35.0.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 23.246.0.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 23.246.1.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 24.0.0.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 24.1.0.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 32.0.0.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 32.1.0.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 32.2.0.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 45.57.0.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 45.57.1.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 52.94.0.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 52.95.0.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 54.239.0.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 54.239.1.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 73.0.0.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 73.1.0.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 75.64.0.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 75.65.0.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 104.64.0.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 104.65.0.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 142.250.0.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 142.250.1.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 172.217.0.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 172.217.1.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 198.38.96.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 198.38.97.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 216.58.192.0/24 | - | null0 | 1 | - | - | - |
| ARELION | 216.58.193.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 1.0.0.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 1.1.1.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 13.64.0.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 13.65.0.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 20.33.0.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 20.34.0.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 24.16.0.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 24.17.0.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 40.64.0.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 40.65.0.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 40.74.0.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 40.75.0.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 71.74.0.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 71.75.0.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 97.80.0.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 97.81.0.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 104.16.0.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 104.17.0.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 104.18.0.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 104.19.0.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 104.131.0.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 104.131.1.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 129.146.0.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 129.146.1.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 132.226.0.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 132.226.1.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 140.82.112.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 140.82.113.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 151.101.0.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 151.101.1.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 151.101.2.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 159.65.0.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 159.65.1.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 172.64.0.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 172.65.0.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 192.30.252.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 192.30.253.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 199.232.0.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 199.232.1.0/24 | - | null0 | 1 | - | - | - |
| COGENT | 199.232.2.0/24 | - | null0 | 1 | - | - | - |
| GTT | 46.5.0.0/24 | - | null0 | 1 | - | - | - |
| GTT | 46.6.0.0/24 | - | null0 | 1 | - | - | - |
| GTT | 46.7.0.0/24 | - | null0 | 1 | - | - | - |
| GTT | 51.68.0.0/24 | - | null0 | 1 | - | - | - |
| GTT | 51.68.1.0/24 | - | null0 | 1 | - | - | - |
| GTT | 51.75.0.0/24 | - | null0 | 1 | - | - | - |
| GTT | 51.75.1.0/24 | - | null0 | 1 | - | - | - |
| GTT | 51.158.0.0/24 | - | null0 | 1 | - | - | - |
| GTT | 51.158.1.0/24 | - | null0 | 1 | - | - | - |
| GTT | 62.6.0.0/24 | - | null0 | 1 | - | - | - |
| GTT | 62.7.0.0/24 | - | null0 | 1 | - | - | - |
| GTT | 62.8.0.0/24 | - | null0 | 1 | - | - | - |
| GTT | 65.21.0.0/24 | - | null0 | 1 | - | - | - |
| GTT | 65.21.1.0/24 | - | null0 | 1 | - | - | - |
| GTT | 80.10.0.0/24 | - | null0 | 1 | - | - | - |
| GTT | 80.11.0.0/24 | - | null0 | 1 | - | - | - |
| GTT | 80.12.0.0/24 | - | null0 | 1 | - | - | - |
| GTT | 80.58.0.0/24 | - | null0 | 1 | - | - | - |
| GTT | 80.59.0.0/24 | - | null0 | 1 | - | - | - |
| GTT | 80.128.0.0/24 | - | null0 | 1 | - | - | - |
| GTT | 80.129.0.0/24 | - | null0 | 1 | - | - | - |
| GTT | 80.130.0.0/24 | - | null0 | 1 | - | - | - |
| GTT | 83.137.0.0/24 | - | null0 | 1 | - | - | - |
| GTT | 83.138.0.0/24 | - | null0 | 1 | - | - | - |
| GTT | 83.139.0.0/24 | - | null0 | 1 | - | - | - |
| GTT | 86.128.0.0/24 | - | null0 | 1 | - | - | - |
| GTT | 86.129.0.0/24 | - | null0 | 1 | - | - | - |
| GTT | 86.130.0.0/24 | - | null0 | 1 | - | - | - |
| GTT | 193.248.0.0/24 | - | null0 | 1 | - | - | - |
| GTT | 193.249.0.0/24 | - | null0 | 1 | - | - | - |
| GTT | 193.250.0.0/24 | - | null0 | 1 | - | - | - |
| GTT | 195.186.0.0/24 | - | null0 | 1 | - | - | - |
| GTT | 195.186.1.0/24 | - | null0 | 1 | - | - | - |
| GTT | 195.186.2.0/24 | - | null0 | 1 | - | - | - |
| GTT | 195.186.3.0/24 | - | null0 | 1 | - | - | - |
| GTT | 212.183.0.0/24 | - | null0 | 1 | - | - | - |
| GTT | 212.184.0.0/24 | - | null0 | 1 | - | - | - |
| GTT | 212.185.0.0/24 | - | null0 | 1 | - | - | - |
| GTT | 213.4.0.0/24 | - | null0 | 1 | - | - | - |
| GTT | 213.5.0.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 13.108.0.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 13.108.1.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 13.110.0.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 13.110.1.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 17.248.0.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 17.248.1.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 17.249.0.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 17.249.1.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 17.250.0.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 17.250.1.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 17.251.0.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 17.252.0.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 31.13.24.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 31.13.25.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 45.33.0.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 45.33.1.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 71.160.0.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 71.161.0.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 98.0.0.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 98.1.0.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 99.181.64.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 99.181.65.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 108.0.0.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 108.1.0.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 139.162.0.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 139.162.1.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 157.240.0.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 157.240.1.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 157.240.2.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 157.240.3.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 172.32.0.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 172.33.0.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 172.34.0.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 172.35.0.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 185.60.216.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 185.60.217.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 185.166.140.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 185.166.141.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 208.54.0.0/24 | - | null0 | 1 | - | - | - |
| LUMEN | 208.54.1.0/24 | - | null0 | 1 | - | - | - |
| NTT | 27.80.0.0/24 | - | null0 | 1 | - | - | - |
| NTT | 27.81.0.0/24 | - | null0 | 1 | - | - | - |
| NTT | 27.82.0.0/24 | - | null0 | 1 | - | - | - |
| NTT | 27.83.0.0/24 | - | null0 | 1 | - | - | - |
| NTT | 35.186.224.0/24 | - | null0 | 1 | - | - | - |
| NTT | 35.186.225.0/24 | - | null0 | 1 | - | - | - |
| NTT | 47.74.0.0/24 | - | null0 | 1 | - | - | - |
| NTT | 47.75.0.0/24 | - | null0 | 1 | - | - | - |
| NTT | 47.88.0.0/24 | - | null0 | 1 | - | - | - |
| NTT | 47.89.0.0/24 | - | null0 | 1 | - | - | - |
| NTT | 47.90.0.0/24 | - | null0 | 1 | - | - | - |
| NTT | 47.91.0.0/24 | - | null0 | 1 | - | - | - |
| NTT | 104.244.42.0/24 | - | null0 | 1 | - | - | - |
| NTT | 104.244.43.0/24 | - | null0 | 1 | - | - | - |
| NTT | 104.244.44.0/24 | - | null0 | 1 | - | - | - |
| NTT | 108.174.0.0/24 | - | null0 | 1 | - | - | - |
| NTT | 108.174.1.0/24 | - | null0 | 1 | - | - | - |
| NTT | 126.0.0.0/24 | - | null0 | 1 | - | - | - |
| NTT | 126.1.0.0/24 | - | null0 | 1 | - | - | - |
| NTT | 126.2.0.0/24 | - | null0 | 1 | - | - | - |
| NTT | 126.3.0.0/24 | - | null0 | 1 | - | - | - |
| NTT | 144.2.0.0/24 | - | null0 | 1 | - | - | - |
| NTT | 144.2.1.0/24 | - | null0 | 1 | - | - | - |
| NTT | 162.14.0.0/24 | - | null0 | 1 | - | - | - |
| NTT | 162.14.1.0/24 | - | null0 | 1 | - | - | - |
| NTT | 162.62.0.0/24 | - | null0 | 1 | - | - | - |
| NTT | 162.62.1.0/24 | - | null0 | 1 | - | - | - |
| NTT | 162.254.192.0/24 | - | null0 | 1 | - | - | - |
| NTT | 162.254.193.0/24 | - | null0 | 1 | - | - | - |
| NTT | 170.114.0.0/24 | - | null0 | 1 | - | - | - |
| NTT | 170.114.1.0/24 | - | null0 | 1 | - | - | - |
| NTT | 170.114.2.0/24 | - | null0 | 1 | - | - | - |
| NTT | 170.114.3.0/24 | - | null0 | 1 | - | - | - |
| NTT | 199.16.156.0/24 | - | null0 | 1 | - | - | - |
| NTT | 199.16.157.0/24 | - | null0 | 1 | - | - | - |
| NTT | 199.59.148.0/24 | - | null0 | 1 | - | - | - |
| NTT | 210.145.0.0/24 | - | null0 | 1 | - | - | - |
| NTT | 210.145.1.0/24 | - | null0 | 1 | - | - | - |
| NTT | 210.146.0.0/24 | - | null0 | 1 | - | - | - |
| NTT | 210.146.1.0/24 | - | null0 | 1 | - | - | - |
| OOB | 0.0.0.0/0 | 192.168.128.254 | - | 1 | - | - | - |

#### Static Routes Device Configuration

```eos
!
ip route vrf ARELION 3.0.0.0/24 Null0
ip route vrf ARELION 3.2.0.0/24 Null0
ip route vrf ARELION 8.8.4.0/24 Null0
ip route vrf ARELION 8.8.8.0/24 Null0
ip route vrf ARELION 12.0.0.0/24 Null0
ip route vrf ARELION 12.1.0.0/24 Null0
ip route vrf ARELION 12.2.0.0/24 Null0
ip route vrf ARELION 15.197.0.0/24 Null0
ip route vrf ARELION 15.197.1.0/24 Null0
ip route vrf ARELION 23.32.0.0/24 Null0
ip route vrf ARELION 23.33.0.0/24 Null0
ip route vrf ARELION 23.34.0.0/24 Null0
ip route vrf ARELION 23.35.0.0/24 Null0
ip route vrf ARELION 23.246.0.0/24 Null0
ip route vrf ARELION 23.246.1.0/24 Null0
ip route vrf ARELION 24.0.0.0/24 Null0
ip route vrf ARELION 24.1.0.0/24 Null0
ip route vrf ARELION 32.0.0.0/24 Null0
ip route vrf ARELION 32.1.0.0/24 Null0
ip route vrf ARELION 32.2.0.0/24 Null0
ip route vrf ARELION 45.57.0.0/24 Null0
ip route vrf ARELION 45.57.1.0/24 Null0
ip route vrf ARELION 52.94.0.0/24 Null0
ip route vrf ARELION 52.95.0.0/24 Null0
ip route vrf ARELION 54.239.0.0/24 Null0
ip route vrf ARELION 54.239.1.0/24 Null0
ip route vrf ARELION 73.0.0.0/24 Null0
ip route vrf ARELION 73.1.0.0/24 Null0
ip route vrf ARELION 75.64.0.0/24 Null0
ip route vrf ARELION 75.65.0.0/24 Null0
ip route vrf ARELION 104.64.0.0/24 Null0
ip route vrf ARELION 104.65.0.0/24 Null0
ip route vrf ARELION 142.250.0.0/24 Null0
ip route vrf ARELION 142.250.1.0/24 Null0
ip route vrf ARELION 172.217.0.0/24 Null0
ip route vrf ARELION 172.217.1.0/24 Null0
ip route vrf ARELION 198.38.96.0/24 Null0
ip route vrf ARELION 198.38.97.0/24 Null0
ip route vrf ARELION 216.58.192.0/24 Null0
ip route vrf ARELION 216.58.193.0/24 Null0
ip route vrf COGENT 1.0.0.0/24 Null0
ip route vrf COGENT 1.1.1.0/24 Null0
ip route vrf COGENT 13.64.0.0/24 Null0
ip route vrf COGENT 13.65.0.0/24 Null0
ip route vrf COGENT 20.33.0.0/24 Null0
ip route vrf COGENT 20.34.0.0/24 Null0
ip route vrf COGENT 24.16.0.0/24 Null0
ip route vrf COGENT 24.17.0.0/24 Null0
ip route vrf COGENT 40.64.0.0/24 Null0
ip route vrf COGENT 40.65.0.0/24 Null0
ip route vrf COGENT 40.74.0.0/24 Null0
ip route vrf COGENT 40.75.0.0/24 Null0
ip route vrf COGENT 71.74.0.0/24 Null0
ip route vrf COGENT 71.75.0.0/24 Null0
ip route vrf COGENT 97.80.0.0/24 Null0
ip route vrf COGENT 97.81.0.0/24 Null0
ip route vrf COGENT 104.16.0.0/24 Null0
ip route vrf COGENT 104.17.0.0/24 Null0
ip route vrf COGENT 104.18.0.0/24 Null0
ip route vrf COGENT 104.19.0.0/24 Null0
ip route vrf COGENT 104.131.0.0/24 Null0
ip route vrf COGENT 104.131.1.0/24 Null0
ip route vrf COGENT 129.146.0.0/24 Null0
ip route vrf COGENT 129.146.1.0/24 Null0
ip route vrf COGENT 132.226.0.0/24 Null0
ip route vrf COGENT 132.226.1.0/24 Null0
ip route vrf COGENT 140.82.112.0/24 Null0
ip route vrf COGENT 140.82.113.0/24 Null0
ip route vrf COGENT 151.101.0.0/24 Null0
ip route vrf COGENT 151.101.1.0/24 Null0
ip route vrf COGENT 151.101.2.0/24 Null0
ip route vrf COGENT 159.65.0.0/24 Null0
ip route vrf COGENT 159.65.1.0/24 Null0
ip route vrf COGENT 172.64.0.0/24 Null0
ip route vrf COGENT 172.65.0.0/24 Null0
ip route vrf COGENT 192.30.252.0/24 Null0
ip route vrf COGENT 192.30.253.0/24 Null0
ip route vrf COGENT 199.232.0.0/24 Null0
ip route vrf COGENT 199.232.1.0/24 Null0
ip route vrf COGENT 199.232.2.0/24 Null0
ip route vrf GTT 46.5.0.0/24 Null0
ip route vrf GTT 46.6.0.0/24 Null0
ip route vrf GTT 46.7.0.0/24 Null0
ip route vrf GTT 51.68.0.0/24 Null0
ip route vrf GTT 51.68.1.0/24 Null0
ip route vrf GTT 51.75.0.0/24 Null0
ip route vrf GTT 51.75.1.0/24 Null0
ip route vrf GTT 51.158.0.0/24 Null0
ip route vrf GTT 51.158.1.0/24 Null0
ip route vrf GTT 62.6.0.0/24 Null0
ip route vrf GTT 62.7.0.0/24 Null0
ip route vrf GTT 62.8.0.0/24 Null0
ip route vrf GTT 65.21.0.0/24 Null0
ip route vrf GTT 65.21.1.0/24 Null0
ip route vrf GTT 80.10.0.0/24 Null0
ip route vrf GTT 80.11.0.0/24 Null0
ip route vrf GTT 80.12.0.0/24 Null0
ip route vrf GTT 80.58.0.0/24 Null0
ip route vrf GTT 80.59.0.0/24 Null0
ip route vrf GTT 80.128.0.0/24 Null0
ip route vrf GTT 80.129.0.0/24 Null0
ip route vrf GTT 80.130.0.0/24 Null0
ip route vrf GTT 83.137.0.0/24 Null0
ip route vrf GTT 83.138.0.0/24 Null0
ip route vrf GTT 83.139.0.0/24 Null0
ip route vrf GTT 86.128.0.0/24 Null0
ip route vrf GTT 86.129.0.0/24 Null0
ip route vrf GTT 86.130.0.0/24 Null0
ip route vrf GTT 193.248.0.0/24 Null0
ip route vrf GTT 193.249.0.0/24 Null0
ip route vrf GTT 193.250.0.0/24 Null0
ip route vrf GTT 195.186.0.0/24 Null0
ip route vrf GTT 195.186.1.0/24 Null0
ip route vrf GTT 195.186.2.0/24 Null0
ip route vrf GTT 195.186.3.0/24 Null0
ip route vrf GTT 212.183.0.0/24 Null0
ip route vrf GTT 212.184.0.0/24 Null0
ip route vrf GTT 212.185.0.0/24 Null0
ip route vrf GTT 213.4.0.0/24 Null0
ip route vrf GTT 213.5.0.0/24 Null0
ip route vrf LUMEN 13.108.0.0/24 Null0
ip route vrf LUMEN 13.108.1.0/24 Null0
ip route vrf LUMEN 13.110.0.0/24 Null0
ip route vrf LUMEN 13.110.1.0/24 Null0
ip route vrf LUMEN 17.248.0.0/24 Null0
ip route vrf LUMEN 17.248.1.0/24 Null0
ip route vrf LUMEN 17.249.0.0/24 Null0
ip route vrf LUMEN 17.249.1.0/24 Null0
ip route vrf LUMEN 17.250.0.0/24 Null0
ip route vrf LUMEN 17.250.1.0/24 Null0
ip route vrf LUMEN 17.251.0.0/24 Null0
ip route vrf LUMEN 17.252.0.0/24 Null0
ip route vrf LUMEN 31.13.24.0/24 Null0
ip route vrf LUMEN 31.13.25.0/24 Null0
ip route vrf LUMEN 45.33.0.0/24 Null0
ip route vrf LUMEN 45.33.1.0/24 Null0
ip route vrf LUMEN 71.160.0.0/24 Null0
ip route vrf LUMEN 71.161.0.0/24 Null0
ip route vrf LUMEN 98.0.0.0/24 Null0
ip route vrf LUMEN 98.1.0.0/24 Null0
ip route vrf LUMEN 99.181.64.0/24 Null0
ip route vrf LUMEN 99.181.65.0/24 Null0
ip route vrf LUMEN 108.0.0.0/24 Null0
ip route vrf LUMEN 108.1.0.0/24 Null0
ip route vrf LUMEN 139.162.0.0/24 Null0
ip route vrf LUMEN 139.162.1.0/24 Null0
ip route vrf LUMEN 157.240.0.0/24 Null0
ip route vrf LUMEN 157.240.1.0/24 Null0
ip route vrf LUMEN 157.240.2.0/24 Null0
ip route vrf LUMEN 157.240.3.0/24 Null0
ip route vrf LUMEN 172.32.0.0/24 Null0
ip route vrf LUMEN 172.33.0.0/24 Null0
ip route vrf LUMEN 172.34.0.0/24 Null0
ip route vrf LUMEN 172.35.0.0/24 Null0
ip route vrf LUMEN 185.60.216.0/24 Null0
ip route vrf LUMEN 185.60.217.0/24 Null0
ip route vrf LUMEN 185.166.140.0/24 Null0
ip route vrf LUMEN 185.166.141.0/24 Null0
ip route vrf LUMEN 208.54.0.0/24 Null0
ip route vrf LUMEN 208.54.1.0/24 Null0
ip route vrf NTT 27.80.0.0/24 Null0
ip route vrf NTT 27.81.0.0/24 Null0
ip route vrf NTT 27.82.0.0/24 Null0
ip route vrf NTT 27.83.0.0/24 Null0
ip route vrf NTT 35.186.224.0/24 Null0
ip route vrf NTT 35.186.225.0/24 Null0
ip route vrf NTT 47.74.0.0/24 Null0
ip route vrf NTT 47.75.0.0/24 Null0
ip route vrf NTT 47.88.0.0/24 Null0
ip route vrf NTT 47.89.0.0/24 Null0
ip route vrf NTT 47.90.0.0/24 Null0
ip route vrf NTT 47.91.0.0/24 Null0
ip route vrf NTT 104.244.42.0/24 Null0
ip route vrf NTT 104.244.43.0/24 Null0
ip route vrf NTT 104.244.44.0/24 Null0
ip route vrf NTT 108.174.0.0/24 Null0
ip route vrf NTT 108.174.1.0/24 Null0
ip route vrf NTT 126.0.0.0/24 Null0
ip route vrf NTT 126.1.0.0/24 Null0
ip route vrf NTT 126.2.0.0/24 Null0
ip route vrf NTT 126.3.0.0/24 Null0
ip route vrf NTT 144.2.0.0/24 Null0
ip route vrf NTT 144.2.1.0/24 Null0
ip route vrf NTT 162.14.0.0/24 Null0
ip route vrf NTT 162.14.1.0/24 Null0
ip route vrf NTT 162.62.0.0/24 Null0
ip route vrf NTT 162.62.1.0/24 Null0
ip route vrf NTT 162.254.192.0/24 Null0
ip route vrf NTT 162.254.193.0/24 Null0
ip route vrf NTT 170.114.0.0/24 Null0
ip route vrf NTT 170.114.1.0/24 Null0
ip route vrf NTT 170.114.2.0/24 Null0
ip route vrf NTT 170.114.3.0/24 Null0
ip route vrf NTT 199.16.156.0/24 Null0
ip route vrf NTT 199.16.157.0/24 Null0
ip route vrf NTT 199.59.148.0/24 Null0
ip route vrf NTT 210.145.0.0/24 Null0
ip route vrf NTT 210.145.1.0/24 Null0
ip route vrf NTT 210.146.0.0/24 Null0
ip route vrf NTT 210.146.1.0/24 Null0
ip route vrf OOB 0.0.0.0/0 192.168.128.254
```

### Router General

#### Router General Device Configuration

```eos
!
router general
   control-functions
      code unit TRANSIT_ROUTE_ORIGINS
         function SET_ORIGIN_ARELION() -> bool {
            if match(source.prefix, prefix_list_v4("PL_GOOGLE_15169")) {
               set(source.as_path, [15169]);
               return true;
            }
            elif match(source.prefix, prefix_list_v4("PL_AMAZON_16509")) {
               set(source.as_path, [16509]);
               return true;
            }
            elif match(source.prefix, prefix_list_v4("PL_NETFLIX_2906")) {
               set(source.as_path, [2906]);
               return true;
            }
            elif match(source.prefix, prefix_list_v4("PL_AKAMAI_20940")) {
               set(source.as_path, [20940]);
               return true;
            }
            elif match(source.prefix, prefix_list_v4("PL_ATT_7018")) {
               set(source.as_path, [7018]);
               return true;
            }
            elif match(source.prefix, prefix_list_v4("PL_COMCAST_7922")) {
               set(source.as_path, [7922]);
               return true;
            }
            return false;
         }

         function SET_ORIGIN_COGENT() -> bool {
            if match(source.prefix, prefix_list_v4("PL_CLOUDFLARE_13335")) {
               set(source.as_path, [13335]);
               return true;
            }
            elif match(source.prefix, prefix_list_v4("PL_MICROSOFT_8075")) {
               set(source.as_path, [8075]);
               return true;
            }
            elif match(source.prefix, prefix_list_v4("PL_GITHUB_36459")) {
               set(source.as_path, [36459]);
               return true;
            }
            elif match(source.prefix, prefix_list_v4("PL_DIGITALOCEAN_14061")) {
               set(source.as_path, [14061]);
               return true;
            }
            elif match(source.prefix, prefix_list_v4("PL_FASTLY_54113")) {
               set(source.as_path, [54113]);
               return true;
            }
            elif match(source.prefix, prefix_list_v4("PL_CHARTER_20115")) {
               set(source.as_path, [20115]);
               return true;
            }
            elif match(source.prefix, prefix_list_v4("PL_ORACLE_31898")) {
               set(source.as_path, [31898]);
               return true;
            }
            return false;
         }

         function SET_ORIGIN_LUMEN() -> bool {
            if match(source.prefix, prefix_list_v4("PL_META_32934")) {
               set(source.as_path, [32934]);
               return true;
            }
            elif match(source.prefix, prefix_list_v4("PL_APPLE_714")) {
               set(source.as_path, [714]);
               return true;
            }
            elif match(source.prefix, prefix_list_v4("PL_VERIZON_701")) {
               set(source.as_path, [701]);
               return true;
            }
            elif match(source.prefix, prefix_list_v4("PL_TMOBILE_21928")) {
               set(source.as_path, [21928]);
               return true;
            }
            elif match(source.prefix, prefix_list_v4("PL_LINODE_63949")) {
               set(source.as_path, [63949]);
               return true;
            }
            elif match(source.prefix, prefix_list_v4("PL_SALESFORCE_14340")) {
               set(source.as_path, [14340]);
               return true;
            }
            elif match(source.prefix, prefix_list_v4("PL_TWITCH_46489")) {
               set(source.as_path, [46489]);
               return true;
            }
            return false;
         }

         function SET_ORIGIN_NTT() -> bool {
            if match(source.prefix, prefix_list_v4("PL_TWITTER_13414")) {
               set(source.as_path, [13414]);
               return true;
            }
            elif match(source.prefix, prefix_list_v4("PL_ZOOM_52347")) {
               set(source.as_path, [52347]);
               return true;
            }
            elif match(source.prefix, prefix_list_v4("PL_ALIBABA_45102")) {
               set(source.as_path, [45102]);
               return true;
            }
            elif match(source.prefix, prefix_list_v4("PL_TENCENT_132203")) {
               set(source.as_path, [132203]);
               return true;
            }
            elif match(source.prefix, prefix_list_v4("PL_SOFTBANK_17676")) {
               set(source.as_path, [17676]);
               return true;
            }
            elif match(source.prefix, prefix_list_v4("PL_KDDI_2516")) {
               set(source.as_path, [2516]);
               return true;
            }
            elif match(source.prefix, prefix_list_v4("PL_NTTCOM_4713")) {
               set(source.as_path, [4713]);
               return true;
            }
            elif match(source.prefix, prefix_list_v4("PL_LINKEDIN_14413")) {
               set(source.as_path, [14413]);
               return true;
            }
            elif match(source.prefix, prefix_list_v4("PL_SPOTIFY_8403")) {
               set(source.as_path, [8403]);
               return true;
            }
            elif match(source.prefix, prefix_list_v4("PL_VALVE_32590")) {
               set(source.as_path, [32590]);
               return true;
            }
            return false;
         }

         function SET_ORIGIN_GTT() -> bool {
            if match(source.prefix, prefix_list_v4("PL_DTAG_3320")) {
               set(source.as_path, [3320]);
               return true;
            }
            elif match(source.prefix, prefix_list_v4("PL_BT_2856")) {
               set(source.as_path, [2856]);
               return true;
            }
            elif match(source.prefix, prefix_list_v4("PL_ORANGE_5511")) {
               set(source.as_path, [5511]);
               return true;
            }
            elif match(source.prefix, prefix_list_v4("PL_VODAFONE_3209")) {
               set(source.as_path, [3209]);
               return true;
            }
            elif match(source.prefix, prefix_list_v4("PL_TELEFONICA_12956")) {
               set(source.as_path, [12956]);
               return true;
            }
            elif match(source.prefix, prefix_list_v4("PL_SWISSCOM_3303")) {
               set(source.as_path, [3303]);
               return true;
            }
            elif match(source.prefix, prefix_list_v4("PL_OVH_16276")) {
               set(source.as_path, [16276]);
               return true;
            }
            elif match(source.prefix, prefix_list_v4("PL_HETZNER_24940")) {
               set(source.as_path, [24940]);
               return true;
            }
            elif match(source.prefix, prefix_list_v4("PL_SCALEWAY_12876")) {
               set(source.as_path, [12876]);
               return true;
            }
            return false;
         }
         EOF
   !
   exit
   exit
```

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65000 | 100.64.255.0 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Maximum-accepted-routes | Maximum-advertised-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ----------------------- | ------------------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 198.51.100.1 | 394437 | ARELION | False | - | - | - | - | - | - | - | - | - | - |
| 2601::1 | 394437 | ARELION | False | - | - | - | - | - | - | - | - | - | - |
| 10.99.12.1 | 174 | ARELION | False | - | - | - | - | - | - | - | - | - | - |
| 10.99.13.1 | 3356 | ARELION | False | - | - | - | - | - | - | - | - | - | - |
| 10.99.14.1 | 2914 | ARELION | False | - | - | - | - | - | - | - | - | - | - |
| 10.99.15.1 | 3257 | ARELION | False | - | - | - | - | - | - | - | - | - | - |
| 198.51.100.3 | 394437 | COGENT | False | - | - | - | - | - | - | - | - | - | - |
| 2602::1 | 394437 | COGENT | False | - | - | - | - | - | - | - | - | - | - |
| 10.99.12.0 | 1299 | COGENT | False | - | - | - | - | - | - | - | - | - | - |
| 10.99.23.1 | 3356 | COGENT | False | - | - | - | - | - | - | - | - | - | - |
| 10.99.24.1 | 2914 | COGENT | False | - | - | - | - | - | - | - | - | - | - |
| 10.99.25.1 | 3257 | COGENT | False | - | - | - | - | - | - | - | - | - | - |
| 198.51.100.9 | 394437 | GTT | False | - | - | - | - | - | - | - | - | - | - |
| 2605::1 | 394437 | GTT | False | - | - | - | - | - | - | - | - | - | - |
| 10.99.15.0 | 1299 | GTT | False | - | - | - | - | - | - | - | - | - | - |
| 10.99.25.0 | 174 | GTT | False | - | - | - | - | - | - | - | - | - | - |
| 10.99.35.0 | 3356 | GTT | False | - | - | - | - | - | - | - | - | - | - |
| 10.99.45.0 | 2914 | GTT | False | - | - | - | - | - | - | - | - | - | - |
| 198.51.100.5 | 394437 | LUMEN | False | - | - | - | - | - | - | - | - | - | - |
| 2603::1 | 394437 | LUMEN | False | - | - | - | - | - | - | - | - | - | - |
| 10.99.13.0 | 1299 | LUMEN | False | - | - | - | - | - | - | - | - | - | - |
| 10.99.23.0 | 174 | LUMEN | False | - | - | - | - | - | - | - | - | - | - |
| 10.99.34.1 | 2914 | LUMEN | False | - | - | - | - | - | - | - | - | - | - |
| 10.99.35.1 | 3257 | LUMEN | False | - | - | - | - | - | - | - | - | - | - |
| 198.51.100.7 | 394437 | NTT | False | - | - | - | - | - | - | - | - | - | - |
| 2604::1 | 394437 | NTT | False | - | - | - | - | - | - | - | - | - | - |
| 10.99.14.0 | 1299 | NTT | False | - | - | - | - | - | - | - | - | - | - |
| 10.99.24.0 | 174 | NTT | False | - | - | - | - | - | - | - | - | - | - |
| 10.99.34.0 | 3356 | NTT | False | - | - | - | - | - | - | - | - | - | - |
| 10.99.45.1 | 3257 | NTT | False | - | - | - | - | - | - | - | - | - | - |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute | Graceful Restart |
| --- | ------------------- | ------------ | ---------------- |
| ARELION | - | connected<br>static | - |
| COGENT | - | connected<br>static | - |
| GTT | - | connected<br>static | - |
| LUMEN | - | connected<br>static | - |
| NTT | - | connected<br>static | - |

#### Router BGP Device Configuration

```eos
!
router bgp 65000
   router-id 100.64.255.0
   !
   vrf ARELION
      router-id 100.64.255.1
      neighbor 10.99.12.1 remote-as 174
      neighbor 10.99.12.1 local-as 1299 no-prepend replace-as
      neighbor 10.99.12.1 description COGENT (AS174)
      neighbor 10.99.13.1 remote-as 3356
      neighbor 10.99.13.1 local-as 1299 no-prepend replace-as
      neighbor 10.99.13.1 description LUMEN (AS3356)
      neighbor 10.99.14.1 remote-as 2914
      neighbor 10.99.14.1 local-as 1299 no-prepend replace-as
      neighbor 10.99.14.1 description NTT (AS2914)
      neighbor 10.99.15.1 remote-as 3257
      neighbor 10.99.15.1 local-as 1299 no-prepend replace-as
      neighbor 10.99.15.1 description GTT (AS3257)
      neighbor 198.51.100.1 remote-as 394437
      neighbor 198.51.100.1 local-as 1299 no-prepend replace-as
      neighbor 198.51.100.1 description CYWE-A (AS394437)
      neighbor 2601::1 remote-as 394437
      neighbor 2601::1 local-as 1299 no-prepend replace-as
      neighbor 2601::1 description CYWE-A (AS394437) IPv6
      redistribute connected
      redistribute static rcf SET_ORIGIN_ARELION()
      !
      address-family ipv4
         neighbor 10.99.12.1 activate
         neighbor 10.99.13.1 activate
         neighbor 10.99.14.1 activate
         neighbor 10.99.15.1 activate
         neighbor 198.51.100.1 activate
      !
      address-family ipv6
         neighbor 2601::1 activate
   !
   vrf COGENT
      router-id 100.64.255.2
      neighbor 10.99.12.0 remote-as 1299
      neighbor 10.99.12.0 local-as 174 no-prepend replace-as
      neighbor 10.99.12.0 description ARELION (AS1299)
      neighbor 10.99.23.1 remote-as 3356
      neighbor 10.99.23.1 local-as 174 no-prepend replace-as
      neighbor 10.99.23.1 description LUMEN (AS3356)
      neighbor 10.99.24.1 remote-as 2914
      neighbor 10.99.24.1 local-as 174 no-prepend replace-as
      neighbor 10.99.24.1 description NTT (AS2914)
      neighbor 10.99.25.1 remote-as 3257
      neighbor 10.99.25.1 local-as 174 no-prepend replace-as
      neighbor 10.99.25.1 description GTT (AS3257)
      neighbor 198.51.100.3 remote-as 394437
      neighbor 198.51.100.3 local-as 174 no-prepend replace-as
      neighbor 198.51.100.3 description CYWE-B (AS394437)
      neighbor 2602::1 remote-as 394437
      neighbor 2602::1 local-as 174 no-prepend replace-as
      neighbor 2602::1 description CYWE-B (AS394437) IPv6
      redistribute connected
      redistribute static rcf SET_ORIGIN_COGENT()
      !
      address-family ipv4
         neighbor 10.99.12.0 activate
         neighbor 10.99.23.1 activate
         neighbor 10.99.24.1 activate
         neighbor 10.99.25.1 activate
         neighbor 198.51.100.3 activate
      !
      address-family ipv6
         neighbor 2602::1 activate
   !
   vrf GTT
      router-id 100.64.255.5
      neighbor 10.99.15.0 remote-as 1299
      neighbor 10.99.15.0 local-as 3257 no-prepend replace-as
      neighbor 10.99.15.0 description ARELION (AS1299)
      neighbor 10.99.25.0 remote-as 174
      neighbor 10.99.25.0 local-as 3257 no-prepend replace-as
      neighbor 10.99.25.0 description COGENT (AS174)
      neighbor 10.99.35.0 remote-as 3356
      neighbor 10.99.35.0 local-as 3257 no-prepend replace-as
      neighbor 10.99.35.0 description LUMEN (AS3356)
      neighbor 10.99.45.0 remote-as 2914
      neighbor 10.99.45.0 local-as 3257 no-prepend replace-as
      neighbor 10.99.45.0 description NTT (AS2914)
      neighbor 198.51.100.9 remote-as 394437
      neighbor 198.51.100.9 local-as 3257 no-prepend replace-as
      neighbor 198.51.100.9 description CYGA-A (AS394437)
      neighbor 2605::1 remote-as 394437
      neighbor 2605::1 local-as 3257 no-prepend replace-as
      neighbor 2605::1 description CYGA-A (AS394437) IPv6
      redistribute connected
      redistribute static rcf SET_ORIGIN_GTT()
      !
      address-family ipv4
         neighbor 10.99.15.0 activate
         neighbor 10.99.25.0 activate
         neighbor 10.99.35.0 activate
         neighbor 10.99.45.0 activate
         neighbor 198.51.100.9 activate
      !
      address-family ipv6
         neighbor 2605::1 activate
   !
   vrf LUMEN
      router-id 100.64.255.3
      neighbor 10.99.13.0 remote-as 1299
      neighbor 10.99.13.0 local-as 3356 no-prepend replace-as
      neighbor 10.99.13.0 description ARELION (AS1299)
      neighbor 10.99.23.0 remote-as 174
      neighbor 10.99.23.0 local-as 3356 no-prepend replace-as
      neighbor 10.99.23.0 description COGENT (AS174)
      neighbor 10.99.34.1 remote-as 2914
      neighbor 10.99.34.1 local-as 3356 no-prepend replace-as
      neighbor 10.99.34.1 description NTT (AS2914)
      neighbor 10.99.35.1 remote-as 3257
      neighbor 10.99.35.1 local-as 3356 no-prepend replace-as
      neighbor 10.99.35.1 description GTT (AS3257)
      neighbor 198.51.100.5 remote-as 394437
      neighbor 198.51.100.5 local-as 3356 no-prepend replace-as
      neighbor 198.51.100.5 description FIBT-B (AS394437)
      neighbor 2603::1 remote-as 394437
      neighbor 2603::1 local-as 3356 no-prepend replace-as
      neighbor 2603::1 description FIBT-B (AS394437) IPv6
      redistribute connected
      redistribute static rcf SET_ORIGIN_LUMEN()
      !
      address-family ipv4
         neighbor 10.99.13.0 activate
         neighbor 10.99.23.0 activate
         neighbor 10.99.34.1 activate
         neighbor 10.99.35.1 activate
         neighbor 198.51.100.5 activate
      !
      address-family ipv6
         neighbor 2603::1 activate
   !
   vrf NTT
      router-id 100.64.255.4
      neighbor 10.99.14.0 remote-as 1299
      neighbor 10.99.14.0 local-as 2914 no-prepend replace-as
      neighbor 10.99.14.0 description ARELION (AS1299)
      neighbor 10.99.24.0 remote-as 174
      neighbor 10.99.24.0 local-as 2914 no-prepend replace-as
      neighbor 10.99.24.0 description COGENT (AS174)
      neighbor 10.99.34.0 remote-as 3356
      neighbor 10.99.34.0 local-as 2914 no-prepend replace-as
      neighbor 10.99.34.0 description LUMEN (AS3356)
      neighbor 10.99.45.1 remote-as 3257
      neighbor 10.99.45.1 local-as 2914 no-prepend replace-as
      neighbor 10.99.45.1 description GTT (AS3257)
      neighbor 198.51.100.7 remote-as 394437
      neighbor 198.51.100.7 local-as 2914 no-prepend replace-as
      neighbor 198.51.100.7 description TSHL-A (AS394437)
      neighbor 2604::1 remote-as 394437
      neighbor 2604::1 local-as 2914 no-prepend replace-as
      neighbor 2604::1 description TSHL-A (AS394437) IPv6
      redistribute connected
      redistribute static rcf SET_ORIGIN_NTT()
      !
      address-family ipv4
         neighbor 10.99.14.0 activate
         neighbor 10.99.24.0 activate
         neighbor 10.99.34.0 activate
         neighbor 10.99.45.1 activate
         neighbor 198.51.100.7 activate
      !
      address-family ipv6
         neighbor 2604::1 activate
```

## Filters

### Prefix-lists

#### Prefix-lists Summary

##### PL_AKAMAI_20940

| Sequence | Action |
| -------- | ------ |
| 10 | permit 23.32.0.0/24 |
| 20 | permit 23.33.0.0/24 |
| 30 | permit 23.34.0.0/24 |
| 40 | permit 23.35.0.0/24 |
| 50 | permit 104.64.0.0/24 |
| 60 | permit 104.65.0.0/24 |

##### PL_ALIBABA_45102

| Sequence | Action |
| -------- | ------ |
| 10 | permit 47.74.0.0/24 |
| 20 | permit 47.75.0.0/24 |
| 30 | permit 47.88.0.0/24 |
| 40 | permit 47.89.0.0/24 |
| 50 | permit 47.90.0.0/24 |
| 60 | permit 47.91.0.0/24 |

##### PL_AMAZON_16509

| Sequence | Action |
| -------- | ------ |
| 10 | permit 3.0.0.0/24 |
| 20 | permit 3.2.0.0/24 |
| 30 | permit 15.197.0.0/24 |
| 40 | permit 15.197.1.0/24 |
| 50 | permit 52.94.0.0/24 |
| 60 | permit 52.95.0.0/24 |
| 70 | permit 54.239.0.0/24 |
| 80 | permit 54.239.1.0/24 |

##### PL_APPLE_714

| Sequence | Action |
| -------- | ------ |
| 10 | permit 17.248.0.0/24 |
| 20 | permit 17.248.1.0/24 |
| 30 | permit 17.249.0.0/24 |
| 40 | permit 17.249.1.0/24 |
| 50 | permit 17.250.0.0/24 |
| 60 | permit 17.250.1.0/24 |
| 70 | permit 17.251.0.0/24 |
| 80 | permit 17.252.0.0/24 |

##### PL_ATT_7018

| Sequence | Action |
| -------- | ------ |
| 10 | permit 12.0.0.0/24 |
| 20 | permit 12.1.0.0/24 |
| 30 | permit 12.2.0.0/24 |
| 40 | permit 32.0.0.0/24 |
| 50 | permit 32.1.0.0/24 |
| 60 | permit 32.2.0.0/24 |

##### PL_BT_2856

| Sequence | Action |
| -------- | ------ |
| 10 | permit 62.6.0.0/24 |
| 20 | permit 62.7.0.0/24 |
| 30 | permit 62.8.0.0/24 |
| 40 | permit 86.128.0.0/24 |
| 50 | permit 86.129.0.0/24 |
| 60 | permit 86.130.0.0/24 |

##### PL_CHARTER_20115

| Sequence | Action |
| -------- | ------ |
| 10 | permit 24.16.0.0/24 |
| 20 | permit 24.17.0.0/24 |
| 30 | permit 97.80.0.0/24 |
| 40 | permit 97.81.0.0/24 |
| 50 | permit 71.74.0.0/24 |
| 60 | permit 71.75.0.0/24 |

##### PL_CLOUDFLARE_13335

| Sequence | Action |
| -------- | ------ |
| 10 | permit 1.1.1.0/24 |
| 20 | permit 1.0.0.0/24 |
| 30 | permit 104.16.0.0/24 |
| 40 | permit 104.17.0.0/24 |
| 50 | permit 104.18.0.0/24 |
| 60 | permit 104.19.0.0/24 |
| 70 | permit 172.64.0.0/24 |
| 80 | permit 172.65.0.0/24 |

##### PL_COMCAST_7922

| Sequence | Action |
| -------- | ------ |
| 10 | permit 24.0.0.0/24 |
| 20 | permit 24.1.0.0/24 |
| 30 | permit 73.0.0.0/24 |
| 40 | permit 73.1.0.0/24 |
| 50 | permit 75.64.0.0/24 |
| 60 | permit 75.65.0.0/24 |

##### PL_DIGITALOCEAN_14061

| Sequence | Action |
| -------- | ------ |
| 10 | permit 104.131.0.0/24 |
| 20 | permit 104.131.1.0/24 |
| 30 | permit 159.65.0.0/24 |
| 40 | permit 159.65.1.0/24 |

##### PL_DTAG_3320

| Sequence | Action |
| -------- | ------ |
| 10 | permit 46.5.0.0/24 |
| 20 | permit 46.6.0.0/24 |
| 30 | permit 46.7.0.0/24 |
| 40 | permit 80.128.0.0/24 |
| 50 | permit 80.129.0.0/24 |
| 60 | permit 80.130.0.0/24 |

##### PL_FASTLY_54113

| Sequence | Action |
| -------- | ------ |
| 10 | permit 151.101.0.0/24 |
| 20 | permit 151.101.1.0/24 |
| 30 | permit 151.101.2.0/24 |
| 40 | permit 199.232.0.0/24 |
| 50 | permit 199.232.1.0/24 |
| 60 | permit 199.232.2.0/24 |

##### PL_GITHUB_36459

| Sequence | Action |
| -------- | ------ |
| 10 | permit 140.82.112.0/24 |
| 20 | permit 140.82.113.0/24 |
| 30 | permit 192.30.252.0/24 |
| 40 | permit 192.30.253.0/24 |

##### PL_GOOGLE_15169

| Sequence | Action |
| -------- | ------ |
| 10 | permit 8.8.8.0/24 |
| 20 | permit 8.8.4.0/24 |
| 30 | permit 142.250.0.0/24 |
| 40 | permit 142.250.1.0/24 |
| 50 | permit 172.217.0.0/24 |
| 60 | permit 172.217.1.0/24 |
| 70 | permit 216.58.192.0/24 |
| 80 | permit 216.58.193.0/24 |

##### PL_HETZNER_24940

| Sequence | Action |
| -------- | ------ |
| 10 | permit 65.21.0.0/24 |
| 20 | permit 65.21.1.0/24 |

##### PL_KDDI_2516

| Sequence | Action |
| -------- | ------ |
| 10 | permit 27.80.0.0/24 |
| 20 | permit 27.81.0.0/24 |
| 30 | permit 27.82.0.0/24 |
| 40 | permit 27.83.0.0/24 |

##### PL_LINKEDIN_14413

| Sequence | Action |
| -------- | ------ |
| 10 | permit 108.174.0.0/24 |
| 20 | permit 108.174.1.0/24 |
| 30 | permit 144.2.0.0/24 |
| 40 | permit 144.2.1.0/24 |

##### PL_LINODE_63949

| Sequence | Action |
| -------- | ------ |
| 10 | permit 45.33.0.0/24 |
| 20 | permit 45.33.1.0/24 |
| 30 | permit 139.162.0.0/24 |
| 40 | permit 139.162.1.0/24 |

##### PL_META_32934

| Sequence | Action |
| -------- | ------ |
| 10 | permit 31.13.24.0/24 |
| 20 | permit 31.13.25.0/24 |
| 30 | permit 157.240.0.0/24 |
| 40 | permit 157.240.1.0/24 |
| 50 | permit 157.240.2.0/24 |
| 60 | permit 157.240.3.0/24 |
| 70 | permit 185.60.216.0/24 |
| 80 | permit 185.60.217.0/24 |

##### PL_MICROSOFT_8075

| Sequence | Action |
| -------- | ------ |
| 10 | permit 13.64.0.0/24 |
| 20 | permit 13.65.0.0/24 |
| 30 | permit 20.33.0.0/24 |
| 40 | permit 20.34.0.0/24 |
| 50 | permit 40.64.0.0/24 |
| 60 | permit 40.65.0.0/24 |
| 70 | permit 40.74.0.0/24 |
| 80 | permit 40.75.0.0/24 |

##### PL_NETFLIX_2906

| Sequence | Action |
| -------- | ------ |
| 10 | permit 45.57.0.0/24 |
| 20 | permit 45.57.1.0/24 |
| 30 | permit 23.246.0.0/24 |
| 40 | permit 23.246.1.0/24 |
| 50 | permit 198.38.96.0/24 |
| 60 | permit 198.38.97.0/24 |

##### PL_NTTCOM_4713

| Sequence | Action |
| -------- | ------ |
| 10 | permit 210.145.0.0/24 |
| 20 | permit 210.145.1.0/24 |
| 30 | permit 210.146.0.0/24 |
| 40 | permit 210.146.1.0/24 |

##### PL_ORACLE_31898

| Sequence | Action |
| -------- | ------ |
| 10 | permit 129.146.0.0/24 |
| 20 | permit 129.146.1.0/24 |
| 30 | permit 132.226.0.0/24 |
| 40 | permit 132.226.1.0/24 |

##### PL_ORANGE_5511

| Sequence | Action |
| -------- | ------ |
| 10 | permit 80.10.0.0/24 |
| 20 | permit 80.11.0.0/24 |
| 30 | permit 80.12.0.0/24 |
| 40 | permit 193.248.0.0/24 |
| 50 | permit 193.249.0.0/24 |
| 60 | permit 193.250.0.0/24 |

##### PL_OVH_16276

| Sequence | Action |
| -------- | ------ |
| 10 | permit 51.68.0.0/24 |
| 20 | permit 51.68.1.0/24 |
| 30 | permit 51.75.0.0/24 |
| 40 | permit 51.75.1.0/24 |

##### PL_SALESFORCE_14340

| Sequence | Action |
| -------- | ------ |
| 10 | permit 13.108.0.0/24 |
| 20 | permit 13.108.1.0/24 |
| 30 | permit 13.110.0.0/24 |
| 40 | permit 13.110.1.0/24 |

##### PL_SCALEWAY_12876

| Sequence | Action |
| -------- | ------ |
| 10 | permit 51.158.0.0/24 |
| 20 | permit 51.158.1.0/24 |

##### PL_SOFTBANK_17676

| Sequence | Action |
| -------- | ------ |
| 10 | permit 126.0.0.0/24 |
| 20 | permit 126.1.0.0/24 |
| 30 | permit 126.2.0.0/24 |
| 40 | permit 126.3.0.0/24 |

##### PL_SPOTIFY_8403

| Sequence | Action |
| -------- | ------ |
| 10 | permit 35.186.224.0/24 |
| 20 | permit 35.186.225.0/24 |

##### PL_SWISSCOM_3303

| Sequence | Action |
| -------- | ------ |
| 10 | permit 195.186.0.0/24 |
| 20 | permit 195.186.1.0/24 |
| 30 | permit 195.186.2.0/24 |
| 40 | permit 195.186.3.0/24 |

##### PL_TELEFONICA_12956

| Sequence | Action |
| -------- | ------ |
| 10 | permit 80.58.0.0/24 |
| 20 | permit 80.59.0.0/24 |
| 30 | permit 213.4.0.0/24 |
| 40 | permit 213.5.0.0/24 |

##### PL_TENCENT_132203

| Sequence | Action |
| -------- | ------ |
| 10 | permit 162.62.0.0/24 |
| 20 | permit 162.62.1.0/24 |
| 30 | permit 162.14.0.0/24 |
| 40 | permit 162.14.1.0/24 |

##### PL_TMOBILE_21928

| Sequence | Action |
| -------- | ------ |
| 10 | permit 172.32.0.0/24 |
| 20 | permit 172.33.0.0/24 |
| 30 | permit 172.34.0.0/24 |
| 40 | permit 172.35.0.0/24 |
| 50 | permit 208.54.0.0/24 |
| 60 | permit 208.54.1.0/24 |

##### PL_TWITCH_46489

| Sequence | Action |
| -------- | ------ |
| 10 | permit 185.166.140.0/24 |
| 20 | permit 185.166.141.0/24 |
| 30 | permit 99.181.64.0/24 |
| 40 | permit 99.181.65.0/24 |

##### PL_TWITTER_13414

| Sequence | Action |
| -------- | ------ |
| 10 | permit 104.244.42.0/24 |
| 20 | permit 104.244.43.0/24 |
| 30 | permit 104.244.44.0/24 |
| 40 | permit 199.16.156.0/24 |
| 50 | permit 199.16.157.0/24 |
| 60 | permit 199.59.148.0/24 |

##### PL_VALVE_32590

| Sequence | Action |
| -------- | ------ |
| 10 | permit 162.254.192.0/24 |
| 20 | permit 162.254.193.0/24 |

##### PL_VERIZON_701

| Sequence | Action |
| -------- | ------ |
| 10 | permit 71.160.0.0/24 |
| 20 | permit 71.161.0.0/24 |
| 30 | permit 98.0.0.0/24 |
| 40 | permit 98.1.0.0/24 |
| 50 | permit 108.0.0.0/24 |
| 60 | permit 108.1.0.0/24 |

##### PL_VODAFONE_3209

| Sequence | Action |
| -------- | ------ |
| 10 | permit 83.137.0.0/24 |
| 20 | permit 83.138.0.0/24 |
| 30 | permit 83.139.0.0/24 |
| 40 | permit 212.183.0.0/24 |
| 50 | permit 212.184.0.0/24 |
| 60 | permit 212.185.0.0/24 |

##### PL_ZOOM_52347

| Sequence | Action |
| -------- | ------ |
| 10 | permit 170.114.0.0/24 |
| 20 | permit 170.114.1.0/24 |
| 30 | permit 170.114.2.0/24 |
| 40 | permit 170.114.3.0/24 |

#### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL_AKAMAI_20940
   seq 10 permit 23.32.0.0/24
   seq 20 permit 23.33.0.0/24
   seq 30 permit 23.34.0.0/24
   seq 40 permit 23.35.0.0/24
   seq 50 permit 104.64.0.0/24
   seq 60 permit 104.65.0.0/24
!
ip prefix-list PL_ALIBABA_45102
   seq 10 permit 47.74.0.0/24
   seq 20 permit 47.75.0.0/24
   seq 30 permit 47.88.0.0/24
   seq 40 permit 47.89.0.0/24
   seq 50 permit 47.90.0.0/24
   seq 60 permit 47.91.0.0/24
!
ip prefix-list PL_AMAZON_16509
   seq 10 permit 3.0.0.0/24
   seq 20 permit 3.2.0.0/24
   seq 30 permit 15.197.0.0/24
   seq 40 permit 15.197.1.0/24
   seq 50 permit 52.94.0.0/24
   seq 60 permit 52.95.0.0/24
   seq 70 permit 54.239.0.0/24
   seq 80 permit 54.239.1.0/24
!
ip prefix-list PL_APPLE_714
   seq 10 permit 17.248.0.0/24
   seq 20 permit 17.248.1.0/24
   seq 30 permit 17.249.0.0/24
   seq 40 permit 17.249.1.0/24
   seq 50 permit 17.250.0.0/24
   seq 60 permit 17.250.1.0/24
   seq 70 permit 17.251.0.0/24
   seq 80 permit 17.252.0.0/24
!
ip prefix-list PL_ATT_7018
   seq 10 permit 12.0.0.0/24
   seq 20 permit 12.1.0.0/24
   seq 30 permit 12.2.0.0/24
   seq 40 permit 32.0.0.0/24
   seq 50 permit 32.1.0.0/24
   seq 60 permit 32.2.0.0/24
!
ip prefix-list PL_BT_2856
   seq 10 permit 62.6.0.0/24
   seq 20 permit 62.7.0.0/24
   seq 30 permit 62.8.0.0/24
   seq 40 permit 86.128.0.0/24
   seq 50 permit 86.129.0.0/24
   seq 60 permit 86.130.0.0/24
!
ip prefix-list PL_CHARTER_20115
   seq 10 permit 24.16.0.0/24
   seq 20 permit 24.17.0.0/24
   seq 30 permit 97.80.0.0/24
   seq 40 permit 97.81.0.0/24
   seq 50 permit 71.74.0.0/24
   seq 60 permit 71.75.0.0/24
!
ip prefix-list PL_CLOUDFLARE_13335
   seq 10 permit 1.1.1.0/24
   seq 20 permit 1.0.0.0/24
   seq 30 permit 104.16.0.0/24
   seq 40 permit 104.17.0.0/24
   seq 50 permit 104.18.0.0/24
   seq 60 permit 104.19.0.0/24
   seq 70 permit 172.64.0.0/24
   seq 80 permit 172.65.0.0/24
!
ip prefix-list PL_COMCAST_7922
   seq 10 permit 24.0.0.0/24
   seq 20 permit 24.1.0.0/24
   seq 30 permit 73.0.0.0/24
   seq 40 permit 73.1.0.0/24
   seq 50 permit 75.64.0.0/24
   seq 60 permit 75.65.0.0/24
!
ip prefix-list PL_DIGITALOCEAN_14061
   seq 10 permit 104.131.0.0/24
   seq 20 permit 104.131.1.0/24
   seq 30 permit 159.65.0.0/24
   seq 40 permit 159.65.1.0/24
!
ip prefix-list PL_DTAG_3320
   seq 10 permit 46.5.0.0/24
   seq 20 permit 46.6.0.0/24
   seq 30 permit 46.7.0.0/24
   seq 40 permit 80.128.0.0/24
   seq 50 permit 80.129.0.0/24
   seq 60 permit 80.130.0.0/24
!
ip prefix-list PL_FASTLY_54113
   seq 10 permit 151.101.0.0/24
   seq 20 permit 151.101.1.0/24
   seq 30 permit 151.101.2.0/24
   seq 40 permit 199.232.0.0/24
   seq 50 permit 199.232.1.0/24
   seq 60 permit 199.232.2.0/24
!
ip prefix-list PL_GITHUB_36459
   seq 10 permit 140.82.112.0/24
   seq 20 permit 140.82.113.0/24
   seq 30 permit 192.30.252.0/24
   seq 40 permit 192.30.253.0/24
!
ip prefix-list PL_GOOGLE_15169
   seq 10 permit 8.8.8.0/24
   seq 20 permit 8.8.4.0/24
   seq 30 permit 142.250.0.0/24
   seq 40 permit 142.250.1.0/24
   seq 50 permit 172.217.0.0/24
   seq 60 permit 172.217.1.0/24
   seq 70 permit 216.58.192.0/24
   seq 80 permit 216.58.193.0/24
!
ip prefix-list PL_HETZNER_24940
   seq 10 permit 65.21.0.0/24
   seq 20 permit 65.21.1.0/24
!
ip prefix-list PL_KDDI_2516
   seq 10 permit 27.80.0.0/24
   seq 20 permit 27.81.0.0/24
   seq 30 permit 27.82.0.0/24
   seq 40 permit 27.83.0.0/24
!
ip prefix-list PL_LINKEDIN_14413
   seq 10 permit 108.174.0.0/24
   seq 20 permit 108.174.1.0/24
   seq 30 permit 144.2.0.0/24
   seq 40 permit 144.2.1.0/24
!
ip prefix-list PL_LINODE_63949
   seq 10 permit 45.33.0.0/24
   seq 20 permit 45.33.1.0/24
   seq 30 permit 139.162.0.0/24
   seq 40 permit 139.162.1.0/24
!
ip prefix-list PL_META_32934
   seq 10 permit 31.13.24.0/24
   seq 20 permit 31.13.25.0/24
   seq 30 permit 157.240.0.0/24
   seq 40 permit 157.240.1.0/24
   seq 50 permit 157.240.2.0/24
   seq 60 permit 157.240.3.0/24
   seq 70 permit 185.60.216.0/24
   seq 80 permit 185.60.217.0/24
!
ip prefix-list PL_MICROSOFT_8075
   seq 10 permit 13.64.0.0/24
   seq 20 permit 13.65.0.0/24
   seq 30 permit 20.33.0.0/24
   seq 40 permit 20.34.0.0/24
   seq 50 permit 40.64.0.0/24
   seq 60 permit 40.65.0.0/24
   seq 70 permit 40.74.0.0/24
   seq 80 permit 40.75.0.0/24
!
ip prefix-list PL_NETFLIX_2906
   seq 10 permit 45.57.0.0/24
   seq 20 permit 45.57.1.0/24
   seq 30 permit 23.246.0.0/24
   seq 40 permit 23.246.1.0/24
   seq 50 permit 198.38.96.0/24
   seq 60 permit 198.38.97.0/24
!
ip prefix-list PL_NTTCOM_4713
   seq 10 permit 210.145.0.0/24
   seq 20 permit 210.145.1.0/24
   seq 30 permit 210.146.0.0/24
   seq 40 permit 210.146.1.0/24
!
ip prefix-list PL_ORACLE_31898
   seq 10 permit 129.146.0.0/24
   seq 20 permit 129.146.1.0/24
   seq 30 permit 132.226.0.0/24
   seq 40 permit 132.226.1.0/24
!
ip prefix-list PL_ORANGE_5511
   seq 10 permit 80.10.0.0/24
   seq 20 permit 80.11.0.0/24
   seq 30 permit 80.12.0.0/24
   seq 40 permit 193.248.0.0/24
   seq 50 permit 193.249.0.0/24
   seq 60 permit 193.250.0.0/24
!
ip prefix-list PL_OVH_16276
   seq 10 permit 51.68.0.0/24
   seq 20 permit 51.68.1.0/24
   seq 30 permit 51.75.0.0/24
   seq 40 permit 51.75.1.0/24
!
ip prefix-list PL_SALESFORCE_14340
   seq 10 permit 13.108.0.0/24
   seq 20 permit 13.108.1.0/24
   seq 30 permit 13.110.0.0/24
   seq 40 permit 13.110.1.0/24
!
ip prefix-list PL_SCALEWAY_12876
   seq 10 permit 51.158.0.0/24
   seq 20 permit 51.158.1.0/24
!
ip prefix-list PL_SOFTBANK_17676
   seq 10 permit 126.0.0.0/24
   seq 20 permit 126.1.0.0/24
   seq 30 permit 126.2.0.0/24
   seq 40 permit 126.3.0.0/24
!
ip prefix-list PL_SPOTIFY_8403
   seq 10 permit 35.186.224.0/24
   seq 20 permit 35.186.225.0/24
!
ip prefix-list PL_SWISSCOM_3303
   seq 10 permit 195.186.0.0/24
   seq 20 permit 195.186.1.0/24
   seq 30 permit 195.186.2.0/24
   seq 40 permit 195.186.3.0/24
!
ip prefix-list PL_TELEFONICA_12956
   seq 10 permit 80.58.0.0/24
   seq 20 permit 80.59.0.0/24
   seq 30 permit 213.4.0.0/24
   seq 40 permit 213.5.0.0/24
!
ip prefix-list PL_TENCENT_132203
   seq 10 permit 162.62.0.0/24
   seq 20 permit 162.62.1.0/24
   seq 30 permit 162.14.0.0/24
   seq 40 permit 162.14.1.0/24
!
ip prefix-list PL_TMOBILE_21928
   seq 10 permit 172.32.0.0/24
   seq 20 permit 172.33.0.0/24
   seq 30 permit 172.34.0.0/24
   seq 40 permit 172.35.0.0/24
   seq 50 permit 208.54.0.0/24
   seq 60 permit 208.54.1.0/24
!
ip prefix-list PL_TWITCH_46489
   seq 10 permit 185.166.140.0/24
   seq 20 permit 185.166.141.0/24
   seq 30 permit 99.181.64.0/24
   seq 40 permit 99.181.65.0/24
!
ip prefix-list PL_TWITTER_13414
   seq 10 permit 104.244.42.0/24
   seq 20 permit 104.244.43.0/24
   seq 30 permit 104.244.44.0/24
   seq 40 permit 199.16.156.0/24
   seq 50 permit 199.16.157.0/24
   seq 60 permit 199.59.148.0/24
!
ip prefix-list PL_VALVE_32590
   seq 10 permit 162.254.192.0/24
   seq 20 permit 162.254.193.0/24
!
ip prefix-list PL_VERIZON_701
   seq 10 permit 71.160.0.0/24
   seq 20 permit 71.161.0.0/24
   seq 30 permit 98.0.0.0/24
   seq 40 permit 98.1.0.0/24
   seq 50 permit 108.0.0.0/24
   seq 60 permit 108.1.0.0/24
!
ip prefix-list PL_VODAFONE_3209
   seq 10 permit 83.137.0.0/24
   seq 20 permit 83.138.0.0/24
   seq 30 permit 83.139.0.0/24
   seq 40 permit 212.183.0.0/24
   seq 50 permit 212.184.0.0/24
   seq 60 permit 212.185.0.0/24
!
ip prefix-list PL_ZOOM_52347
   seq 10 permit 170.114.0.0/24
   seq 20 permit 170.114.1.0/24
   seq 30 permit 170.114.2.0/24
   seq 40 permit 170.114.3.0/24
```

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| ARELION | enabled |
| COGENT | enabled |
| GTT | enabled |
| LUMEN | enabled |
| NTT | enabled |
| OOB | disabled |

### VRF Instances Device Configuration

```eos
!
vrf instance ARELION
   description Arelion (AS1299)
!
vrf instance COGENT
   description Cogent (AS174)
!
vrf instance GTT
   description GTT (AS3257)
!
vrf instance LUMEN
   description Lumen (AS3356)
!
vrf instance NTT
   description NTT (AS2914)
!
vrf instance OOB
```
