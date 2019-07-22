import time
import re
import datetime
import urllib.request
import urllib.parse
import json
import requests
from threading import Thread
import sys
import tool
from tqdm import trange



def main(city):
    count = 1
    total = 1
    while count <= total:
        payloadHeader = {

            "Host": "www.998.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.8 Safari/537.36",

        }
        payloadData = {
            "PageIndex": count,
            "PageSize": "5",
            "cityId": city
        }
        postUrl='http://www.998.com/HotelList/SearchHotelList'
        r = requests.post(url=postUrl,data=payloadData,headers=payloadHeader)
        result = r.text
        try:
            total = re.findall(r'TotalCount":(.*?),',result)[0]
        except:
            break
        total = int(total)
        total = int(total/5+1)
        '''
        每个城市和每页都更新一次data
        '''
        name1 = re.findall(r'"HotelName":"(.*?)"',result)
        hotel_type_temp = re.findall(r'"HotelType":"(.*?)"',result)
        hotel_types = []

        for j in range(len(hotel_type_temp)):
            if hotel_type_temp[j] != 'null':
                hotel_types.append(hotel_type_temp[j])

        address1 = re.findall(r'"Address":"(.*?)"',result)
        tel1 = re.findall(r'"Phone":"(.*?)"',result)
        xy = re.findall(r'BmapPoint":"(.*?)"',result)
        ids = re.findall(r'"HotelCode":"(.*?)"',result)
        ids_temp = list(set(ids))
        ids_temp.sort(key = ids.index)
        ids = ids_temp
        name_ens = re.findall(r'HotelNameEn":"(.*?)"',result)
        start_times = re.findall(r'StartBusinessTime":"(.*?)"',result)
        facilities = re.findall(r'HotelServiceList(.*?)HotelServiceListAll',result)
        imgs = re.findall(r'"HotelImg":"(.*?)"',result)
        scores = re.findall(r'CommentScore":(.*?),',result)
        lowest = re.findall(r'LowestPrice":"(.*?)"',result)

        for i in range(len(xy)):
            equip = ''
            if facilities[i] :
                facility = facilities[i]
                facility = re.findall(r'"KeyId":"(.*?)","Ho',facility)
                for j in range(len(facility)):
                    if facility[j] == '51':
                        equip = equip + '|早餐'
                    if facility[j] == '41':
                        equip = equip +'|停车场'
                    if facility[j] == '152':
                        equip = equip + '|会议室'
                    if facility[j] == '215':
                        equip = equip +'|客房WIFI'
                    if facility[j] == '91':
                        equip = equip + '|接待外宾'
                    if facility[j] == '189':
                        equip = equip +'|自助机'
            equip = equip.strip('|')
            name = name1[i]
            hotel_type = hotel_types[i]
            price = lowest[i]
            if price == '满房':
                price = ''
            address = address1[i].replace(',',';').replace(' ','')
            tel = tel1[i]
            if len(tel) == 0 or len(tel) == 1:
                tel = ''
            lng = xy[i].split(',')[1]
            start_time = start_times[i]
            score = scores[i]
            lat = xy[i].split(',')[0]
            id = ids[i]
            img = imgs[i]
            name_en = name_ens[i]
            if len(name_en) == 0:
                name_en = ''
            final = id+','+name+','+img+','+score+','+equip+','+start_time+','+address+','+tel+','+lng+','+lat+','+hotel_type+','+name_en+','+price
            #print(final)
            lens = [id,name,img,score,start_time,address,tel,lng,lat,hotel_type,name_en]
            if len(lens) != 11:
                print('此条信息异常')
                count += 1
                continue

            tool.csv_write('data/out_data/998.csv',final)
        count += 1
def get(num,num2):
    cities = []
    with open('data/tool_data/998_cities.json') as f:
        dic = json.load(f)
        for row in dic:
            cities.append(row.get('ID',None))
    for i in trange(num,num2):
        main(cities[i])
        #print('已完成城市ID:',cities[i])
    print('success')
thread1 = Thread(target=get,args=(0,47))
thread2 = Thread(target=get,args=(47,94))
thread3 = Thread(target=get,args=(94,141))
thread4 = Thread(target=get,args=(141,188))
thread5 = Thread(target=get,args=(188,235))
thread6 = Thread(target=get,args=(235,282))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()


