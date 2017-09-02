#!/usr/bin/env python
# -*- encoding=utf-8 -*-
import dns.resolver

domain = raw_input('Please input an domain: ')
ns = dns.resolver.query(domain,'NS')
#指定查询类型为NS记录
for i in ns.response.answer:
    for j in i.items:
	print j.to_text()

