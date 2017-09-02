#!/usr/bin/env python
# -*- encoding=utf-8 -*-
import dns.resolver

domain = raw_input('Please input an domain: ')
MX = dns.resolver.query(domain,'MX')
#指定查询内容为MX
for i in MX:
#遍历回应结果，输出MX记录的prefernece及exchanger信息
    print 'MX preference=',i.preference,'mail exchanger = ',i.exchange
