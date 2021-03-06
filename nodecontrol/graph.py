#!/usr/bin/python
import subprocess		#this module is similar to sys used to parse commands to the sys
import argparse			# this is used to pick up the arguments supplied to an excuted script
import sshwithcmd		# a module i wrote to make ssh connections to a remote node
import matplotlib.pyplot as plt  #module for the graphing
import numpy as np
import matplotlib.animation as animation
import datetime			#module for timing
from matplotlib import dates
import random
def animate(val,name):
	#print val
	x1=[]
	y1=[]
	y11=[]

	x2=[]
	y2=[]
	y22=[]

	x3=[]
	y3=[]
	y33=[]

	x4=[]
	y4=[]
	y44=[]
	
	ax1 = plt.subplot2grid((2,2),(0,0))#,rowspan=1,colspan=1)     # create a subplot which will be a 1X1
	ax2 = plt.subplot2grid((2,2), (0,1))
	ax3 = plt.subplot2grid((2,2), (1,0))
	ax4 = plt.subplot2grid((2,2), (1,1))

	ax1.set_title(name[0])
	ax2.set_title(name[1])
	ax3.set_title(name[2])
	ax4.set_title(name[3])
	
	#plt.xticks(rotation='vertical')
	
	ax1.set_xticklabels([])
	ax2.set_xticklabels([])
	ax3.set_xticklabels([])
	ax4.set_xticklabels([])
	#plt.subplots_adjust(bottom=.3)	

	#plt.xlabel('TimeStamp')
	#plt.ylabel('Number of Received bytes/sec              Number of Transmitted bytes/sec')
	#print val		

	# graph_data=open('statdata.txt','r').read()    # read data from DeterlabControl/nodecontrol/statdata.txt  which is the text file that holds the stats information gotten from the remote node
	# lines=graph_data.split('\n')	#split the lines in the txt file...this will create a list containing all of the lines in the txt file
	# for line in lines:
	# 	if len(line)>1:
	# 		y,y0,x=line.split(",")   #since the list item created above consist of y1,y2, and x we split this variables based on a dilimiter which is ','  
			
	# 		x1.append(datetime.datetime.strptime(x,"%a %b %d %H:%M:%S %Y")) #conert x which is the timestamp to a plottable values using the datetime.strptime. Note %a means abbreviated week example Wed,%b means abbreviated month example july, %d means number day , %H means hours, %M means minute, %S means seconds and %Y means year.
	# 		y1.append(int(y))   # created a list of integers gotten by converting the string values in y
	# 		y2.append(int("-"+y0)) # created a list of integers gotten by converting the string values in y0 but this time append '-' to it. This is to ensure that it is plotted reversed 
	i=0
	while i<4:
		
		if i==0:
			for j in val[0]:
				y,y0,x=j.split(",")   #since the list item created above consist of y1,y2, and x we split this variables based on a dilimiter which is ','  
				x1.append(datetime.datetime.strptime(x,"%a %b %d %H:%M:%S %Y")) #conert x which is the timestamp to a plottable values using the datetime.strptime. Note %a means abbreviated week example Wed,%b means abbreviated month example july, %d means number day , %H means hours, %M means minute, %S means seconds and %Y means year.
				y1.append(int(y))   # created a list of integers gotten by converting the string values in y
				y11.append(int("-"+y0)) # created a list of integers gotten by converting the string values in y0 but this time append '-' to it. This is to ensure that it is plotted reversed 	
		if i==1:
			for j in val[1]:
				y,y0,x=j.split(",")   #since the list item created above consist of y1,y2, and x we split this variables based on a dilimiter which is ','  
				x2.append(datetime.datetime.strptime(x,"%a %b %d %H:%M:%S %Y")) #conert x which is the timestamp to a plottable values using the datetime.strptime. Note %a means abbreviated week example Wed,%b means abbreviated month example july, %d means number day , %H means hours, %M means minute, %S means seconds and %Y means year.
				y2.append(int(y))   # created a list of integers gotten by converting the string values in y
				y22.append(int("-"+y0)) # created a list of integers gotten by converting the string values in y0 but this time append '-' to it. This is to ensure that it is plotted reversed 	
		if i==2:
			for j in val[2]:
				y,y0,x=j.split(",")   #since the list item created above consist of y1,y2, and x we split this variables based on a dilimiter which is ','  
				x3.append(datetime.datetime.strptime(x,"%a %b %d %H:%M:%S %Y")) #conert x which is the timestamp to a plottable values using the datetime.strptime. Note %a means abbreviated week example Wed,%b means abbreviated month example july, %d means number day , %H means hours, %M means minute, %S means seconds and %Y means year.
				y3.append(int(y))   # created a list of integers gotten by converting the string values in y
				y33.append(int("-"+y0)) # created a list of integers gotten by converting the string values in y0 but this time append '-' to it. This is to ensure that it is plotted reversed 	
		if i==3:
			for j in val[3]:
				y,y0,x=j.split(",")   #since the list item created above consist of y1,y2, and x we split this variables based on a dilimiter which is ','  
				x4.append(datetime.datetime.strptime(x,"%a %b %d %H:%M:%S %Y")) #conert x which is the timestamp to a plottable values using the datetime.strptime. Note %a means abbreviated week example Wed,%b means abbreviated month example july, %d means number day , %H means hours, %M means minute, %S means seconds and %Y means year.
				y4.append(int(y))   # created a list of integers gotten by converting the string values in y
				y44.append(int("-"+y0)) # created a list of integers gotten by converting the string values in y0 but this time append '-' to it. This is to ensure that it is plotted reversed 				
		i+=1
	#print y1
	#print y2
	#print x1
	
	r=[]
	r.append(len(x1))
	r.append(len(x2))
	r.append(len(x3))
	r.append(len(x4))
	k=r
	k.sort()
	#r.sort()
	m=r.index(min(r))
	if (r[m])!=(k[1]):
		print "running modification for less"
		u={0:x1,1:x2,2:x3,3:x4}
		u0={0:y1,1:y2,2:y3,3:y4}
		u00={0:y11,1:y22,2:y33,3:y44}
		L=len(u[0])-r[m]
		u1={0:x1,1:x2,2:x3,3:x4}
		u2={0:y1,1:y2,2:y3,3:y4}
		u3={0:y11,1:y22,2:y33,3:y44}

		u.pop(m)
		u0.pop(m)
		u00.pop(m)
		f=[0,1,2,3]
		f.pop(m)
		q=random.choice(f)
		for i in range(r[m],len(u[q])):
			u1[m].append(u[q][i])
			u2[m].append(0)#u0[q][i])
			u3[m].append(0)#u00[q][i])




