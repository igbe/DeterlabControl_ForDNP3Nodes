#!/usr/bin/python
import sshwithcmd

def main():
	cmd="python /users/oigbe000/DeterlabControl/nodecontrol/pingclient.py"#./DeterlabControl/nodecontrol/pingclient.py"
	output,err=sshwithcmd.sshwithcmd("oigbe000@users.isi.deterlab.net",cmd)
	print output
	print err
	print "server is ok"

if __name__ == "__main__":
	main()
