#!/bin/bash
cd ~/

sudo apt-get install autoconf libtool g++ git -y

cd asio
git checkout -b asio asio-1-10-3
cd ~/
export ASIO_HOME=/users/oigbe000/asio/asio/include
echo "export ASIO_HOME=/users/oigbe000/asio/asio/include" >> .bashrc


