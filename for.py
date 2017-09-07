#!/usr/bin/env python
print """
Please input the flower words
(f)rom start word
(t)o end word
(i)ncresment word
(e)xit :exit the program
"""
while True:
    con = raw_input("do you want continue ")
    if con.strip()[0] == "e":
        break
    stanum = int(raw_input("please the from num:  "))
    endnum = int(raw_input("please the end num:  "))
    incnum = int(raw_input("please the incresment num:  "))
    print [x for x in range(stanum,endnum+1,incnum)]
    

