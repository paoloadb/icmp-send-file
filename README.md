
# icmp-send-file
### Send contents of a file line by line via icmp (ping) packets
\
Written in python3.  Just something I was messing around with one day.  :p

Uses scapy to send icmp packets\
you will need to run both as root.\
\
**example**: send the /etc/passwd file to the server\
on the server machine (let's say, with ip address 192.168.0.100):  `sudo python3 server.py`\
on the client machine: `sudo python3 client.py 192.168.0.100 /etc/passwd`

# Files

**server.py**: Listens for icmp packets from client.py, extracts and displays the data from the packet.\
**client.py**: Sends the icmp packet with the file contents as data payload.  One ping packet per line.

## Still a work in progress

I might, or might not, improve upon it. If you find some use for it somehow, feel free to build upon it if you like. 
