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
from selenium import webdriver
import unittest
from selenium.webdriver.common.action_chains import ActionChains
def isElementExist(driver,element):
    flag = True
    browser = driver
    try:
        browser.driver.find_element_by_xpath(element)
        return flag

    except:
        flag = False
        return flag

option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = Chrome(options=option)



def get_url():
    url = 'http://www.dianping.com/shenzhen/ch20/g119r29'
    driver.get(url)
    for i in range(50):
        ids = re.findall(r'data-shopid="(.*?)".*?title="(.*?)"',driver.page_source)
        #if EC.element_to_be_clickable((By.CLASS_NAME,"next")):
        flag = True
        try:
            driver.find_element_by_xpath("//*[text()='下一页']")
        except:
            flag = False
        if flag:
            driver.find_element_by_xpath("//*[text()='下一页']").click()
            csvFile2 = open('id.csv', 'a', newline='')  # 设置newline，否则两行之间会空一行
            writer = csv.writer(csvFile2, delimiter='\t')
            for i in range(len(ids)):
                writer.writerow(ids[i])
            csvFile2.close()
        else:
            csvFile2 = open('id.csv', 'a', newline='')  # 设置newline，否则两行之间会空一行
            writer = csv.writer(csvFile2, delimiter='\t')
            for i in range(len(ids)):
                writer.writerow(ids[i])
            csvFile2.close()
            return 0


get_url()
