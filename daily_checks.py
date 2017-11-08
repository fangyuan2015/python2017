#!/usr/bin/evn python
#coding: utf-8
#Script Name: daily_checks.py
#Author: Craig Richards
#Created: 07th December 2011
#Last Modified: 01st May 2013
#Version: 1.4

#Modifications: 1.1 Removed the static lines for the putty session,it now reada a file,loops through and make the connections.

#Description： This simple script loads everything I need to carry out the daily checks for our system.

import platform
import os
import subprocess
import sys
#Load the Library Module

from time import strftime
#Load just the strtime Module from time

def clean_screen():
#function to clean the screen
    if os.name == 'posix':
#Unix/Linux/MacOS/BSD/etc
	os.system('clear')
    elif os.name in ('nt','dos','ce'):
#DOS/Windows
	os.system('CLS')
#Clear the Screen
def print_docs():
    print "Printing Daily Check Sheets:"
#The command below passes the command line string to open word,open the docment,print it then close word down.
    subprocess.Popen(["C:\\Program Files (x86)\Microsoft Office\Office14\winword.exe","P:\\\\Docmentation\\Daily Docs\\Back office"])
def putty_sessions():
    for server in open(conffilename):
	subprocess.Popen(('putty-load '+server))
#Open the PuTTY sessions
def rdp_sessions():
    print "Loading RDP Sessions:"
    subprocess.Popen("mstsc eclr.rdp")
#Open up a terminal session connection and load the euroclean session.
def euroclear_docs():
#The command below opens IE and loads the Euroclear password document
    subprocess.Popen('"C:\\Program Files\\Internet Explorer\\iexplore.exe"' '"file://fs1\pub_b\Pub_Admin\Documentation\Settlements_Files\PWD\Eclr.doc"')
#End of the functions
#Start of the Main Program

filename = sys.argv[0]
confdir = os.getenv("my_config")
conffile = ('daily_checks_servers.conf')
#Set the variable conffile -1.3
conffilename = os.path.join(confdir,conffile)
#Set the variable conffilename by join confdir and conffile together
clear_screen()
#The command below prints a little welcome message, as well as the script name,the date and the time and where is was run from.
print "Good Morning " + os.getenv('USERNAME')+","+filename,"ran at",strftime("%Y-%m-%d %H:%M:%S"),"on",platform.node(),"run from",os.getcwd()
print_docs()
putty_sessions()
rdp_sessions()
euroclear_docs()

