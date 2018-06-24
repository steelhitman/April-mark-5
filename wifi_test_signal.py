from __future__ import print_function
from WindowsWifi import getWirelessInterfaces
from WindowsWifi import getWirelessAvailableNetworkList
import os
import time

if __name__ == "__main__":
    #fp=open("signals.txt",'w')
    #fp.close()
    ifaces = getWirelessInterfaces()
    for iface in ifaces:
        #print(iface)
        guid = iface.guid
        networks = getWirelessAvailableNetworkList(iface)
        #print("")
        for network in networks:
            print (network)
            #fp.write(network)
            #fp.write("-"*20)
            print("-" * 20)
        #print("")
    #time.sleep(5)
    #var=raw_input()
