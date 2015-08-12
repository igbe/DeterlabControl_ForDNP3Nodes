#!/usr/bin/python
import subprocess
import sshwithcmd
import random

print "starting pinging....."

def get_node_ip(node_ip):
	''' returns the node and ip from a node.txt file with "node,ip" as content
	''' 
	print "in get node function"
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
	
	nodes,ips=get_node_ip("/users/oigbe000/DeterlabControl/nodecontrol/node.txt")	
	print nodes, ips		
	
	
	while True:
	    print "in while one"
	    node=random.choice(nodes)
	    node=node + ".Grid.TCPFlooding"
	    ip=random.choice(ips)
	    print "pinging %s from %s" %(ip,node) 
	    cmd="ping %s -c 2"%(ip)
	    output, error= sshwithcmd.sshwithcmd(node, cmd)
	    
	    print output,error
	print "out of while loop"
if __name__ == "__main__":
	main()
