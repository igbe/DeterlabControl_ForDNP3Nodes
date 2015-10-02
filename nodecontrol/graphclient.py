#!/usr/bin/python
import subprocess		#this module is similar to sys used to parse commands to the sys
import argparse			# this is used to pick up the arguments supplied to an excuted script



def getdata(host,time):
        cmd="python ~/DeterlabControl/nodecontrol/graphtest.py %s %d & python ~/DeterlabControl/nodecontrol/graphtest.py %s %d & python ~/DeterlabControl/nodecontrol/graphtest.py %s %d & python ~/DeterlabControl/nodecontrol/graphtest.py %s %d" %(host[0],time,host[1],time,host[2],time, host[3],time)
        p=subprocess.Popen([cmd], shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        (output, err) = p.communicate()
        print output,err
        #return output






def main():

	parser = argparse.ArgumentParser(description="Plot the graph of a DeterLab node characteristics againsts time")
	#parser.add_argument("username", type=str, help="your deterlab username")
	parser.add_argument("node1", type=str, help="the name of the 1st deterlab node to graph e.g master")
	parser.add_argument("node2", type=str, help="the name of the 2nd deterlab node to graph e.g oustation")
	parser.add_argument("node3", type=str, help="the name of the 3rd deterlab node to graph e.g attacker")
	parser.add_argument("node4", type=str, help="the name of the 4th deterlab node to graph e.g control")
	parser.add_argument("time", type=int, help="the number of seconds to poll the node for stats.")#, default=60)
	args = parser.parse_args()
	
	
	host=["%s.grid.tcpflooding"%(args.node1),"%s.grid.tcpflooding"%(args.node2),"%s.grid.tcpflooding"%(args.node3),"%s.grid.tcpflooding"%(args.node4)]
	time=args.time
	getdata(host,time)

if __name__ == "__main__":
        main()
	

