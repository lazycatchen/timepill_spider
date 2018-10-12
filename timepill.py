from tqdm import tqdm
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
import pandas as pd
import numpy as np
import re

body,name,book,content,bottom,date,name1=[],[],[],[],[],[],[]
def get_one_page(key):
    try:
      #打开浏览器窗口
        option_chrome = webdriver.ChromeOptions()
        option_chrome.add_argument('--headless')

        driver = webdriver.Chrome(chrome_options=option_chrome)
        #time.sleep(1)

        url = "http://www.timepill.net/"+str(key)
        driver.get(url)
        infor = driver.find_elements_by_class_name("diary")
        for i in range(len(infor)):
            temp=infor[i].find_element_by_class_name("body").text
            try:
                 name1=infor[i].find_element_by_class_name("name").text
            except:
                name1=("")
            name.append(name1)
            date.append(temp.replace(name1,'').split('《')[0][-12:-1])
        driver.quit()
        return
    except TimeoutException or WebDriverException:
        return get_one_page()

num = [n*20 for n in range(0,150)]
for key in tqdm(num):
    print ("正在爬取{}".format(key))
    get_one_page(key)


result = {'date': date, 'name': name}
result = pd.DataFrame(result, columns=['date', 'name'])
result.to_csv("result.csv",encoding="utf_8_sig")