#!/usr/bin/env python
#Author: Craig Richards
#Created: 19th July 2012
#Last Modified: 
#Description: This will scan the current directory and all subdirectorries and display the size.

import os,sys

directory = sys.argv[1]
dir_size = 0
for (path,dirs,files) in os.walk(directory):
#Walk through all the directories
    for file in files:
	filename = os.path.join(path,file)
	dir_size += os.path.getsize(filename)
#Get the sizes,the following lines print the sizes in bytes,kb,Mband Gb
print "Folder Size in Bytes = %0.2f Bytes" % (dir_size)
print "Folder Size in Kilobytes = %0.2f KB" % (dir_size/1024.0)
print "Folder Size in Megabytes = %0.2f MB" % (dir_size/1024/1024.0)
print "Folder Size in Gigabytes = %0.2f GB" % (dir_size/1024/1024/1024.0)

