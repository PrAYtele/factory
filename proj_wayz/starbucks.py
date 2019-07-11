import re
with open('data/starbucks.html') as html:
    html = html.read()
    ids = re.findall(r'"id":"(.*?)"',html)
    print(len(ids))
    name = re.findall(r'"name":"(.*?)"',html)
    print(len(name))
    city = re.findall(r'"city":"(.*?)"',html)
    print(len(city))
