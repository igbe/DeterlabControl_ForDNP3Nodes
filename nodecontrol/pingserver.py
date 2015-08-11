#!/usr/bin/python
import sshwithcmd
import subprocess
import random

def get_node_ip(node_ip):
	''' returns the node and ip from a node.txt file with "node,ip" as content
	''' 
	ip=[]
	node=[]
	f = open(node_ip,'r')
	for j in f.readlines():
		n,i=j.split(",")
		node.append(n)
		ip.append(i.strip('\n'))
	return node,ip

def main():
	print "make sure you have updated the node.txt"
	node,ip=get_node_ip("node.txt")
	cmd="python pingclient.py %s %s"%(random.choice(node),random.choice(ip))
	sshwithcmd.sshwithcmd("oigbe000@users.isi.deterlab.net",cmd)


if __name__ == "__main__":
	main()
# p=subprocess.Popen(["python", file1], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# f = open('/tmp/nodelist.txt','r')
# for i in f.readlines():
# 	print i