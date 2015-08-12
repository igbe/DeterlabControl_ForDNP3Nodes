#!/usr/bin/python
import subprocess		#this module is similar to sys used to parse commands to the sys
import argparse			# this is used to pick up the arguments supplied to an excuted script
import sshwithcmd		# a module i wrote to make ssh connections to a remote node
import matplotlib.pyplot as plt  #module for the graphing
import numpy as np
import matplotlib.animation as animation
import datetime			#module for timing


def animate():

	x1=[]
	y1=[]
	y2=[]
	
	ax1=plt.subplot2grid((1,1),(0,0),rowspan=1,colspan=1)     # create a subplot which will be a 1X1
	plt.xlabel('TimeStamp')
	plt.ylabel('Number of Bytes Received              Number of Bytes Transmitted')
		

	graph_data=open('statdata.txt','r').read()    # read data from DeterlabControl/nodecontrol/statdata.txt  which is the text file that holds the stats information gotten from the remote node
	lines=graph_data.split('\n')	#split the lines in the txt file...this will create a list containing all of the lines in the txt file
	for line in lines:
		if len(line)>1:
			y,y0,x=line.split(",")   #since the list item created above consist of y1,y2, and x we split this variables based on a dilimiter which is ','  
			
			x1.append(datetime.datetime.strptime(x,"%a %b %d %H:%M:%S %Y")) #conert x which is the timestamp to a plottable values using the datetime.strptime. Note %a means abbreviated week example Wed,%b means abbreviated month example july, %d means number day , %H means hours, %M means minute, %S means seconds and %Y means year.
			y1.append(int(y))   # created a list of integers gotten by converting the string values in y
			y2.append(int("-"+y0)) # created a list of integers gotten by converting the string values in y0 but this time append '-' to it. This is to ensure that it is plotted reversed 
	
# To solve the problem where their is a spike in the early parts of your graph after the 0,0 plot. this bug is corrected for both y1 and y2
# we do this by checking if the 1st and 3rd item of the list is zero. If it is zero, then that means the second item ought to be zero too.

	if (y1[0] and y1[2])==0:  
		y1[1]=0

	if (y2[0] and y2[2])==0:
		y2[1]=0

#to convert the lists y1,y2 and x1 to an array. this is only necessary cause we want to fill some sections of it with color. else plotting the list without
# converting to np.array will work too but can only be used to line plots without fill. Note also, that if the timestamp(x) was a normal value, then we also
# dont need np.array to use fill inbetween below

	y1=np.array(y1)
	y2=np.array(y2)
	x1=np.array(x1)
	
#plot both transmitted bytes (y1) and received bytes (y2) on the same graph against time
	ax1.plot(x1,y1)
	ax1.plot(x1,y2)

# enable the grid
	ax1.grid(True)

# fill between the minimum value of y1, and all values of y1, the fill bewteen the maximum value of y2 (maximum cause y2 is inverted hence, its minimum becomes its maximum)
# use dark green (no alpha value) for the tx 
	ax1.fill_between(x1,min(y1),y1,facecolor='green')#,alpha=0.3)
	ax1.fill_between(x1,max(y2),y2,facecolor='green',alpha=0.5)
	
	plt.show()

def main():

	parser = argparse.ArgumentParser(description="Plot the graph of a DeterLab node characteristics againsts time")
	#parser.add_argument("username", type=str, help="your deterlab username")
	parser.add_argument("node", type=str, help="the name of the deterlab node to graph")
	parser.add_argument("time", type=int, help="the number of seconds to poll the node for stats.")#, default=60)
	args = parser.parse_args()
	
	agent="oigbe000@users.isi.deterlab.net"
	host=args.node
	time=args.time
	cmd="python DeterlabControl/nodecontrol/graphclient.py %s %d"%(host,time)

	output, error= sshwithcmd.sshwithcmd(agent, cmd)
	
	fig =plt.figure()
	plt.suptitle('Bandwidth Utilization for %s'%(host.split(".")[0]),size=16)


	myfile1 = open('statdata.txt', 'w')
	myfile1.write(output)
	myfile1.close()
	animate()


if __name__ == "__main__":
	main()



