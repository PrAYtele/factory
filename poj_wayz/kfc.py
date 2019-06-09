import time
import re
import lib.webdriver as webdriver
import lib.writer as writer
driver = webdriver.chrome()
url = 'http://www.kfc.com.cn/kfccda/storelist/'
driver.get(url)
driver.find_element_by_id("keyword").click()
driver.find_element_by_id("keyword").send_keys("餐厅")
driver.find_element_by_id("btn_search").click()
time.sleep(2)
#temp = driver.find_element_by_id("listhtml").get_attribute('innerHTML')
#print(temp)
strr = list(range(20))
while True:
    info = re.findall(r'align="center">(.*?)</td>.*?<td>(.*?)</td>.*?target="_blank" class="(.*?)</td>',driver.page_source)
    print(info)
    for i in range(len(info)):
        print(info[i][0])
        print(info[i][1])
        wifi = False
        allday = False
        view = False
        birth = False
        if 'WiFi' in info[i][2]:
            wifi = True
        if '全天营业' in info[i][2]:
            allday = True
        if '店内参观' in info[i][2]:
            view = True
        if '生日餐会' in info[i][2]:
            birth = True
        temp = ' '
        if wifi == True:
            temp = temp + 'WiFi'+' '
        if allday == True:
            temp = temp + '全天营业'+' '
        if view == True:
            temp = temp + '店内参观'+' '
        if birth == True:
            temp = temp + '生日餐会'+' '
        strr[i] = info[i][0] + ',' + info[i][1] + ',' + temp
        writer.csv_write('data/kfc.csv',strr[i])
    driver.maximize_window()
    element = driver.find_elements_by_class_name("number")[-1]
    driver.execute_script("arguments[0].click();", element)
    time.sleep(1)
    continue