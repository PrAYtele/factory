import time
import re
import lib.webdriver as drive
import lib.writer as writer
import lib.te as te



driver = drive.chrome()
driver.maximize_window()
def get_url(url):
    driver.get(url)
    driver.maximize_window()
    for i in range(21):##21是因为没有超过20页的，所以循环最多到19次
        flag = False
        try:
            driver.find_element_by_xpath("//*[text()='下一页']")##找到下一页按钮说明当前输入的城市有维也纳酒店
            flag = True
        except:
            flag = False

        if flag == True:
            driver.maximize_window()
            info1 = re.findall(r'class="tei_width">(.*?店.*?店)', driver.page_source)##店名
            info2 = re.findall(r'class="whow_eee">(.*?)</span><a href="javas',driver.page_source)##地址
            info3 = re.findall(r'class="start_hh"><p>(.*?)/',driver.page_source)##评分
            info4 = re.findall('yellow_F8">查看地图<.*?yellow_F8">(.*?)</sp',driver.page_source)##最低价格
            info5 = re.findall(r'mapOpen.*?&quot;(.*?)&quot;,&quot;(.*?)span class="icon_', driver.page_source)##坐标
            info6 = re.findall(r'chooseMorePromotion.*?data-value="(.*?)">', driver.page_source)##id
            info7 = re.findall(r'(http://image.wyn88.com/adminbranch/.*?middle.jpg)',driver.page_source)##图片
            if len(info1)!=len(info6):##这个循环是为了把没有id的未开业的店统一起来
                for i in range(len(info1)-len(info6)):
                    info6.append('0')
            if len(info7)!=len(info1):##未开业的店统一使用默认图片
                for i in range(len(info1)-len(info7)):
                    info7.append('http://www.wyn88.com/images/hotel_img_choubei.png')
            #print(info5)
            for i in range(len(info1)):
                info5[i] = str(info5[i])
                info5[i] = re.sub(r'[(\')><\";=]*', '', info5[i])##原始的html坐标格式有很多符号，去掉
                info5[i] = info5[i].replace('&quot', '')
                if 'html' in info1[i]:
                    temp = re.findall(r'http.*?.html">(.*?店.*?店)',info1[i])[0]##因为未开业的店名前面没有网址，所以要把开业的店名网址去掉
                    info1[i] = str(temp)
                icons1 = driver.find_elements_by_class_name("icon_all")[i].get_attribute('innerHTML')##定位到第一行icon
                icons1 = re.findall(r'title="(.*?)"', icons1)
                icons2 = driver.find_elements_by_class_name("icon_all")[i+1].get_attribute('innerHTML')##定位到第二行icon
                icons2 = re.findall(r'title="(.*?)"', icons2)
                strr=info6[i]+','+info1[i]+')'+','+info2[i]+','+info3[i]+','+info4[i]+','+info5[i]+','+str(icons1)+','+str(icons2)+','+info7[i]
                strr = str(strr)
                print(strr)
                writer.csv_write('data/wyn.csv',strr)

            driver.maximize_window()
            driver.find_element_by_xpath("//*[text()='下一页']")
            flag2 = re.findall(r'onclick="seachNewHotel(.*?)">下一页<',driver.page_source)
            if len(flag2) != 0:##如果下一页的JavaScript属性长度不为0，也就是可以点击
                time.sleep(1)
                driver.find_element_by_xpath("//*[text()='下一页']").click()
                continue
            else:
                return 0
        else:
            return 0

j= 0
while True:
    url_head = 'http://www.wyn88.com/resv/newresv.html?startTime=2019-05-24&endTime=2019-05-25&keyWord=&cityName='
    division = te.getdiv()
    url=url_head+division[j]
    get_url(url)
    j += 1

