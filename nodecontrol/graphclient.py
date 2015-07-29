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

def main():
	parser = argparse.ArgumentParser(description="Plot the graph of a DeterLab node characteristics againsts time")
	parser.add_argument("node", type=str, help="the name of the deterlab node to graph")
	parser.add_argument("time", type=int, help="the number of seconds to poll the node for stats.")#, default=60)
	args = parser.parse_args()
	
	host=args.node
	time=args.time

	command="cat /sys/class/net/eth0/statistics/tx_bytes"
	command1="ip route get 10.1.1.1 | cut -b 14-17"

	output,err=sshwithcmd(host,command)
	output1,err=sshwithcmd(host,command1)

	print output
	print output1

if __name__ == "__main__":
	main()
