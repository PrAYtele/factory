import time
import re
from selenium.webdriver.support.wait import WebDriverWait
import lib.webdriver as webdriver


driver = webdriver.chrome()
url = 'https://www.xiaolongkan.com/storesFind.html'
wait = WebDriverWait(driver, 10)
driver.get(url)
driver.find_element_by_class_name("current").click()
#time.sleep(1)
driver.find_element_by_xpath("//*[text()='门店']").click()
#time.sleep(1)
driver.find_element_by_id("cityName").click()
#time.sleep(1)
driver.find_element_by_id("cityName").send_keys("店")
#time.sleep(1)
driver.find_element_by_class_name("BtnSearch._iconfont").click()
time.sleep(5)
driver.find_element_by_class_name("BtnSearch._iconfont").click()
# time.sleep(2)
# #temp = driver.find_element_by_id("listhtml").get_attribute('innerHTML')
# #print(temp)
# strr = list(range(20))
# while True:
#     info = re.findall(r'align="center">(.*?)</td>.*?<td>(.*?)</td>.*?target="_blank" class="(.*?)</td>',driver.page_source)
#     print(info)
#     for i in range(len(info)):
#         print(info[i][0])
#         print(info[i][1])
#         wifi = False
#         allday = False
#         view = False
#         birth = False
#         if 'WiFi' in info[i][2]:
#             wifi = True
#         if '全天营业' in info[i][2]:
#             allday = True
#         if '店内参观' in info[i][2]:
#             view = True
#         if '生日餐会' in info[i][2]:
#             birth = True
#         temp = ' '
#         if wifi == True:
#             temp = temp + 'WiFi'+' '
#         if allday == True:
#             temp = temp + '全天营业'+' '
#         if view == True:
#             temp = temp + '店内参观'+' '
#         if birth == True:
#             temp = temp + '生日餐会'+' '
#         strr[i] = info[i][0] + ',' + info[i][1] + ',' + temp
#         csvFile2 = open('kfc.csv', 'a+', newline='')  # 设置newline，否则两行之间会空一行
#         csvFile2.write(strr[i] + '\n')
#         csvFile2.close()
#     driver.maximize_window()
#     element = driver.find_elements_by_class_name("number")[-1]
#     driver.execute_script("arguments[0].click();", element)
#     time.sleep(1)
#     continue