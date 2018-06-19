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

def day_disp():
    text=list(time.ctime().split(' '))
    day_s=['Mon','Tue','Wed','Thur','Fri','Sat','Sun'];
    day=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    month_s=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    month=['January','February','March','April','May','June','July','August','September','Octber','November','December']
    year=text[4]
    date=text[2]
    ti=list(text[3].split(':'))
    #print time[0],time[1],time[2]
    hh=ti[0]
    mm=ti[1]
    ss=ti[2]
    #if hh >12 and hh!=24:
    #    hh=int(hh)-12
    #    print hh,":",mm," pm"
    #elif hh==24:
    #        print "00:",mm," am"
    #else:
    #    print hh,":",mm," am"
    #print text
    d=day[day_s.index(text[0])]
    print d
    t="It's "+d
    tts = gTTS(text=t, lang='en')
    tts.save("day.mp3")
    f="day.mp3"
    audio = MP3(f)
    length=audio.info.length
    clip = mp3play.load(f)
    clip.play()
    time.sleep(length)
    clip.stop()

def time_disp():
    text=list(time.ctime().split(' '))
    day_s=['Mon','Tue','Wed','Thur','Fri','Sat','Sun'];
    day=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    month_s=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    month=['January','February','March','April','May','June','July','August','September','Octber','November','December']
    year=text[4]
    date=text[2]
    ti=list(text[3].split(':'))
    #print time[0],time[1],time[2]
    hh=ti[0]
    mm=ti[1]
    ss=ti[2]
    tim=""
    if hh >12 and hh!=24:
        hh=int(hh)-12
        hh=str(hh)
        tim=hh+":"+mm+" pm"
    elif hh==24:
        tim="00:"+mm+" am"
    else:
        tim=hh+":"+mm+" am"
    #print text
    print tim
    tim="The Time is "+tim
    tts = gTTS(text=tim, lang='en')
    tts.save("time.mp3")
    f="time.mp3"
    audio = MP3(f)
    length=audio.info.length
    clip = mp3play.load(f)
    clip.play()
    time.sleep(length)
    clip.stop()

def date():
    text=list(time.ctime().split(' '))
    day_s=['Mon','Tue','Wed','Thur','Fri','Sat','Sun'];
    day=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    month_s=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    month=['January','February','March','April','May','June','July','August','September','Octber','November','December']
    year=text[4]
    date=text[2]
    ti=list(text[3].split(':'))
    #print time[0],time[1],time[2]
    hh=ti[0]
    mm=ti[1]
    ss=ti[2]
    #if hh >12 and hh!=24:
    #    hh=int(hh)-12
    #    print hh,":",mm," pm"
    #elif hh==24:
    #        print "00:",mm," am"
    #else:
    #    print hh,":",mm," am"
    #print text
    mon=month[month_s.index(text[1])]
    print date, mon,year
    t=date+" "+mon+" "+year
    tts = gTTS(text=t, lang='en')
    tts.save("date.mp3")
    f="date.mp3"
    audio = MP3(f)
    length=audio.info.length
    clip = mp3play.load(f)
    clip.play()
    time.sleep(length)
    clip.stop()

def search(key):
    text=""
    #tts = gTTS(text="what to search for ?", lang='en')
    #tts.save("search.mp3")
    #f="search.mp3"
    #audio = MP3(f)
    #length=audio.info.length    
    #clip = mp3play.load(f)
    #clip.play()
    #time.sleep(length)
    #clip.stop()
    #with sr.Microphone(device_index = device_id, sample_rate = sample_rate, chunk_size = chunk_size) as source:
    #    r.adjust_for_ambient_noise(source,1)
    #    print "Say search keywork..."
    #        
    #    audio = r.listen(source)
    #    try:
    #        text = r.recognize_google(audio)
    #        print "you said: " + text
    #    except:
    #        pass
            
    driver = webdriver.Chrome(executable_path=r"C:\Python27\april\chromedriver.exe")
    driver.get("https://www.wikipedia.org/")
    elem = driver.find_element_by_name("search")
    elem.clear()
    elem.send_keys(key)
    elem.send_keys(Keys.ENTER)
    data=driver.find_element_by_xpath("//*[@id='mw-content-text']/div/p[1]").text
    print data.encode("utf-8")
    #assert "No results found." not in driver.page_source
    driver.close()
    tts = gTTS(text=data, lang='en')
    tts.save("result.mp3")
    f="result.mp3"
    audio = MP3(f)
    length=audio.info.length
    clip = mp3play.load(f)
    clip.play()
    time.sleep(length)
    clip.stop()
    
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

                if text=="what's the date":
                    os.system("start date.py")
                    #date()
                
                elif text=="what's the time":
                    os.system("start time_disp.py")
                    #time_disp()
                    
                elif text=="set an alarm":
                    os.system("start alarm.py")
                    f="alarm_aud.mp3"
                    audio = MP3(f)
                    length=audio.info.length
                    time.sleep(length)

                elif ala=="wake me up":
                    te=text.split(" ")
                    time_alarm=" ".join(te[3:])
                    time_alarm=time_alarm.strip(" ")
                    f=open("command_alarm.txt",'w')
                    f.write(time_alarm)
                    f.close()
                    os.system("start alarm.py")
                    f="alarm_aud.mp3"
                    audio = MP3(f)
                    length=audio.info.length
                    time.sleep(length)

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
##                    f="about_me.mp3"
##                    audio = MP3(f)
##                    length=audio.info.length
##                    clip = mp3play.load(f)
##                    clip.play()
##                    time.sleep(length)
##                    clip.stop()
                    os.system("start about_me.py")
                    
                elif vol_con=="set volume to":
                    te=text.split(" ")
                    vol=" ".join(te[3:])
                    vol=vol.strip(" ")
                    vol=int(vol)
                    volume.Set_volume(vol)
                    
                elif vol_con=="increase volume by":
                    te=text.split(" ")
                    vol=" ".join(te[3:])
                    vol=vol.strip(" ")
                    vol=int(vol)
                    volume.inc_volume(vol)

                elif vol_con=="decrease volume by":
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

        
            
