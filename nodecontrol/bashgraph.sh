#!/bin/bash

INTERVAL="1"  # update interval in seconds

if [ -z "$1" ]; then
        echo
        echo usage: $0 ["time in secs"]
        echo
        echo e.g. $0 3
        echo
        exit
fi

IF=`ip route get 10.1.1.1 | cut -b 14-17`
for i in {`seq 1 $1`}

do
        R1=`cat /sys/class/net/$IF/statistics/rx_bytes`
        T1=`cat /sys/class/net/$IF/statistics/tx_bytes`
        sleep $INTERVAL
        R2=`cat /sys/class/net/$IF/statistics/rx_bytes`
        T2=`cat /sys/class/net/$IF/statistics/tx_bytes`
        TBPS=`expr $T2 - $T1`
        RBPS=`expr $R2 - $R1`
        #TKBPS=`expr $TBPS / 1024`
        #RKBPS=`expr $RBPS / 1024`
        echo "$TBPS,$RBPS,`date +'%a %b %d %I:%M:%S %Y'`"
done
