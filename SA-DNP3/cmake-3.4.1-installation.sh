wget https://cmake.org/files/v3.4/cmake-3.4.1.tar.gz
tar xzf cmake-3.4.1.tar.gz
cd cmake-3.4.1
./configure --prefix=/opt/cmake
make
make install

#Verification:After installation without any errors you can verify the installation by running the command below:
/opt/cmake/bin/cmake -version

#The output should look something like below (depending upon cmake version you are installing).
#cmake version 3.4.1
