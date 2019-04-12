import phone
import re


def text_save(filename, data):  # filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename, 'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
       # s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功")

for i in range(1, 9999):
    strr="四川"
    #print(str(i).zfill(4))
    phoneNum = '187'+str(i).zfill(4)
    info = phone.Phone().find(phoneNum)
    info=str(info)
    print(info)
    if strr in info:
        text_save("C:/Users/Administrator/Desktop/13.txt",info)
    else:
        continue
