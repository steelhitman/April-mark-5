import speech_recognition as sr
import mp3play
from mutagen.mp3 import MP3
import sys
import time
from time import ctime
import time
import os
from gtts import gTTS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import control_volume as volume
import random
import signal_save as ss
    
def rest():
    tts = gTTS(text="If you need me, I'll be around", lang='en')
    tts.save("rest.mp3")
    f="rest.mp3"
    audio = MP3(f)
    length=audio.info.length
    clip = mp3play.load(f)
    clip.play()
    time.sleep(length)
    clip.stop()

    while True:
        with sr.Microphone(device_index = device_id, sample_rate = sample_rate, 
                                chunk_size = chunk_size) as source:
            try:
                r.adjust_for_ambient_noise(source,1)
                print "In silent Mode..."
        
                audio = r.listen(source)
                text = r.recognize_google(audio)
                text=text.lower()
                if text=="wake up april":
                    tts = gTTS(text="I am up", lang='en')
                    tts.save("wake.mp3")
                    f="wake.mp3"
                    audio = MP3(f)
                    length=audio.info.length
                    clip = mp3play.load(f)
                    clip.play()
                    time.sleep(length)
                    clip.stop()
                    break
                else:
                    pass
            except:
                pass

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    #os.system("start audio_out.py")

speak("It's a pleasure to have you back")
f="audio.mp3"
audio = MP3(f)
length=audio.info.length
clip = mp3play.load(f)
clip.play()
time.sleep(length)
clip.stop()

mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"
sample_rate = 48000
chunk_size = 2048

r = sr.Recognizer()
 
mic_list = sr.Microphone.list_microphone_names()

device_id = 0

global alarmtime

for i, microphone_name in enumerate(mic_list):
    if microphone_name == mic_name:
        device_id = i
