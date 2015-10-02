#!/usr/bin/python
import argparse
import subprocess
import datetime
import time as tm
from time import sleep
import argparse


def sshwithcmd(node,command):
        '''function for sshing into a node to run  a command which might include executing
        a script. Both node and scriptpath are string variables'''
        cmd=str(command)
        host=str(node)
        p=subprocess.Popen(["ssh", "%s" % host, cmd], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (output, err) = p.communicate()
        return output,err

def task(host,time):
	command="bash ~/DeterlabControl/nodecontrol/bashgraph.sh %d"%(time)
        output,err=sshwithcmd(host,command)
#        print output
	#print err
        print output, host.split(".")[0]

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