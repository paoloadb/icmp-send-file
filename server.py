import socket
import sys
import struct

def listen_for_ping():
  s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
  s.setsockopt(socket.SOL_IP, socket.IP_HDRINCL, 1)
  while 1:
    data, addr = s.recvfrom(65535)
    print(data[28:].decode("utf-8").strip())

try:
    listen_for_ping()
except KeyboardInterrupt:
    sys.exit()