#to convert the lists y1,y2 and x1 to an array. this is only necessary cause we want to fill some sections of it with color. else plotting the list without
# converting to np.array will work too but can only be used to line plots without fill. Note also, that if the timestamp(x) was a normal value, then we also
# dont need np.array to use fill inbetween below

	y1=np.array(y1)
	y11=np.array(y11)
	x1=np.array(x1)

	y2=np.array(y2)
	y22=np.array(y22)
	x2=np.array(x2)

	y3=np.array(y3)
	y33=np.array(y33)
	x3=np.array(x3)

	y4=np.array(y4)
	y44=np.array(y44)
	x4=np.array(x4)
	
#plot both transmitted bytes (y1) and received bytes (y2) on the same graph against time
	ax1.plot(x1,y1)
	ax1.plot(x1,y11)

	ax2.plot(x2,y2)
	ax2.plot(x2,y22)

	ax3.plot(x3,y3)
	ax3.plot(x3,y33)

	ax4.plot(x4,y4)
	ax4.plot(x4,y44)

# enable the grid
	ax1.grid(True)
	ax2.grid(True)
	ax3.grid(True)
	ax4.grid(True)
#Add x and y label
	#ax1.set_xlabel('Timestamp')
	ax1.set_ylabel('Bandwidth in bytes/s')

	#ax2.set_xlabel('Timestamp')
	ax2.set_ylabel('Bandwidth in bytes/s')

	#ax3.set_xlabel('Timestamp')
	ax3.set_ylabel('Bandwidth in bytes/s')

	#ax4.set_xlabel('Timestamp')
	ax4.set_ylabel('Bandwidth in bytes/s')

