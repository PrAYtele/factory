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




number=0
def save_img(img):
        global number
        global a
        img_url = img
        if len(img_url) == 0:
            return 0
        else:
            img_url=str(img_url[0])
            print(img_url)
            file_path = 'D:/book/%d'%a
            file_name = "%d"%(number)
            number+=1

        try:
            # 是否有这个路径
            if not os.path.exists(file_path):
                # 创建路径
                os.makedirs(file_path)
                # 获得图片后缀
            file_suffix = os.path.splitext(img_url)[1]
            print(file_suffix)
            # 拼接图片名（包含路径）
            filename = '{}{}{}{}'.format(file_path, os.sep, file_name, file_suffix)
            print(filename)
            # 下载图片，并保存到文件夹中
            urllib.request.urlretrieve(img_url, filename=filename)

        except IOError as e:
            print("IOError")
        except Exception as e:
            print("Exception")

def yellow(counter1):
    global a
    global b

    url = 'https://m.duzhez.com/rank/'
    re

    response = requests.get(url)
    # response.encoding = 'iso-8859-1'
    response.encoding = 'utf-8'
    # print(response.text)
    html = response.text

    key1 = re.findall(r'Box" data-key="(.*?)"', html, re.S)
    key=key1[counter1]

    second_url = 'm.duzhez.com/manhua/'
    second_url = "%s%s%s%s" % ('https://', second_url, key, '/')
    # print(second_url)
    second_response = requests.get(second_url)
    # response.encoding = 'iso-8859-1'
    second_response.encoding = 'UTF-8'
    # print(response.text)
    second_html = second_response.text
    # print(second_html)
    key2=re.findall(r'a href="/manhua(.*?).html',second_html,re.S)
    lenkey=len(key2)
    lenkey=lenkey-1
    for i in range(lenkey):


        chapter = re.findall('%s/(.*?).html' % key, second_html)[i]
        # print(chapter)
        #for i in range(100):

        thd_url = "%s%s%s" % (second_url, chapter, '.html?p=1')
            #print(thd_url)
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe')
        #driver = webdriver.Chrome()

        driver.get(thd_url)
               # al = driver.switch_to.alert()
                #result=al.text()
                #print(result)
        while True:
            result = EC.alert_is_present()(driver)
            print(result)
            #time.sleep(1)


            if result:
                driver.close()
                print("return")
                break
            else:
                img_html = re.findall(r'" src="(.+?.jpg)', driver.page_source)
                print(img_html)
                save_img(img_html)
                driver.find_element_by_id("images").click()


a=0
b=0
c=0
while True:
    yellow(a)
    a+=1




#
# class alert_is_present(object):
#       global driver
# #     """ Expect an alert to be present."""
# #
# #     """判断当前页面的alert弹窗"""
# #     def __init__(self):
# #         pass
# #
#       def __call__(self, driver):
#         try:
#             print("return")
#             alert = driver.switch_to.alert()
#             alert.text
#             return alert
#         except NoAlertPresentException:
#             print("abcde")
#             return False







