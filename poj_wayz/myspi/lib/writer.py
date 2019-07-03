import csv
def csv_write(path,strr):
    csvFile2 = open(path, 'a+', newline='')  # 设置newline，否则两行之间会空一行
    csvFile2.write(strr + '\n')
    csvFile2.close()