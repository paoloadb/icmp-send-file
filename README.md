
# icmp-send-file
Written in python3.  Just something I was messing around with one day.  :p
Send contents of a file line by line via icmp (ping) packets
Uses scapy to send icmp packets

# Files

**server.py**: Listens for icmp packets from client.py, extracts and displays the data from the packet.\
**client.py**: Sends the icmp packet with the file contents as data payload.  One ping packet per line.

## Still a work in progress

I might, or might not, improve upon it. If you find some use for it somehow, feel free to build upon it if you like. 
