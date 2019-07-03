import re
import csv
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

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
    url = 'http://www.dianping.com/shenzhen/ch20/g119r12035'
    driver.get(url)
    for i in range(50):
        ids = re.findall(r'data-shopid="(.*?)".*?title="(.*?)"',driver.page_source)

        flag = True
        try:
            driver.find_element_by_xpath("//*[text()='下一页']")
        except:
            flag = False
        if flag:
            driver.find_element_by_xpath("//*[text()='下一页']").click()
            csvFile2 = open('C:/Users/admin/PycharmProjects/myspi/id.csv', 'a', newline='')  # 设置newline，否则两行之间会空一行
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