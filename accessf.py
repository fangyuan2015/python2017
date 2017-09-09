#!/usr/bin/env python
#coding:utf-8
fn = raw_input('Please input filename: ')
num = int(raw_input('请输入行数'))
fobj = open(fn,'r')
for i in range(num):
    print fobj.readline(),
