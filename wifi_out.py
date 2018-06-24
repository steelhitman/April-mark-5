import time
import mp3play
from mutagen.mp3 import MP3
import sys
from gtts import gTTS

f=open("wifi_out.txt",'r')
c=0
for line in f:
   if c==0: 
        output=line
        c=c+1
print output
tts = gTTS(text=output, lang='en')
tts.save("wifi_out.mp3")
f="wifi_out.mp3"
audio = MP3(f)
length=audio.info.length
clip = mp3play.load(f)
clip.play()
time.sleep(length)
clip.stop()
