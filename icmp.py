#!/usr/bin/env python

try:
    from scapy.all import *
except:
    sys.exit('[!] Install the scapy libraries with: pip install scapy')

ip = '192.168.1.1'
icmp = IP(dst=ip)/ICMP()
resp = sr1(icmp, timeout=10)