# fill between the minimum value of y1, and all values of y1, the fill bewteen the maximum value of y2 (maximum cause y2 is inverted hence, its minimum becomes its maximum)
# use dark green (no alpha value) for the tx 
	ax1.fill_between(x1,0,y1,facecolor='green',alpha=0.5)
	ax1.fill_between(x1,0,y11,facecolor='blue',alpha=0.5)

	ax2.fill_between(x2,0,y2,facecolor='green',alpha=0.5)
	ax2.fill_between(x2,0,y22,facecolor='blue',alpha=0.5)

	ax3.fill_between(x3,0,y3,facecolor='green',alpha=0.5)
	ax3.fill_between(x3,0,y33,facecolor='blue',alpha=0.5)

	ax4.fill_between(x4,0,y4,facecolor='green',alpha=0.5)
	ax4.fill_between(x4,0,y44,facecolor='blue',alpha=0.5)
	
	plt.show()
def getdata(out):
	L=len(out)
	i=0
	data=[]
	name=[]
	nodes=['master','outstation1','outstation2','outstation3','outstation4', 'attacker']
	prev=0
	while i < L:
		#print i
		if out[i] in nodes:
			data.append(out[prev:i])
			name.append(out[i])
			prev=i+1
			i+=1
			#print "seen empty space" 
			#print 'out[i-1] is ',out[i-1],'out[i] is ',out[i],'out[i+1] is ',out[i+1]
		else:
			i+=1
	#data.remove([])
	#name.remove('')
	#print data
	#print name	
	return data,name


