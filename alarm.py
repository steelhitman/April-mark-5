import speech_recognition as sr
import mp3play
from mutagen.mp3 import MP3
import sys
from time import ctime
import time
import os
from gtts import gTTS

import datetime
text=""
try:
    fp=open("command_alarm.txt",'r')
    for line in fp:
        text=line
    fp.close
except:
    pass
if text=="":
    mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"
    sample_rate = 48000
    chunk_size = 2048

    r = sr.Recognizer()
     
    mic_list = sr.Microphone.list_microphone_names()

    device_id = 0

    for i, microphone_name in enumerate(mic_list):
        if microphone_name == mic_name:
            device_id = i
    while True:
        with sr.Microphone(device_index = device_id, sample_rate = sample_rate, chunk_size = chunk_size) as source:
            r.adjust_for_ambient_noise(source)
            print "say alarm time..."
            
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print "you said: " + text
            except:
                pass
            if text!="":
                break
    text=text.lower()
    print text
    text=text.split(' ')
    print text
    global hr
    global mins
    if "o" in text[1]:
        hr= text[0]
        mins=text[2]
    else:
        t=text[0]
        t=t.split(":")
        hr=t[0]
        try:
            mins=t[1]
        except:
            mins="00"
        
    if text[1]=="a.m." or text[1]=="a.m" :
        if hr=="12":
            hr=str(int(hr)-12)
    elif text[1]=="p.m." or text[1]=="p.m":
        hr=str(int(hr)+12)
    print hr,mins
    while True:
        rn = str(datetime.datetime.now().time())
        rn=rn.split(":")
        hr1=rn[0]
        mins1=rn[1]
        print hr,mins,"     ",hr1,mins1
        if int(hr)==int(hr1) and int(mins)==int(mins1):
            print "alarm"
            break

    for i in range(0,2):
        f="alarm_tone.mp3"
        audio = MP3(f)
        length=audio.info.length    
        clip = mp3play.load(f)
        clip.play()
        time.sleep(length)
        clip.stop()
    print "alarm off"
else:
    text=text.lower()
    print text
    text=text.split(' ')
    print text
    global hr
    global mins
    if "o" in text[1]:
        hr= text[0]
        mins=text[2]
    else:
        t=text[0]
        t=t.split(":")
        hr=t[0]
        try:
            mins=t[1]
        except:
            mins="00"
        
    if text[1]=="a.m." or text[1]=="a.m" :
        if hr=="12":
            hr=str(int(hr)-12)
    elif text[1]=="p.m." or text[1]=="p.m":
        hr=str(int(hr)+12)
    print hr,mins
    while True:
        rn = str(datetime.datetime.now().time())
        rn=rn.split(":")
        hr1=rn[0]
        mins1=rn[1]
        print hr,mins,"     ",hr1,mins1
        if int(hr)==int(hr1) and int(mins)==int(mins1):
            print "alarm"
            break

    for i in range(0,2):
        f="alarm_tone.mp3"
        audio = MP3(f)
        length=audio.info.length    
        clip = mp3play.load(f)
        clip.play()
        time.sleep(length)
        clip.stop()
    print "alarm off"




