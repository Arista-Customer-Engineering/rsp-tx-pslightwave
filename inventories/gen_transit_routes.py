#!/usr/bin/env python3
"""Generate static routes, prefix lists, and RCF functions for TRANSIT.yml.

Produces YAML fragments for ~200 realistic prefixes distributed across
5 carrier VRFs with AS-path injection via RCF (Router Control Functions).
"""

import yaml

CARRIERS = {
    "ARELION": {
        "as": "1299",
        "origins": {
            "15169": {  # Google
                "name": "GOOGLE",
                "prefixes": [
                    "8.8.8.0/24", "8.8.4.0/24", "142.250.0.0/24", "142.250.1.0/24",
                    "172.217.0.0/24", "172.217.1.0/24", "216.58.192.0/24", "216.58.193.0/24",
                ],
            },
            "16509": {  # Amazon/AWS
                "name": "AMAZON",
                "prefixes": [
                    "3.0.0.0/24", "3.2.0.0/24", "15.197.0.0/24", "15.197.1.0/24",
                    "52.94.0.0/24", "52.95.0.0/24", "54.239.0.0/24", "54.239.1.0/24",
                ],
            },
            "2906": {  # Netflix
                "name": "NETFLIX",
                "prefixes": [
                    "45.57.0.0/24", "45.57.1.0/24", "23.246.0.0/24", "23.246.1.0/24",
                    "198.38.96.0/24", "198.38.97.0/24",
                ],
            },
            "20940": {  # Akamai
                "name": "AKAMAI",
                "prefixes": [
                    "23.32.0.0/24", "23.33.0.0/24", "23.34.0.0/24", "23.35.0.0/24",
                    "104.64.0.0/24", "104.65.0.0/24",
                ],
            },
            "7018": {  # AT&T
                "name": "ATT",
                "prefixes": [
                    "12.0.0.0/24", "12.1.0.0/24", "12.2.0.0/24",
                    "32.0.0.0/24", "32.1.0.0/24", "32.2.0.0/24",
                ],
            },
            "7922": {  # Comcast
                "name": "COMCAST",
                "prefixes": [
                    "24.0.0.0/24", "24.1.0.0/24", "73.0.0.0/24",
                    "73.1.0.0/24", "75.64.0.0/24", "75.65.0.0/24",
                ],
            },
        },
    },
    "COGENT": {
        "as": "174",
        "origins": {
            "13335": {  # Cloudflare
                "name": "CLOUDFLARE",
                "prefixes": [
                    "1.1.1.0/24", "1.0.0.0/24", "104.16.0.0/24", "104.17.0.0/24",
                    "104.18.0.0/24", "104.19.0.0/24", "172.64.0.0/24", "172.65.0.0/24",
                ],
            },
            "8075": {  # Microsoft
                "name": "MICROSOFT",
                "prefixes": [
                    "13.64.0.0/24", "13.65.0.0/24", "20.33.0.0/24", "20.34.0.0/24",
                    "40.64.0.0/24", "40.65.0.0/24", "40.74.0.0/24", "40.75.0.0/24",
                ],
            },
            "36459": {  # GitHub
                "name": "GITHUB",
                "prefixes": [
                    "140.82.112.0/24", "140.82.113.0/24",
                    "192.30.252.0/24", "192.30.253.0/24",
                ],
            },
            "14061": {  # DigitalOcean
                "name": "DIGITALOCEAN",
                "prefixes": [
                    "104.131.0.0/24", "104.131.1.0/24",
                    "159.65.0.0/24", "159.65.1.0/24",
                ],
            },
            "54113": {  # Fastly
                "name": "FASTLY",
                "prefixes": [
                    "151.101.0.0/24", "151.101.1.0/24", "151.101.2.0/24",
                    "199.232.0.0/24", "199.232.1.0/24", "199.232.2.0/24",
                ],
            },
            "20115": {  # Charter/Spectrum
                "name": "CHARTER",
                "prefixes": [
                    "24.16.0.0/24", "24.17.0.0/24", "97.80.0.0/24",
                    "97.81.0.0/24", "71.74.0.0/24", "71.75.0.0/24",
                ],
            },
            "31898": {  # Oracle Cloud
                "name": "ORACLE",
                "prefixes": [
                    "129.146.0.0/24", "129.146.1.0/24",
                    "132.226.0.0/24", "132.226.1.0/24",
                ],
            },
        },
    },
    "LUMEN": {
        "as": "3356",
        "origins": {
            "32934": {  # Meta/Facebook
                "name": "META",
                "prefixes": [
                    "31.13.24.0/24", "31.13.25.0/24", "157.240.0.0/24", "157.240.1.0/24",
                    "157.240.2.0/24", "157.240.3.0/24", "185.60.216.0/24", "185.60.217.0/24",
                ],
            },
            "714": {  # Apple
                "name": "APPLE",
                "prefixes": [
                    "17.248.0.0/24", "17.248.1.0/24", "17.249.0.0/24", "17.249.1.0/24",
                    "17.250.0.0/24", "17.250.1.0/24", "17.251.0.0/24", "17.252.0.0/24",
                ],
            },
            "701": {  # Verizon
                "name": "VERIZON",
                "prefixes": [
                    "71.160.0.0/24", "71.161.0.0/24", "98.0.0.0/24",
                    "98.1.0.0/24", "108.0.0.0/24", "108.1.0.0/24",
                ],
            },
            "21928": {  # T-Mobile
                "name": "TMOBILE",
                "prefixes": [
                    "172.32.0.0/24", "172.33.0.0/24", "172.34.0.0/24",
                    "172.35.0.0/24", "208.54.0.0/24", "208.54.1.0/24",
                ],
            },
            "63949": {  # Linode/Akamai Connected
                "name": "LINODE",
                "prefixes": [
                    "45.33.0.0/24", "45.33.1.0/24",
                    "139.162.0.0/24", "139.162.1.0/24",
                ],
            },
            "14340": {  # Salesforce
                "name": "SALESFORCE",
                "prefixes": [
                    "13.108.0.0/24", "13.108.1.0/24",
                    "13.110.0.0/24", "13.110.1.0/24",
                ],
            },
            "46489": {  # Twitch
                "name": "TWITCH",
                "prefixes": [
                    "185.166.140.0/24", "185.166.141.0/24",
                    "99.181.64.0/24", "99.181.65.0/24",
                ],
            },
        },
    },
    "NTT_VRF": {
        "as": "2914",
        "origins": {
            "13414": {  # Twitter/X
                "name": "TWITTER",
                "prefixes": [
                    "104.244.42.0/24", "104.244.43.0/24", "104.244.44.0/24",
                    "199.16.156.0/24", "199.16.157.0/24", "199.59.148.0/24",
                ],
            },
            "52347": {  # Zoom
                "name": "ZOOM",
                "prefixes": [
                    "170.114.0.0/24", "170.114.1.0/24",
                    "170.114.2.0/24", "170.114.3.0/24",
                ],
            },
            "45102": {  # Alibaba
                "name": "ALIBABA",
                "prefixes": [
                    "47.74.0.0/24", "47.75.0.0/24", "47.88.0.0/24",
                    "47.89.0.0/24", "47.90.0.0/24", "47.91.0.0/24",
                ],
            },
            "132203": {  # Tencent
                "name": "TENCENT",
                "prefixes": [
                    "162.62.0.0/24", "162.62.1.0/24",
                    "162.14.0.0/24", "162.14.1.0/24",
                ],
            },
            "17676": {  # SoftBank
                "name": "SOFTBANK",
                "prefixes": [
                    "126.0.0.0/24", "126.1.0.0/24",
                    "126.2.0.0/24", "126.3.0.0/24",
                ],
            },
            "2516": {  # KDDI
                "name": "KDDI",
                "prefixes": [
                    "27.80.0.0/24", "27.81.0.0/24",
                    "27.82.0.0/24", "27.83.0.0/24",
                ],
            },
            "4713": {  # NTT Communications
                "name": "NTTCOM",
                "prefixes": [
                    "210.145.0.0/24", "210.145.1.0/24",
                    "210.146.0.0/24", "210.146.1.0/24",
                ],
            },
            "14413": {  # LinkedIn
                "name": "LINKEDIN",
                "prefixes": [
                    "108.174.0.0/24", "108.174.1.0/24",
                    "144.2.0.0/24", "144.2.1.0/24",
                ],
            },
            "8403": {  # Spotify
                "name": "SPOTIFY",
                "prefixes": [
                    "35.186.224.0/24", "35.186.225.0/24",
                ],
            },
            "32590": {  # Valve/Steam
                "name": "VALVE",
                "prefixes": [
                    "162.254.192.0/24", "162.254.193.0/24",
                ],
            },
        },
    },
    "GTT": {
        "as": "3257",
        "origins": {
            "3320": {  # Deutsche Telekom
                "name": "DTAG",
                "prefixes": [
                    "46.5.0.0/24", "46.6.0.0/24", "46.7.0.0/24",
                    "80.128.0.0/24", "80.129.0.0/24", "80.130.0.0/24",
                ],
            },
            "2856": {  # BT
                "name": "BT",
                "prefixes": [
                    "62.6.0.0/24", "62.7.0.0/24", "62.8.0.0/24",
                    "86.128.0.0/24", "86.129.0.0/24", "86.130.0.0/24",
                ],
            },
            "5511": {  # Orange
                "name": "ORANGE",
                "prefixes": [
                    "80.10.0.0/24", "80.11.0.0/24", "80.12.0.0/24",
                    "193.248.0.0/24", "193.249.0.0/24", "193.250.0.0/24",
                ],
            },
            "3209": {  # Vodafone
                "name": "VODAFONE",
                "prefixes": [
                    "83.137.0.0/24", "83.138.0.0/24", "83.139.0.0/24",
                    "212.183.0.0/24", "212.184.0.0/24", "212.185.0.0/24",
                ],
            },
            "12956": {  # Telefonica
                "name": "TELEFONICA",
                "prefixes": [
                    "80.58.0.0/24", "80.59.0.0/24",
                    "213.4.0.0/24", "213.5.0.0/24",
                ],
            },
            "3303": {  # Swisscom
                "name": "SWISSCOM",
                "prefixes": [
                    "195.186.0.0/24", "195.186.1.0/24",
                    "195.186.2.0/24", "195.186.3.0/24",
                ],
            },
            "16276": {  # OVH
                "name": "OVH",
                "prefixes": [
                    "51.68.0.0/24", "51.68.1.0/24",
                    "51.75.0.0/24", "51.75.1.0/24",
                ],
            },
            "24940": {  # Hetzner
                "name": "HETZNER",
                "prefixes": [
                    "65.21.0.0/24", "65.21.1.0/24",
                ],
            },
            "12876": {  # Scaleway
                "name": "SCALEWAY",
                "prefixes": [
                    "51.158.0.0/24", "51.158.1.0/24",
                ],
            },
        },
    },
}

