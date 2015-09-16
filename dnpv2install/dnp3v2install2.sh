#!/bin/bash

cd ~/
export ASIO_HOME=/users/oigbe000/asio/asio/include
echo $ASIO_HOME

echo "going inside dnp3 folder..."
#cp -r dnp3 /tmp/
cd dnp3
#cd /tmp/dnp3

echo "running git checkout..."
#git checkout 2.0.1
git checkout --detach 2.0.x
echo "running cmake..."
#echo "running autoreconf part...."

/opt/cmake/bin/cmake -DCMAKE_INSTALL_PREFIX=/usr -DDEMO=ON && make -j && sudo make install

echo "done with installation"


