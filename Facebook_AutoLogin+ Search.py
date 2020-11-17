from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyautogui, sys
import time
import pandas as pd
import requests
import selenium

Email = input('Enter Your Email: ')
Password = input('Enter Your Password: ')
OnlyFan = input('Please The Guy You Want To Stalk: ')


options= webdriver.ChromeOptions()
options.add_argument('--disable-notifications')

driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\chromedriver', chrome_options=options )


driver.get('https://www.facebook.com')

#elements = driver.find_elements(By.id,'email')
#elements = driver.find_elements(By.id,'pass')

driver.find_element_by_xpath('//*[@id="email"]').send_keys(Email)
driver.find_element_by_xpath('//*[@id="pass"]').send_keys(Password)
driver.find_element_by_xpath('//*[@id="u_0_b"]').send_keys(Keys.ENTER)
time.sleep(6)
driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/label/input').send_keys(OnlyFan)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/label/input').send_keys(Keys.ENTER)
time.sleep(2)
driver.get_screenshot_as_file('Screenshot.png')
time.sleep(5)
driver.find_elements_(OnlyFan).click()


