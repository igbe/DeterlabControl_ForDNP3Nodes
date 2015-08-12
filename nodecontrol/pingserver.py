#!/usr/bin/python
import sshwithcmd
import subprocess
import random


def main():
	cmd="python /users/oigbe000/DeterlabControl/nodecontrol/pingclient.py"#./DeterlabControl/nodecontrol/pingclient.py"
	output,err=sshwithcmd.sshwithcmd("oigbe000@users.isi.deterlab.net",cmd)
	print output
	print err
	print "server is ok"

if __name__ == "__main__":
	main()
# p=subprocess.Popen(["python", file1], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# f = open('/tmp/nodelist.txt','r')
# for i in f.readlines():
# 	print i