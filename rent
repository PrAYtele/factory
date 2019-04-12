from selenium import webdriver
import time
import re
import os, stat
import urllib.request
from PIL import Image
import requests
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def info_rs():

    url = 'http://rs.xidian.edu.cn/forum.php?mod=forumdisplay&fid=565&filter=typeid&typeid=109'
    chrome_options = Options()
    #chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe')
    # driver = webdriver.Chrome()

    driver.get(url)
    #print(driver.page_source)

    html = re.findall(r'id="normalthread_(.*?)">', driver.page_source)
    #driver.find_element_by_class_name("s xst")
    #driver.click()
    for i in range(len(html)):
        a='http://rs.xidian.edu.cn/forum.php?mod=viewthread&tid='
        b=html[i]
        c='&extra=page%3D1'
        url2="%s%s%s" % (a,b,c)
        i+=1
        #print(url2)
        driver.get(url2)
        html2 = re.findall(r'div id="post_(.*?)">', driver.page_source)
        #print(html2)
        post="%s%s%s"%('//*[@id="postmessage_',html2[0],'"]')

        #print(post)
        titlepath='//*[@id="thread_subject"]'
        title=driver.find_element_by_xpath(titlepath).text
        print(title)
        content=driver.find_element_by_xpath(post).text
        print(content)
        file = open("C:/Users/Administrator/Desktop/12.txt",'a')
        file.write('title:')
        file.write(title)
        file.write('\n')
        file.write('content:')
        file.write(content)
        file.write('\n')
        file.write("\n-------------------------------------------\n")
        file.close()




    #print(html)


    #html=re.findall(r'class="sxst">(.*?)</a>',html,re.S)
    #print(len(eles))
info_rs()