k=0
def main():
	global k
	parser = argparse.ArgumentParser(description="Plot the graph of a DeterLab node characteristics againsts time")
	#parser.add_argument("username", type=str, help="your deterlab username")
	parser.add_argument("node1", type=str, help="the name of the 1st deterlab node to graph")
	parser.add_argument("node2", type=str, help="the name of the 2nd deterlab node to graph")
	parser.add_argument("node3", type=str, help="the name of the 3rd deterlab node to graph")
	parser.add_argument("node4", type=str, help="the name of the 4th deterlab node to graph")
	parser.add_argument("time", type=int, help="the number of seconds to poll the node for stats.")#, default=60)
	args = parser.parse_args()
	
	agent="oigbe000@users.isi.deterlab.net"
	
	host1=args.node1
	host2=args.node2
	host3=args.node3
	host4=args.node4
	time=args.time
	cmd="python ~/DeterlabControl/nodecontrol/graphclient.py %s %s %s %s %d"%(host1,host2,host3,host4,time)
	output, error= sshwithcmd.sshwithcmd(agent, cmd)
	#out=['87,158,Tue Oct 06 10:40:08 2015', '0,0,Tue Oct 06 10:40:09 2015', '87,158,Tue Oct 06 10:40:10 2015', '0,0,Tue Oct 06 10:40:11 2015', '87,158,Tue Oct 06 10:40:12 2015','87,158,Tue Oct 06 10:40:13 2015', '93,155,Tue Oct 06 10:40:14 2015', '87,158,Tue Oct 06 10:40:15 2015', '0,0,Tue Oct 06 10:40:16 2015', '87,158,Tue Oct 06 10:40:17 2015', '0,0,Tue Oct 06 10:40:18 2015', '87,158,Tue Oct 06 10:40:20 2015', '0,0,Tue Oct 06 10:40:21 2015', '87,158,Tue Oct 06 10:40:22 2015', '0,0,Tue Oct 06 10:40:23 2015','87,158,Tue Oct 06 10:40:24 2015', '140,70,Tue Oct 06 10:40:25 2015', '0,0,Tue Oct 06 10:40:26 2015', 'outstation1', '0,0,Tue Oct 06 10:40:08 2015', '0,0,Tue Oct 06 10:40:09 2015', '0,0,Tue Oct 06 10:40:10 2015', '0,0,Tue Oct 06 10:40:11 2015', '0,0,Tue Oct 06 10:40:12 2015', '0,0,Tue Oct 06 10:40:13 2015', '0,0,Tue Oct 06 10:40:15 2015','0,0,Tue Oct 06 10:40:16 2015', '0,0,Tue Oct 06 10:40:17 2015', '0,0,Tue Oct 06 10:40:18 2015', '0,0,Tue Oct 06 10:40:19 2015', '0,0,Tue Oct 06 10:40:20 2015', '0,0,Tue Oct 06 10:40:21 2015', '0,0,Tue Oct 06 10:40:22 2015', '0,0,Tue Oct 06 10:40:23 2015', '0,0,Tue Oct 06 10:40:24 2015', '0,0,Tue Oct 06 10:40:25 2015', '0,0,Tue Oct 06 10:40:26 2015', '0,0,Tue Oct 06 10:40:27 2015', '0,0,Tue Oct 06 10:40:28 2015', '0,0,Tue Oct 06 10:40:29 2015', '0,0,Tue Oct 06 10:40:30 2015', '0,0,Tue Oct 06 10:40:31 2015', '0,0,Tue Oct 06 10:40:32 2015', '0,0,Tue Oct 06 10:40:33 2015', '0,0,Tue Oct 06 10:40:34 2015', '0,0,Tue Oct 06 10:40:35 2015', '0,0,Tue Oct 06 10:40:36 2015', '0,0,Tue Oct 06 10:40:37 2015', '0,0,Tue Oct 06 10:40:38 2015', 'outstation2', '0,0,Tue Oct 06 10:40:08 2015', '158,87,Tue Oct 06 10:40:09 2015', '0,0,Tue Oct 06 10:40:10 2015', '158,87,Tue Oct 06 10:40:11 2015', '0,0,Tue Oct 06 10:40:13 2015', '158,87,Tue Oct 06 10:40:14 2015', '155,93,Tue Oct 06 10:40:15 2015', '158,87,Tue Oct 06 10:40:16 2015', '0,0,Tue Oct 06 10:40:17 2015', '158,87,Tue Oct 06 10:40:18 2015', '0,0,Tue Oct 06 10:40:19 2015', '158,87,Tue Oct 06 10:40:20 2015', '0,0,Tue Oct 06 10:40:21 2015', '158,87,Tue Oct 06 10:40:22 2015', '0,0,Tue Oct 06 10:40:23 2015', '158,87,Tue Oct 06 10:40:24 2015', '70,140,Tue Oct 06 10:40:25 2015', '0,0,Tue Oct 06 10:40:26 2015', '78,64,Tue Oct 06 10:40:27 2015', '0,0,Tue Oct 06 10:40:28 2015', '78,64,Tue Oct 06 10:40:29 2015', '0,0,Tue Oct 06 10:40:30 2015', '0,0,Tue Oct 06 10:40:31 2015', '0,0,Tue Oct 06 10:40:32 2015', '78,64,Tue Oct 06 10:40:33 2015', '0,0,Tue Oct 06 10:40:34 2015', '0,0,Tue Oct 06 10:40:35 2015', '0,0,Tue Oct 06 10:40:36 2015', '0,0,Tue Oct 06 10:40:37 2015','78,0,Tue Oct 06 10:40:38 2015', 'master', '0,0,Tue Oct 06 10:40:08 2015', '0,0,Tue Oct 06 10:40:09 2015', '0,0,Tue Oct 06 10:40:10 2015', '0,0,Tue Oct 06 10:40:12 2015', '0,0,Tue Oct 06 10:40:13 2015', '0,0,Tue Oct 06 10:40:14 2015', '0,0,Tue Oct 06 10:40:15 2015', '0,0,Tue Oct 06 10:40:16 2015', '0,0,Tue Oct 06 10:40:17 2015', '0,0,Tue Oct 06 10:40:18 2015', '0,0,Tue Oct 06 10:40:19 2015', '0,0,Tue Oct 06 10:40:20 2015', '0,0,Tue Oct 06 10:40:21 2015', '0,0,Tue Oct 06 10:40:22 2015', '0,0,Tue Oct 06 10:40:23 2015', '0,0,Tue Oct 06 10:40:24 2015', '0,0,Tue Oct 06 10:40:25 2015', '0,0,Tue Oct 06 10:40:26 2015', '0,0,Tue Oct 06 10:40:27 2015', '0,0,Tue Oct 06 10:40:28 2015', '0,0,Tue Oct 06 10:40:29 2015', '0,0,Tue Oct 06 10:40:30 2015', '0,0,Tue Oct 06 10:40:31 2015', '0,0,Tue Oct 06 10:40:32 2015', '0,0,Tue Oct 06 10:40:33 2015', '0,0,Tue Oct 06 10:40:34 2015', '0,0,Tue Oct 06 10:40:35 2015', '0,0,Tue Oct 06 10:40:36 2015', '0,0,Tue Oct 06 10:40:37 2015', '0,0,Tue Oct 06 10:40:38 2015', 'attacker', '', '']

	#print output
	out=output.split("\n")
	#print out
	
	#print out1
	data,name=getdata(out)
	# fig =plt.figure()
	#plt.suptitle('Bandwidth Utilization for %s'%(host.split(".")[0]),size=16)


	animate(data,name)


if __name__ == "__main__":
	main()




