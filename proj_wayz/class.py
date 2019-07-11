import re
import lib.writer as write
with open("data/dianping.html",'r') as f:
    source = f.read()
    ch = re.findall(r'href="/shanghai/ch.*?">(.*?)</a>',source)
    id = re.findall(r'href="/shanghai/ch(.*?)">.*?</a>',source)
    print(ch,id)
    for i in range(len(ch)):
        ch2 = re.findall(r'class="B" href="//www.dianping.com/shanghai/ch'+str(id[i])+'/g(.*?)">(.*?)</a>',source)
        for v in range(len(ch2)):
            result = id[i]+','+ch[i]+','+re.sub(r'[(\')><\";=]*', '', str(ch2[v]))
            print(result)
            # write.csv_write('data/result.csv',result)