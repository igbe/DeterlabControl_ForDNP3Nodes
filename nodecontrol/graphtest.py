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
        command1="ip route get 10.1.1.1 | cut -b 14-17; rm ~/DeterlabControl/nodecontrol/*data.txt"
        output1,err=sshwithcmd(host,command1)
        #print err
        i=0
        prev=[0,0]
        #finaldata=[]
        test=""
        while i < time:
                command="cat /sys/class/net/%s/statistics/tx_bytes; cat /sys/class/net/%s/statistics/rx_bytes; sleep 1; cat /sys/class/net/%s/statistics/tx_bytes; cat /sys/class/net/%s/statistics/rx_bytes"%(output1[0:4],output1[0:4],output1[0:4],output1[0:4])

                x=tm.ctime()
                output,err=sshwithcmd(host,command)
                #t1,r1,t2,r2,n=output.split("\n")

                val=output.split("\n")
                #print val
                #print prev
                #print str(int(val[2])-int(val[0]))+","+str(int(val[3])-int(val[1]))
                if i>=1:
                        data=str(int(val[0])-int(prev[0]))+","+str(int(val[1])-int(prev[1]))+","+str(x)+"\n"  

                        #finaldata.append(data)
                        test=test+data
                        prev[0]=val[2]
                        prev[1]=val[3]
                else:
                        prev[0]=val[2]
                        prev[1]=val[3]


                i=i+1
        #print finaldata
        print test
        print host.split(".")[0]

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