import re
import lib.writer as writer
with open('data/subway.html') as html:
    content = html.read()
    name = re.findall(r'storename">(.*?)</spa',content)
    print(len(name))
    address = re.findall(r'"storeaddress">(.*?)</di',content)
    print(len(address))
    open_time = re.findall(r'lass="opentime">(.*?)</',content)
    print(len(open_time))
    tel = re.findall(r'="storephone">(.*?)</div',content)
    print(len(tel))
    for i in range(len(name)):
        result = name[i]+','+address[i]+','+open_time[i]+','+tel[i]
        writer.csv_write('data/subway.csv',result)