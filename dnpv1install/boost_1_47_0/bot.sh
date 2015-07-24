#!/bin/bash

# Get the version of Boost that you require. This is for 1.54 but feel free to change or manually download yourself
#wget -O boost_1_55_0.tar.gz http://sourceforge.net/projects/boost/files/boost/1.55.0/boost_1_55_0.tar.gz/download
#tar xzvf boost_1_55_0.tar.gz
#cd boost_1_55_0/
# Now we are inside the boost directory we can get the installation script and execute it.
# NOTE: READ THE SCRIPT FIRST
#wget https://dl.dropbox.com/u/88131281/install_boost.sh
#chmod +x install_boost.sh
#./install_boost.sh
echo "Getting required libraries..."
sudo apt-get install build-essential g++ python-dev autotools-dev libicu-dev libbz2-dev
cd boost_1_47_0/
./bootstrap.sh --prefix=/usr/local

# pipe "using mpi ;" to the config file so that mpi is enabled
user_configFile=`find $PWD -name user-config.jam`
echo "using mpi ;" >> $user_configFile
# Build using maximum number of physical cores
n=`cat /proc/cpuinfo | grep "cpu cores" | uniq | awk '{print $NF}'`
 
# begin install
sudo ./b2 --with=all -j $n install
 
sudo ldconfig
cd /tmp
git clone https://github.com/gec/dnp3.git
cd dnp3
sudo apt-get install dh-autoreconf
sudo apt-get install autoconf
autoreconf -f -i
./configure --with-boost=/usr/include --with-boost-libdir=/usr/lib
make
