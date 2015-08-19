#this file is used to compile the demo codes under deterlab
#Note this corrects the problem with the segfault (core dumped) probelm.

echo "Welcome to the DemoEditor"
echo
echo "do you want to edit master or outstation? m for master and o for outstation."
read answer
echo
if [ "$answer" == "m" ]; then
    cd /tmp/dnp3/
    git checkout 2.0.1
    sudo nano cpp/examples/master/DemoMain.cpp    
    g++ --std=c++11 -o cpp/examples/master/DemoMain cpp/examples/master/DemoMain.cpp -lopendnp3 -lasiodnp3 -lopenpal -lasiopal -Icpp/libs/asiodnp3/src/ -Icpp/libs/asiopal/src/ -Icpp/libs/opendnp3/src/ -Icpp/libs/openpal/src/ -I/users/oigbe000/asio/asio/include -pthread -DASIO_STANDALONE -Wl,--no-as-needed
    echo "Done..."
    echo "want to execute code? y for YES or n for NO"
    read answer1
    if [ "$answer1" == "y" ]; then
        cpp/examples/master/DemoMain
    else
        echo "Exiting..."
    fi
else
    cd /tmp/dnp3/
    git checkout 2.0.1
    sudo nano cpp/examples/outstation/DemoMain.cpp
    g++ --std=c++11 -o cpp/examples/outstation/DemoMain cpp/examples/outstation/DemoMain.cpp -lopendnp3 -lasiodnp3 -lopenpal -lasiopal -Icpp/libs/asiodnp3/src/ -Icpp/libs/asiopal/src/ -Icpp/libs/opendnp3/src/ -Icpp/libs/openpal/src/ -I/users/oigbe000/asio/asio/include -pthread -DASIO_STANDALONE -Wl,--no-as-needed
    echo "Done..."
    echo "want to execute code? y for YES or n for NO"
    read answer2
    if [ "$answer2" == "y" ]; then
        cpp/examples/outstation/DemoMain
    else
        echo "Exiting..."
    fi
fi
