#!/bin/bash

import subprocess

p=subprocess.Popen(["rm", "/tmp/nodelist.txt"],shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

y=subprocess.Popen(["node_list", "-v", "-e", "TCPFlooding,Grid"],shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(output1, err1) = y.communicate()

#print output

f = open('/tmp/nodelist.txt','w')

nodes=output1.rsplit("  ")


nodes.remove('control ')
nodes.remove('\n')

#print nodes

for i in nodes:
	f.write((str(i)+"\n")) # python will convert \n to os.linesep
f.close()
m=subprocess.Popen(["cat", "/tmp/nodelist.txt"],shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

(output2, err2) = m.communicate()

print output2
