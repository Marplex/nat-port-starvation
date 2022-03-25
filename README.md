# NAT Port Starvation

Fill the NAT port mapping table with useless port/ip records.

## How it works

```python
for sport in range(0, 60999):
    udp_header = struct.pack('!HHHH', sport, dport, length, checksum)
    s.sendto(udp_header+data, ('1.1.1.1', 0));
```

I made this tool for fun while learning NAT, specifically port mapping.
On the transport layer, TCP and UDP protocols use source and destination ports to communicate with other hosts.
To connect with servers out of the local network, the router creates and maintains a table associating internal port/ip to destination port/ip.

|        LAN        |        WAN         |
| :---------------: | :----------------: |
| 192.168.1.2: 1546 | 230.100.10.1: 7777 |
| 192.168.1.2: 1547 | 230.100.10.1: 7778 |

If never used, entries on this table are deleted after some time (depends on the router). But if you are quick, you can fill this table with junk data, leaving no space for real requests and therefore "disabling" access to the WAN.

## How to use

Just run `main.py` and you'll disable internet access for 1/2 minutes depending on your router (or it might not work)
