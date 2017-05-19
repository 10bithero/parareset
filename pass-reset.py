#!/usr/bin/python
'''
DESC:
	- Simple password reset utility. should work with GNU/Linux systems running standard bash shell
TODO:
	- prompt for username (with auto-default to current user)
	- prompt for hostname
	- add option to parse file of hostnames
'''


import sys
import paramiko
import getpass

def createpass():
	global newpass
	newpass = getpass.getpass('Desired password:\n')
	newpass2 = getpass.getpass('Retype password:\n')
	checkpass(newpass, newpass2)


def checkpass(newpass,newpass2):
	if newpass != newpass2:
		print 'passwords do not match!'
		createpass()
	else:
		print 'passwords match\ncontinuing program'
		return newpass


def connect2host(currpass, newpass):
	s = paramiko.SSHClient()
	s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	s.connect('', username='',password=currpass)
	stdin, stdout, stderr = s.exec_command('passwd')
	stdin.write(currpass)
	stdin.write('\n')
	stdin.flush()
	stdin.write(newpass)
	stdin.write('\n')
	stdin.flush()
	stdin.write(newpass)
	stdin.write('\n')
	stdin.flush()
	print stdout.readlines()
	s.close()

if __name__ == "__main__":
	createpass()
	currpass = getpass.getpass('Current Password: ')
	connect2host(currpass, newpass)
