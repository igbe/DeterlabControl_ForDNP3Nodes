#!/bin/bash
cd ~/
if [ ! -d ~/asio ]; then
	yes | git clone https://github.com/chriskohlhoff/asio.git
		
fi

cd /tmp
if [ ! -d ~/dnp3 ]; then

	yes | git clone https://github.com/automatak/dnp3.git
fi
cd ~/
python DeterlabControl/nodecontrol/nodes.py  #to create a file /tmp/nodelist.txt that will contain list of exp. nodes
while read line; do
    ssh $line.Grid.TCPFlooding 'bash -s' < ~/DeterlabControl/dnpv2install/dnp3v2install1.sh
    ssh $line.Grid.TCPFlooding 'source ~/.bashrc; echo "ASIO_HOME set to: $ASIO_HOME"'
    ssh $line.Grid.TCPFlooding 'bash -s' < ~/DeterlabControl/dnpv2install/dnp3v2install2.sh
done < /tmp/nodelist.txt