# Map VRF key to actual VRF name in EOS config
VRF_NAME = {
    "ARELION": "ARELION",
    "COGENT": "COGENT",
    "LUMEN": "LUMEN",
    "NTT_VRF": "NTT",
    "GTT": "GTT",
}


def gen_static_routes():
    routes = []
    for carrier_key, data in CARRIERS.items():
        vrf = VRF_NAME[carrier_key]
        for _asn, origin in data["origins"].items():
            for pfx in origin["prefixes"]:
                routes.append(f"  - vrf: {vrf}\n    prefix: {pfx}\n    interface: \"null0\"")
    return "\n".join(routes)


def gen_prefix_lists():
    lines = []
    for _carrier, data in CARRIERS.items():
        for asn, origin in data["origins"].items():
            lines.append(f"  - name: PL_{origin['name']}_{asn}")
            lines.append(f"    sequence_numbers:")
            seq = 10
            for pfx in origin["prefixes"]:
                lines.append(f"      - sequence: {seq}")
                lines.append(f"        action: \"permit {pfx}\"")
                seq += 10
    return "\n".join(lines)


def gen_rcf_code():
    """Generate RCF functions for AS path injection on static redistribution."""
    functions = []
    for carrier_key, data in CARRIERS.items():
        vrf = VRF_NAME[carrier_key]
        func_name = f"SET_ORIGIN_{vrf}"
        lines = [f"      function {func_name}() -> bool {{"]
        first = True
        for asn, origin in data["origins"].items():
            pl_name = f"PL_{origin['name']}_{asn}"
            kw = "if" if first else "elif"
            lines.append(f"         {kw} match(source.prefix, prefix_list_v4(\"{pl_name}\")) {{")
            lines.append(f"            set(source.as_path, [{asn}]);")
            lines.append(f"            return true;")
            lines.append(f"         }}")
            first = False
        lines.append(f"         return false;")
        lines.append(f"      }}")
        functions.append("\n".join(lines))
    return "\n\n".join(functions)


