import speech_recognition as sr
import mp3play
from mutagen.mp3 import MP3
import sys
from time import ctime
import time
import os
from gtts import gTTS

import datetime

mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"
sample_rate = 48000
chunk_size = 2048

r = sr.Recognizer()
 
mic_list = sr.Microphone.list_microphone_names()

device_id = 0

for i, microphone_name in enumerate(mic_list):
    if microphone_name == mic_name:
        device_id = i

with sr.Microphone(device_index = device_id, sample_rate = sample_rate, 
                            chunk_size = chunk_size) as source:
        
        r.adjust_for_ambient_noise(source,1)
        print "Say Something"
        
        audio = r.listen(source)
             
        try:
            text = r.recognize_google(audio)
            print "you said: " + text
            inp=list(text.split(' '))
            text = r.recognize_google(audio)
            print "you said: " + text        

            text=text.lower()
            noise_list=["at","to","april","in"]
            text=text.strip().split(' ')
            if ("remind" in text) and ("me" in text) and ("to" in text) :
                noise_free_words = [word for word in text if word not in noise_list] 
                noise_free_text = " ".join(noise_free_words)

            print noise_free_text
            noise_free_text=noise_free_text.split(' ')
            command = noise_free_text[0]
            wo = " ".join(noise_free_words[2:-2])
            w=wo.split(' ')
            work=""
            for wor in w:
                if wor=="my":
                    work=work+" your "
                else:
                    work=work+" "+wor
            time1 = noise_free_text[-2]+" "+noise_free_text[-1]

            print command,"     ",work,"      ",time1

            time1=time1.split(' ')
            global hr
            global mins
            if "o" in time1[1]:
                hr= time1[0]
                mins=time1[2]
            else:
                t=time1[0]
                t=t.split(":")
                hr=t[0]
                try:
                    mins=t[1]
                except:
                    mins="00"
                    
            if time1[1]=="a.m." or time1[1]=="a.m" :
                if hr=="12":
                    hr=str(int(hr)-12)
            elif time1[1]=="p.m." or time1[1]=="p.m":
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
                    
            f="alarm_tone.mp3"
            audio = MP3(f)
            length=audio.info.length    
            clip = mp3play.load(f)
            clip.play()
            time.sleep(length/4)
            clip.stop()
            
            tts = gTTS(text="      Sir you have a reminder to "+work, lang='en')
            tts.save("reminder_work.mp3")


            f="reminder_work.mp3"
            audio = MP3(f)
            length=audio.info.length    
            clip = mp3play.load(f)
            clip.play()
            time.sleep(length)
            clip.stop()
                    

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
         
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