while True:
    with sr.Microphone(device_index = device_id, sample_rate = sample_rate, 
                            chunk_size = chunk_size) as source:

        r.dynamic_energy_threshold = False
        r.adjust_for_ambient_noise(source,1)
        print "Say Something"
        
        audio = r.listen(source)
             
        try:
            text = r.recognize_google(audio)
            print "you said: " + text
            inp=list(text.split(' '))
            if inp[0]=="April" or inp[0]=="april":
                if len(inp)==1:
                    print "Listening..."
                    f="yes.mp3"
                    audio = MP3(f)
                    length=audio.info.length
                    clip = mp3play.load(f)
                    clip.play()
                    time.sleep(length)
                    clip.stop()
                    r.adjust_for_ambient_noise(source,1)
                    audio=r.listen(source)
                    text = r.recognize_google(audio)
                    print "you said: " + text
                else:
                    text=" ".join(inp[1:])
                text=text.lower()
                text.strip(" ")
                i=text.split(' ')
                sear=" ".join(i[:2])
                sear.strip(" ")
                sear2=" ".join(i[:3])
                sear2.strip(" ")
                ala=" ".join(i[:3])
                ala.strip(" ")
                vol_con=" ".join(i[:4])
                vol_con.strip(" ")
                vol_con2=" ".join(i[:3])
                vol_con2.strip(" ")

                if text=="what's the date":
                    os.system("start date.py")
                    #date()
                
                elif text=="what's the time":
                    os.system("start time_disp.py")
                    #time_disp()
                    
                elif text=="set an alarm":
                    f=open("command_alarm.txt",'w')
                    f.write("")
                    f.close()
                    os.system("start alarm.py")

                elif ala=="wake me up":
                    te=text.split(" ")
                    time_alarm=" ".join(te[4:])
                    time_alarm=time_alarm.strip(" ")
                    f=open("command_alarm.txt",'w')
                    f.write(time_alarm)
                    f.close()
                    os.system("start alarm.py")

                elif text=="set a reminder":
                    os.system("start reminder.py")
                    f="reminder_aud.mp3"
                    audio = MP3(f)
                    length=audio.info.length
                    time.sleep(length)
                    
                    
                elif text=="what day is it":
                    os.system("start day.py")
                    #day_disp()

                elif sear=="what is":
                    te=text.split(" ")
                    key=" ".join(te[2:])
                    key=key.strip(" ")
                    f=open("command_search.txt",'w')
                    f.write(key)
                    f.close()
                    os.system("start selenium_searchtts.py")
                    #search(key)

                elif sear=="who is":
                    te=text.split(" ")
                    key=" ".join(te[2:])
                    key=key.strip(" ")
                    f=open("command_search.txt",'w')
                    f.write(key)
                    f.close()
                    os.system("start selenium_searchtts.py")
                    #search(key)

                elif sear2=="tell me about":
                    te=text.split(" ")
                    key=" ".join(te[3:])
                    key=key.strip(" ")
                    f=open("command_search.txt",'w')
                    f.write(key)
                    f.close()
                    os.system("start selenium_searchtts.py")
                    #search(key)

                elif text=="tell me about yourself":
                    os.system("start about_me.py")

                elif "wifi" in text:
                    te=text.split(" ")
                    x=int(te[2])
                    networks=ss.wifi_networks(x)
                    out="The top "+str(x)+" wifi networks are "
                    for s in networks:
                        out=out+s+", "
                    out=out.strip(",")
                    f=open("wifi_out.txt",'w')
                    f.write(out)
                    f.close()
                    os.system("start wifi_out.py")

                elif text=="play music":
                    volume.play()

                elif text=="pause music":
                    volume.play()

                elif text=="next track":
                    volume.next()

                elif text=="play next track":
                    volume.next()

                elif text=="previous track":
                    volume.prev()

                elif text=="play previous track":
                    volume.prev()
                    
                elif text=="full volume":
                    volume.Volume_up_full()
                    
                elif vol_con=="set the volume to":
                    te=text.split(" ")
                    vol=" ".join(te[4:])
                    vol=vol.strip(" ")
                    vol=int(vol)
                    volume.Set_volume(vol)

                elif vol_con=="increase the volume to":
                    te=text.split(" ")
                    vol=" ".join(te[4:])
                    vol=vol.strip(" ")
                    vol=int(vol)
                    volume.Set_volume(vol)

                elif vol_con=="decrease the volume to":
                    te=text.split(" ")
                    vol=" ".join(te[4:])
                    vol=vol.strip(" ")
                    vol=int(vol)
                    volume.Set_volume(vol)

                elif vol_con2=="set volume to":
                    te=text.split(" ")
                    vol=" ".join(te[3:])
                    vol=vol.strip(" ")
                    vol=int(vol)
                    volume.Set_volume(vol)
                    
                elif vol_con=="increase the volume by":
                    te=text.split(" ")
                    vol=" ".join(te[4:])
                    vol=vol.strip(" ")
                    vol=int(vol)
                    volume.inc_volume(vol)

                elif vol_con2=="increase volume by":
                    te=text.split(" ")
                    vol=" ".join(te[3:])
                    vol=vol.strip(" ")
                    vol=int(vol)
                    volume.inc_volume(vol)

                elif vol_con=="decrease the volume by":
                    te=text.split(" ")
                    vol=" ".join(te[4:])
                    vol=vol.strip(" ")
                    vol=int(vol)
                    volume.dec_volume(vol)

                elif vol_con2=="decrease volume by":
                    te=text.split(" ")
                    vol=" ".join(te[3:])
                    vol=vol.strip(" ")
                    vol=int(vol)
                    volume.dec_volume(vol)
                
                elif text=="have some rest":
                    rest()
                    
            elif text=="nice work april":
                os.system("start thanq.py")
                f="thanq.mp3"
                audio = MP3(f)
                length=audio.info.length
                time.sleep(length)

            elif text=="hello april":
                x=random.randint(1,3)
                if x==1:
                    speak("hello sir")
                elif x==2:
                    speak("yes sir")
                elif x==3:
                    speak("how are you sir")
                f="audio.mp3"
                audio = MP3(f)
                length=audio.info.length
                clip = mp3play.load(f)
                clip.play()
                time.sleep(length)
                clip.stop()

            elif text=="how are you april":
                x=random.randint(1,3)
                if x==1:
                    speak("I'm fine sir")
                elif x==2:
                    speak("I'm good sir")
                elif x==3:
                    speak("I am a machine what do you expect ")
                f="audio.mp3"
                audio = MP3(f)
                length=audio.info.length
                clip = mp3play.load(f)
                clip.play()
                time.sleep(length)
                clip.stop()
            
            elif text=="mute":
                volume.Mute()
                
            elif text=="unmute":
                volume.Mute()
            else:
                print "NO command found"
                        
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
         
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        
            
