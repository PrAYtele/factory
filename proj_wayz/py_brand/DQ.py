import re
with open('data/DQ.html',encoding='utf-8') as html:
    html = html.read()
    address = re.findall(r'地址：(.*?)</span>',html)
    print(len(address))
    name = re.findall(r'alt="">(.*?)</p>',html)
    print(len(name))
