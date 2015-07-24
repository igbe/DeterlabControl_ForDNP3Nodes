#!/bin/bash

echo "do you want to install opendnp3 library or have you done that before. input y for yes and n for no:"
read INPUT
if [ "$INPUT" = "y" ]; then

	echo "Getting required libraries..."
	sudo apt-get update
	sudo apt-get install build-essential g++ python-dev autotools-dev libicu-dev libbz2-dev autoconf libtool automake m4 swig
	echo "Copying boost to temp folder..."
	sudo cp -a boost_1_47_0.tar.gz /tmp
	cd /tmp
	echo "installing the boost..."
	tar xvfz boost_1_47_0.tar.gz
	cd boost_1_47_0
	./bootstrap.sh --prefix=/usr

	
	sudo ./bjam install
	#copying the dnp3 folder which was copied from your remote system, but you would have used wget
	echo "Copying the dnp3 folder from your home folder..."
	cd
	sudo cp -a dnp3 /tmp
	cd /tmp/dnp3
	echo "Installign the c++ library..."
	autoreconf -f -i
	#./configure (i changed the line below)
	./configure --with-boost=/usr/include --with-boost-libdir=/usr/lib
	sudo make
	sudo make install
	sudo make check
	
	echo "Done with the c++ library setup"
else
	echo "ok am done..."
	
fi

