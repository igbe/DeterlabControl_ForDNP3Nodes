#!/usr/bin/python
import subprocess
import argparse
print "before import ssh"
import sshwithcmd
print "after import ssh"
def main():
	#print "make sure you have updated the node.txt"
	
	parser = argparse.ArgumentParser(description="Ping an experimental node.")
	parser.add_argument("node", type=str, help="deterlab node to ping from")
	parser.add_argument("ip", type=str, help="random node ip to ping to")
	args = parser.parse_args()
	
	node=args.node + ".Grid.TCPFlooding"
	ip=args.ip
	
	print "pinging %s from %s" %(ip,node) 
	cmd="ping %s -c 2"%(ip)
	output, error= sshwithcmd.sshwithcmd(node, cmd)
	print output,error
if __name__ == "__main__":
	main()
# p=subprocess.Popen(["python", file1], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# f = open('/tmp/nodelist.txt','r')
# for i in f.readlines():
# 	print i
