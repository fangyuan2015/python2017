#!/usr/bin/env python
#coding: utf-8
#filename: client.py

import socket 
#导入socket模块

s = socket.socket()
#创建socket对象
#host = socket.gethostname()
host = 'localhost'
#获取本地主机名
port = 12345
#设置好端口

s.connect((host,port))
print s.recv(1024)
s.close()

