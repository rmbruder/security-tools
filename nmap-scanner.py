import sys

try:
    import nmap
except:
    sys.exit("[!] Install the NMAP library: pip install python-nmap")

# Command arguments

if len(sys.argv) != 3:
    sys.exit("Usage: nmap-scanner.py <targets> <ports>")

ports = str(sys.argv[2])
addrs = str(sys.argv[1])


scanner = nmap.PortScanner()

scanner.scan(addrs, ports)

for host in scanner.all_hosts():
    if not scanner[host].hostname():
        print("The host's IP address is %s and its hostname was not found" % (host))
    else:
        print('-------------------------------------------------------------------')
        print('Host: %s (%s)' % (host, scanner[host].hostname()))
