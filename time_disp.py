import time
import mp3play
from mutagen.mp3 import MP3
import sys
from gtts import gTTS

#text=datetime.datetime.now()
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


