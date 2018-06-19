from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
import mp3play
from mutagen.mp3 import MP3
import sys
import time
from time import ctime
import os
from gtts import gTTS
global text
text=""
fp=open("command_search.txt",'r')
for line in fp:
    text=line
fp.close
driver = webdriver.Chrome(executable_path=r"C:\Python27\april\chromedriver.exe")
driver.get("https://www.wikipedia.org/")
elem = driver.find_element_by_name("search")
elem.clear()
elem.send_keys(text)
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
