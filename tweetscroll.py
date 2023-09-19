#Do imports
import numpy as np
import pandas as pd
import time
import selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# import the required packages and libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# set up a new Selenium driver
driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 今のところ５００ツイートくらいの人しかできない
username = "shuukatsu_9720"
URL = "https://twitter.com/" + username 

# load the URL in the Selenium driver
driver.get(URL)
time.sleep(10) #change according to your pc and internet connection
    
tweets = []
result = False
    
# Get scroll height after first time page load
last_height = driver.execute_script("return document.body.scrollHeight")

last_elem=''
current_elem=''

while True:
    
    # Scroll  to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(6)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    
    #update all_tweets to keep loop
    all_tweets = driver.find_elements(By.XPATH, '//div[@data-testid]//article[@data-testid="tweet"]')

    for item in all_tweets[1:]: # skip tweet already scrapped

        print('--- date ---')
        try:
            date = item.find_element(By.XPATH, './/time').text
        except:
            date = '[empty]'
        print(date)

        print('--- text ---')
        try:
            text = item.find_element(By.XPATH, './/div[@data-testid="tweetText"]').text
        except:
            text = '[empty]'
        print(text)

       
        #Append new tweets replies to tweet array
        tweets.append([username, text, date])
               
        if (last_elem == current_elem):
            result = True
        else:
            last_elem = current_elem


print(tweets)
df = pd.DataFrame(tweets, columns=['name','Tweet', 'Date of Tweet'])
print(df)
