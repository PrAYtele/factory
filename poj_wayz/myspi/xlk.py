import time
import re
import lib.writer as writer
from selenium.webdriver.support.wait import WebDriverWait
import lib.webdriver as webdriver


driver = webdriver.chrome()
url = 'https://www.xiaolongkan.com/storesFind.html'
wait = WebDriverWait(driver, 10)
driver.get(url)

driver.find_element_by_class_name("current").click()
driver.find_element_by_xpath("//*[text()='门店']").click()

driver.find_element_by_id("cityName").click()

driver.find_element_by_id("cityName").send_keys("店")

driver.find_element_by_class_name("BtnSearch._iconfont").click()
time.sleep(5)
driver.find_element_by_class_name("BtnSearch._iconfont").click()
time.sleep(5)
num = re.findall(r'class="unm">(.*?)</span>',driver.page_source)
name = re.findall(r'<span class="name">(.*?)</span>',driver.page_source)
time = re.findall(r'<p><span>营业时间：</span>(.*?)</p>',driver.page_source)
tel = re.findall(r'<p><span>电话：</span>(.*?)</p>',driver.page_source)
address = re.findall(r'<p><span>地址：</span>(.*?)</p>',driver.page_source)
for i in range(807):
    result = num[i]+','+name[i]+','+time[i]+','+tel[i]+','+address[i]
    print(result)
    writer.csv_write('data/xlk.csv',result)
