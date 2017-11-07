#!/usr/bin/env python
#coding:utf-8

#Script Name: batch_file_rename.py
#Author: Craig Richards
#Created: 6th August 2012
#Last Modified: 
#Version:	1.0

#Modifications:
#Description: This will batch rename a group of files in a given directory,once you pass the current and new extensions

import os
import sys

work_dir = sys.argv[1]
old_ext = sys.argv[2]
new_ext = sys.argv[3]
#Set the variable work_dir with the first argument passed
files = os.listdir(work_dir)

for filename in files:
    file_ext = os.path.splitext(filename)[1]
#Get the file extention
    if old_ext == file_ext:
	newfile = filename.replace(old_ext,new_ext)
#Set newfile to be the file name,replace with the new extension
	os.rename(os.path.join(work_dir,filename),os.path.join(work_dir,newfile))


