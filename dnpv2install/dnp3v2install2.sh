#!/bin/bash

cd ~/
export ASIO_HOME=/users/oigbe000/asio/asio/include
echo $ASIO_HOME

echo "going inside dnp3 folder..."

cd dnp3

echo "running git checkout..."
git checkout 2.0.1

echo "running autoreconf part...."
sudo autoreconf -i -f && ./configure && make && sudo make install

echo "done with installation"


