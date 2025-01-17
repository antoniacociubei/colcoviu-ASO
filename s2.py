#!/usr/bin/env python3

import scapy.all as scapy

def scan(network):
    print(f"Scanez rețeaua: {network}")
    # scapy.arping va trimite ARP Requests către fiecare IP din subnet
    # și va afișa cine a răspuns (IP & MAC).
    answered, unanswered = scapy.arping(network)
    
    print("\n--- Rezultate scanare ---")
    for sent, received in answered:
        print(f"IP: {received.psrc}\t MAC: {received.hwsrc}")

if __name__ == "__main__":
    # Înlocuiește cu subnetul VLAN-ului tău, de ex. 10.8.11.0/24
    vlan_subnet = "10.8.11.0/24"
    scan(vlan_subnet)
