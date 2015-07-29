#!/usr/bin/python
import subprocess
import argparse
import sshwithcmd
import matplotlib.pyplot as plt
import numpy as np
import ast
import matplotlib.animation as animation
import datetime


def animate():

	x1=[]
	y1=[]
	y2=[]
	ax1=plt.subplot2grid((1,1),(0,0),rowspan=1,colspan=1)
	#ax2=plt.subplot2grid((2,1),(1,0),rowspan=1,colspan=1)
	plt.xlabel('TimeStamp')
	plt.ylabel('Number of Bytes Received              Number of Bytes Transmitted')
	#ax2.set_ylabel('Number of Bytes Received (bytes)')
	

	graph_data=open('DeterlabControl/nodecontrol/statdata.txt','r').read()
	lines=graph_data.split('\n')
	
	#y1=ast.literal_eval(lines[0])     	# ast.literal_eval changes string of list to list
	#y2=ast.literal_eval(lines[1])		# ast.literal_eval changes string of list to list
	#x=lines[1]#ast.literal_eval(lines[1])		# ast.literal_eval changes string of list to list
	#x=[datetime.datetime.strptime(lines[1],"%a %b %d %H:%M:%S %Y")]
	#y2=[int("-"+str(i)) for i in y2]
	for line in lines:
		if len(line)>1:
			y,y0,x=line.split(",")
			# print y, type(y)
			# print y0, type(y0)
			# print x, type(x)

			x1.append(datetime.datetime.strptime(x,"%a %b %d %H:%M:%S %Y"))
			y1.append(int(y))
			y2.append(int("-"+y0))
	

	if (y1[0] and y1[2])==0:
		y1[1]=0

	if (y2[0] and y2[2])==0:
		y2[1]=0

	# print y1, type(y1)
	# print y2, type(y2)
	# print x1, type(x1)


	y1=np.array(y1)
	y2=np.array(y2)
	x1=np.array(x1)
	# print y1,x
	# ax1.clear()
	# # #ax2.clear()
	
	ax1.plot(x1,y1)
	ax1.plot(x1,y2)

	#ax2.plot(x1,y2)
	
	ax1.grid(True)
	#ax2.grid(True)

	ax1.fill_between(x1,min(y1),y1,facecolor='green')#,alpha=0.3)
	ax1.fill_between(x1,max(y2),y2,facecolor='green',alpha=0.5)
	plt.show()

def main():

	parser = argparse.ArgumentParser(description="Plot the graph of a DeterLab node characteristics againsts time")
	parser.add_argument("username", type=str, help="your deterlab username")
	parser.add_argument("node", type=str, help="the name of the deterlab node to graph")
	parser.add_argument("time", type=int, help="the number of seconds to poll the node for stats.")#, default=60)
	args = parser.parse_args()
	
	agent=args.username + "@users.isi.deterlab.net"
	host=args.node
	time=args.time
	cmd="python DeterlabControl/nodecontrol/graphclient.py %s %d"%(host,time)

	output, error= sshwithcmd.sshwithcmd(agent, cmd)
	#print (output)
	#print (error)

	fig =plt.figure()
	plt.suptitle('Bandwidth Utilization for %s'%(host.split(".")[0]),size=16)


	myfile1 = open('DeterlabControl/nodecontrol/statdata.txt', 'w')
	myfile1.write(output)
	myfile1.close()
	#ani=animation.FuncAnimation(fig,animate,interval=1000)
	animate()





	
if __name__ == "__main__":
	main()



