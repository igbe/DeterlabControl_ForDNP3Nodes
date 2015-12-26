#!/bin/bash

cd
sudo apt-get update
sudo apt-get install autoconf libtool g++ git libssl-dev -y

if [ ! -d ~/asio ]; then
        yes | git clone https://github.com/chriskohlhoff/asio.git
fi

cd asio
git checkout -b asio asio-1-10-3
cd ~/
export ASIO_HOME=~/asio/asio/include
echo "export ASIO_HOME=~/asio/asio/include" >> .bashrc

source ~/.bashrc; echo "ASIO_HOME set to: $ASIO_HOME"
echo $ASIO_HOME

cd
if [ ! -d ~/cmake-3.2.3 ]; then
        wget https://cmake.org/files/v3.2/cmake-3.2.3.tar.gz
	tar xzf cmake-3.2.3.tar.gz
	cd cmake-3.2.3
	./configure --prefix=/opt/cmake
	make
	sudo make install

	#Verification:After installation without any errors you can verify the installation by running the command below:
	/opt/cmake/bin/cmake -version

	#The output should look something like below (depending upon cmake version you are installing).
	#cmake version 3.2.3
cd

if [ ! -d ~/dnp3 ]; then
        yes | git clone https://github.com/automatak/dnp3.git
fi
echo "going inside dnp3 folder..."

cd dnp3
echo "running cmake..."
/opt/cmake/bin/cmake -DCMAKE_INSTALL_PREFIX=/usr -DDEMO=ON -DSECAUTH=ON -DASIO_HOME=~/asio/asio/include && make -j && sudo make install
echo "done with installation"

