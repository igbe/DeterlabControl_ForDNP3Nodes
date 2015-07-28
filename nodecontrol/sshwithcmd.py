#!/usr/bin/python

import subprocess

def sshwithcmd(node,command):
	'''function for sshing into a node to run  a command which might include executing
	a script. Both node and scriptpath are string variables'''
	cmd=str(command)
	host=str(node)

	p=subprocess.Popen(["ssh", "%s" % host, cmd], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	(output, err) = p.communicate()
	return output,err
