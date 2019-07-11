import csv


def getdiv():
    with open('data/2019年3月中华人民共和国县以上行政区划代码.csv','r',encoding='gbk') as csvfile:
        reader = csv.reader(csvfile)
        column = [row[1]for row in reader]
        city = []
        for i in range(len(column)):
            if '市' in column[i]:
                city.append(column[i])
            if '行政区' in column[i]:
                city.append(column[i])
            if '自治州' in column[i]:
                city.append(column[i])
            if '地区' in column[i]:
                city.append(column[i])
            if '盟' in column[i]:
                city.append(column[i])
            else:
                continue
        return city
getdiv()