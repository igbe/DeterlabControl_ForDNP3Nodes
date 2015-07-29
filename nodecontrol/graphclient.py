#!/usr/bin/python
import argparse
import subprocess
import datetime
import time as tm
from time import sleep


def sshwithcmd(node,command):
	'''function for sshing into a node to run  a command which might include executing
	a script. Both node and scriptpath are string variables'''
	cmd=str(command)
	host=str(node)

	p=subprocess.Popen(["ssh", "%s" % host, cmd], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	(output, err) = p.communicate()
	return output,err

def task(host,time):
	
	i=time
	prevy=0
	prevy1=0
	print str(prevy)+","+ str(prevy1)+","+ str(tm.ctime())
	while i>0:
	
		command1="ip route get 10.1.1.1 | cut -b 14-17"
	        output1,err=sshwithcmd(host,command1)

        	command="cat /sys/class/net/%s/statistics/tx_bytes"%(output1[0:4])
	        output,err=sshwithcmd(host,command)

		command="cat /sys/class/net/%s/statistics/rx_bytes"%(output1[0:4])
                output2,err=sshwithcmd(host,command)


        	y=int(output.strip('\n'))
		y1=int(output2.strip('\n'))
	        x=tm.ctime()
        	
		if y==prevy:
			y=0
		else:
			prevy=y
		if y1==prevy1:
                        y1=0
                else:
                        prevy1=y1
		print str(y)+","+ str(y1)+","+str(x)

		sleep(1)
		i-=1

def main():
	
		
	parser = argparse.ArgumentParser(description="Plot the graph of a DeterLab node characteristics againsts time")
	parser.add_argument("node", type=str, help="the name of the deterlab node to graph")
	parser.add_argument("time", type=int, help="the number of seconds to poll the node for stats.")#, default=60)
	args = parser.parse_args()
	
	host=args.node
	time=args.time
	
	task(host,time)
	

if __name__ == "__main__":
	main()
