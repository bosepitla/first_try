# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 19:01:02 2021

@author: newday
tring to use Selenium to open a trade in pocketoption
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

gmailId = 'pitlabose@gmail.com'
passWord = 'dileepraj'

driver = webdriver.Chrome('C:/Users/newday/Desktop/first_try/chromedriver')
driver.get("https://pocketoption.com/en/login")
time.sleep(10)
print("homepage loaded")
driver.find_element_by_link_text("Google").click()
print("cliked google login")
driver.implicitly_wait(15)
  
loginBox = driver.find_element_by_xpath('//*[@id ="identifierId"]')
loginBox.send_keys(gmailId)
nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
nextButton[0].click()
  
passWordBox = driver.find_element_by_xpath(
        '//*[@id ="password"]/div[1]/div / div[1]/input')
passWordBox.send_keys(passWord)
  
nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
nextButton[0].click()
  
print('Login Successful...!!')

time.sleep(10)

#driver.close()