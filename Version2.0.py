from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import pyautogui, sys
import time
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import urllib
import urllib.request
import pandas as pd
import requests
import selenium
import webbrowser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
time.sleep(4)
driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/label/input').send_keys(Keys.ENTER)
time.sleep(3)
l= driver.find_elements_by_partial_link_text(OnlyFan)
i = 0

for i in l:
   #get href from get_attribute()
   print(i.get_attribute("href"))

driver.get_screenshot_as_file('Screenshot.png')
time.sleep(5)


URL2 = input('Which URL ? : ')
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get(URL2)
time.sleep(6)

#img = driver.find_elements_by_tag_name('img alt')
#img = driver.find_elements_by_id('')



#for x in img:
   #get href from get_attribute()
   #src = x.get_attribute('src')
   #urlretrieve(src)

images = driver.find_elements_by_tag_name('img')
for image in images:
    print(image.get_attribute('src'))

soup_a = BeautifulSoup(driver.page_source, 'lxml')
links = []

print('________________________________________________________')
for link in soup_a.find_all('a'):
    links.append(link.get('href'))
    print(links)
print('_________________________________________________________')
print(driver.current_url)
