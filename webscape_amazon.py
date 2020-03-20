#------------------Webscraping data from amazon website------------------
import os
os.chdir('F:\\Python\\Bharti')
os.getcwd()

import numpy as np; print("numpy version---",np.__version__)
import pandas as pd;  print("pandas version:",pd.__version__)
from selenium import webdriver
from bs4 import BeautifulSoup
#ensure chromediver.exe is present at below location
DRIVER_PATH = "C:/Users/BHUSHAN/Desktop/chromedriver.exe"

names=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
noofrews=[]

import time
import selenium, time
from selenium.webdriver.common.keys import Keys
# DRIVER_PATH = '.../Desktop/Scraping/chromedriver 2'
srch = input("[prompt] Enter things to search on google: ")
#download_path = input("[+] Enter the download path in full: ")
driver = selenium.webdriver.Chrome(DRIVER_PATH) 
driver.get('https://google.com') #opens browser
driver.maximize_window() #maixmizes the window
search_box = driver.find_element_by_css_selector('input.gLFyf') #or use que=driver.find_element_by_xpath("//input[@name='q']")
search_box.send_keys(srch)
search_box.submit()
time.sleep(2)
results = driver.find_elements_by_xpath('//div[@class="r"]/a/h3')  # finds webresults
results[1].click() 

content = driver.page_source
soup = BeautifulSoup(content, features ='lxml')

#get maximum pages available for this search on amazon
if len(soup.findAll('li', attrs={'class':'a-disabled'})) is 1:
    max_pg = len(soup.findAll('li', attrs={'class':'a-normal'})) +1
else:
    max_pg = int(soup.findAll('li', attrs={'class':'a-disabled'})[1].text) 
#check what is current page no.
current_pg = int(driver.find_element_by_class_name('a-selected').text)

start_time = time.time()
for current_pg in range(max_pg):
    print('webscraping on page %d' %current_pg)
    time.sleep(2)
    for a in soup.findAll('div', attrs={'class':'sg-col-4-of-12 sg-col-8-of-16 sg-col-16-of-24 sg-col-12-of-20 sg-col-24-of-32 sg-col sg-col-28-of-36 sg-col-20-of-28'}):
        #name=a.find('span', attrs={'class':'a-size-medium a-color-base a-text-normal'})
        rating=a.find('span', attrs={'class':'a-icon-alt'})
        noofrew=a.find('span', attrs={'class':'a-size-base'})
        price=a.find('span', attrs={'class':'a-price-whole'})
        #if name is not None:
        names.append(a.find('span', attrs={'class':'a-size-medium a-color-base a-text-normal'}).text)
        #else:
        #   names.append("NA")
        if price is not None:
            prices.append(price.text)
        else:
            prices.append("NA")
        if rating is not None:
            ratings.append(rating.text)
        else:
            ratings.append("NA")
        if noofrew is not None:
            noofrews.append(noofrew.text)
        else:
            noofrews.append("NA")
    print('webscraping on page %d done' %current_pg)
    next_pg = driver.find_element_by_class_name('a-last')
    next_pg.click()
    time.sleep(5)
    current_pg = int(driver.find_element_by_class_name('a-selected').text)

print("Time taken to extract data:%s" % (time.time() - start_time)) 
#print(time.ctime()) #prints current date time

#Make dataframe for saving as csv
df4 = pd.DataFrame({'Product Name':names,'Rating':ratings,'Noof_rew':noofrews,'Prices':prices}) 
df4.to_csv('sample.csv', index=False, encoding='utf-8')
print("done")
driver.quit()
#--------------------------------END-------------------------------------
