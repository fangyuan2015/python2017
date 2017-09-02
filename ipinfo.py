#!/usr/bin/env python
# -*- encoding=utf-8 -*-
from IPy import IP

ip_s = raw_input("Please input an IP or net-range: ")
ips = IP(ip_s)
if len(ips) > 1:
    print('net: %s' % ips.net())
#输出网络地址
    print('netmask: %s' % ips.netmask())
#输出网络掩码地址
    print('broadcast: %s' % ips.broadcast())
#输出网络广播地址
    print('reverse adress: %s' % ips.reverseNames()[0])
#输出IP反向解析
print('hexadecimal: %s' % ips.strHex())
#输出十六进制地址
print('binary ip: %s' % ips.strBin())
#输出二进制地址
print('iptype: %s' % ips.iptype())

