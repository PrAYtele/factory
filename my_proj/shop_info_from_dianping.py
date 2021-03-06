import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import csv
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
import time

option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = Chrome(options=option)



def get_url():
    url = 'https://m.dianping.com/shoplist/7/search?from=m_search&keyword=%E7%BB%BC%E5%90%88%E5%95%86%E5%9C%BA'
    driver.get(url)
    for i in range(100):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
    name = re.findall(r'item-shop-name\">(.*?)<',driver.page_source)
    stars = re.findall(r'star star-(.*?)\"',driver.page_source)
    price = re.findall(r'item-comment-price\">(.*?)<',driver.page_source)
    region = re.findall(r'item-info-region\">(.*?)<',driver.page_source)
    time.sleep(5)
    csvFile2 = open('test.csv', 'w', newline='')  # 设置newline，否则两行之间会空一行
    writer = csv.writer(csvFile2, delimiter='\t')
    m = len(name)
    for i in range(m):
        writer.writerow(str(name[i]))
    for i in range(m):
        writer.writerow(str(stars[i]))
    for i in range(m):
        writer.writerow(str(price[i]))
    for i in range(m):
        writer.writerow(str(region[i]))

    csvFile2.close()

get_url()
