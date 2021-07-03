# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 19:41:03 2021

@author: newday
"""

from selenium import webdriver
import geckodriver_autoinstaller
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import time

geckodriver_autoinstaller.install()

profile = webdriver.FirefoxProfile('C:\\Users\\newday\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\527p34be.default-release')
# '/Users/newday/Library/Application Support/Firefox/Profiles/xxxxx.default-release'
gmailId = 'pitlabose@gmail.com'
passWord = 'dileepraj'

profile.set_preference("dom.webdriver.enabled", False)
profile.set_preference('useAutomationExtension', False)
profile.update_preferences()
desired = DesiredCapabilities.FIREFOX

driver = webdriver.Firefox(firefox_profile=profile,
                           desired_capabilities=desired)
driver.get("https://pocketoption.com/en/login")
time.sleep(10)
print("homepage loaded")
driver.find_element_by_link_text("Google").click()
print("cliked google login")
time.sleep(10)
# =============================================================================
# driver.implicitly_wait(15)
# time.sleep(10)
# loginBox = driver.find_element_by_xpath('//*[@id ="identifierId"]')
# loginBox.send_keys(gmailId)
# time.sleep(10)
# nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
# nextButton[0].click()
#   
# passWordBox = driver.find_element_by_xpath(
#         '//*[@id ="password"]/div[1]/div / div[1]/input')
# passWordBox.send_keys(passWord)
#   
# nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
# nextButton[0].click()
# =============================================================================
  
print('Login Successful...!!')