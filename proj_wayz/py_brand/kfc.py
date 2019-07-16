import time
import re
import urllib.request
import urllib.parse
import json
import requests
import lib.writer as writer

for j in range(1,654):
    headers = {
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin':'http://www.kfc.com.cn',
    'Referer':'http://www.kfc.com.cn/kfccda/storelist/',
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.8 Safari/537.36'
    }
    keyword = ''
    data = {
        "cname":"",
        "pid": "",
        "keyword": keyword,
        "pageIndex": j,
        "pageSize": "10",
    }
    data = urllib.parse.urlencode(data).encode("utf8")
    request = urllib.request.Request(url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword', headers=headers, )
    response = urllib.request.urlopen(request,data=data)
    result = response.read().decode("utf8")
    print(result)
    for i in range(len(json.loads(result)["Table1"])):
        name = json.loads(result)["Table1"][i]["storeName"]
        print(name)
        address = json.loads(result)["Table1"][i]["addressDetail"]
        equip = json.loads(result)["Table1"][i]["pro"]
        city = json.loads(result)["Table1"][i]["cityName"]
        if '餐厅' in name:
            pass
        else:
            name = name +'餐厅'
        if not address:
            address = ''
        if not equip:
            equip = ''
        if not city:
            city = ''
        temp = name+','+address+','+equip+','+city
        writer.csv_write('data/kfc.csv', temp)
        continue
    continue