def gen_bgp_redistribute():
    """Generate the redistribute lines for each VRF."""
    lines = []
    for carrier_key in CARRIERS:
        vrf = VRF_NAME[carrier_key]
        func_name = f"SET_ORIGIN_{vrf}"
        lines.append(f"    # VRF {vrf}: redistribute static rcf {func_name}()")
    return "\n".join(lines)


if __name__ == "__main__":
    total = sum(
        len(o["prefixes"])
        for c in CARRIERS.values()
        for o in c["origins"].values()
    )
    print(f"Total prefixes: {total}")
    for carrier_key, data in CARRIERS.items():
        vrf = VRF_NAME[carrier_key]
        count = sum(len(o["prefixes"]) for o in data["origins"].values())
        origins = len(data["origins"])
        print(f"  {vrf}: {count} prefixes across {origins} origin ASNs")

    print("\n\n=== STATIC ROUTES (add to static_routes:) ===")
    print(gen_static_routes())

    print("\n\n=== PREFIX LISTS (add to prefix_lists:) ===")
    print(gen_prefix_lists())

    print("\n\n=== RCF CODE (add to router_general.control_functions.code_units content) ===")
    print(gen_rcf_code())

    print("\n\n=== BGP REDISTRIBUTE NOTES ===")
    print(gen_bgp_redistribute())
