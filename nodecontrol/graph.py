#!/usr/bin/python
import subprocess
import argparse
import sshwithcmd
def main():

	parser = argparse.ArgumentParser(description="Plot the graph of a DeterLab node characteristics againsts time")
	#group = parser.add_mutually_exclusive_group()
	#group.add_argument("-v", "--verbose", action="store_true")
	#group.add_argument("-q", "--quiet", action="store_true")
	parser.add_argument("username", type=str, help="your deterlab username")
	parser.add_argument("node", type=str, help="the name of the deterlab node to graph")
	parser.add_argument("time", type=int, help="the number of seconds to poll the node for stats.")#, default=60)
	args = parser.parse_args()
	
	agent=args.username + "@users.isi.deterlab.net"
	host=args.node
	time=args.time
	cmd="python DeterlabControl/nodecontrol/graphclient.py %s %d"%(host,time)

	output, error= sshwithcmd.sshwithcmd(agent, cmd)
	print (output)
	print (error)
	
if __name__ == "__main__":
	main()



