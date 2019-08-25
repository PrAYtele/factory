import re
a = '  123123'
res = re.match(r'^\s*[0-9]*',a)
print(res.group())