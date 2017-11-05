#!/usr/bin/env python
#coding: utf-8
#description: count a file each character,the return is directory
#filname变量应该为文件名的绝对路径
import sys

def countchars(filename):
    count = {}
#初始化一个空字典    
    with open(filename) as info:
#inputFile Replaced with filename
    	readfile = info.read()
    	for character in readfile.upper():
	    count[character] = count.get(character,0) + 1
#count.get用来获取已有count字典中character字符出现的次数，如果未出现则返回0，字符出现的次数作为键值
    	return count

if __name__ == '__main__':
    if sys.version_info.major >= 3:
# if the interpreter version is 3.X,use 'input'
# otherwise use 'raw_input'
    	input_func = input
    else:
	input_func = raw_input

    inputFile = input_func("File Name : ")
    print(countchars(inputFile))
