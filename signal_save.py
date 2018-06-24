import os
import time
def wifi_networks(x):
    os.system("python wifi_test_signal.py>signals.txt")
    #var=raw_input()
    fp=open('signals.txt','r')
    c=0
    signal=[]
    networks=[]
    for line in fp:
        if "Profile Name" in line:
            signal.append(line.strip(" ").split(':')[1])
        elif "SSID" in line and "BSSID" not in line:
            signal[c]=signal[c]+"$"+line.strip(" ").split(':')[1]
        elif "Signal Quality" in line:
            signal[c]=signal[c]+"$"+line.strip(" ").split(':')[1]
        elif "--------------------" in line:
            c=c+1
    #for s in signal:
    #    print s
    signal=set(signal)
    for s in signal:
        data=s.split("$")
        #print data[1].strip("\n"),data[2].strip("\n")
    filter_signal=x
    max_strength=0
    for s in signal:
        data=s.split("$")
        d=data[2].strip("\n")
        d=d.strip("%")
        if int(d)>max_strength:
           max_strength=int(d)
    #print "Max_strength: ", max_strength
    c=0
    while True:
        for s in signal:
            data=s.split("$")
            d=data[2].strip("\n")
            d=d.strip("%")
            if int(d)==max_strength:
                #print data[1].strip("\n")
                networks.append(data[1].strip("\n"))
                c=c+1
            if c>=int(filter_signal):
                break
        max_strength=max_strength-1
        if c>=int(filter_signal):
                break
    #print networks
    return networks

    
