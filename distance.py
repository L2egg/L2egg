from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import requests
import re
from bs4 import BeautifulSoup
import time

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화   
url = 'https://map.naver.com/v5/directions/'
browser.get(url)

time.sleep(6)

f = open('jeju_randmark.txt','r', encoding='UTF-8')
lines = f.readlines()

f1 = open('jeju_venue.txt','r', encoding='UTF-8')
lines_1 = f1.readlines()

for line in lines:
    for line_1 in lines_1:
        browser.find_element(By.XPATH,'//*[@id="directionStart0"]').send_keys(line)
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="directionStart0"]').send_keys(Keys.ENTER)
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="directionGoal1"]').send_keys(line_1)
        browser.find_element(By.XPATH,'//*[@id="directionGoal1"]').send_keys(Keys.ENTER)
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="directionGoal1"]').send_keys(Keys.ENTER)
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="container"]/shrinkable-layout/div/directions-layout/directions-result/div[1]/div/ul/li[2]/a').click()
        time.sleep(3)
        browser.find_element(By.XPATH,'//*[@id="container"]/shrinkable-layout/div/directions-layout/directions-result/div[1]/div[1]/directions-search/div[2]/button[1]').click()
        time.sleep(2)


f.close()
f1.close()