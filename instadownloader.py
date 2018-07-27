from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import sys
import time

username="prashantarya_47"
password="steelhitman47"

driver = webdriver.Chrome(executable_path=r"C:\Python27\april\Test mark 5\chromedriver.exe")
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(1)
actions = ActionChains(driver) 
actions.send_keys(Keys.TAB)
actions.perform()
actions = ActionChains(driver)
actions.send_keys(username)
actions.perform()
actions = ActionChains(driver)
actions.send_keys(Keys.TAB)
actions.perform()
actions = ActionChains(driver)
actions.send_keys(password)
actions.perform()
actions = ActionChains(driver)
actions.send_keys(Keys.RETURN)
actions.perform()
time.sleep(10)
driver.close()
