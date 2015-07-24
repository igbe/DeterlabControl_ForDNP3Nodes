#!/bin/bash

import subprocess
import random

my_node_list=["outstation1.Grid.TCPFlooding","outstation2.Grid.TCPFlooding","outstation3.Grid.TCPFlooding","outstation4.Grid.TCPFlooding","master.Grid.TCPFlooding","attacker.Grid.TCPFlooding"]

ip=["10.1.1.2","10.1.1.3","10.1.1.4","10.1.1.5","10.1.1.6","10.1.1.7"]


while (1):
	for i in my_node_list:
		j=random.choice(ip)
		command="ping %s -c 2"%(j)
		host="%s"%(i)

		print "pinging %s"%(i.rsplit(".")[0])
		p=subprocess.Popen(["ssh", "%s" % host, command], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

		(output, err) = p.communicate()
		#print output
