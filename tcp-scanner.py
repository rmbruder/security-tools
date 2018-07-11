#!/usr/bin/env python

from scapy.all import *

ip = '192.168.1.1'
dst_port = 443

headers = IP(dst=ip)/TCP(dport=dst_port, flags="S")
answers,unanswers=sr(headers,timeout=10)


print(answers)
