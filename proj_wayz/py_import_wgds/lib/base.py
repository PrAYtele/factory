
# -*- coding: utf-8 -*-

import math
import os
import json
import time
import csv
import sys
import datetime

# 引入本地文件
sys.path.append("..")

# 打印信息
def log(arr):
    if type(arr) is list:
        info = ' '.join(str(v) for v in arr)
    else:
        info = str(arr)
    print(info)

# 写入csv
def write_csv_a(path, data):
    if type(data) is list:
        data = ','.join(str(v) for v in data)
    elif type(data) is tuple:
        data = ','.join(str(v) for v in data)
    else:
        data = str(data)
    f = open(path, "a+")
    f.write(data + '\n')
    f.close()

# 读取csv
def read_csv(url):
    csv_data = csv.reader(open(url))
    return csv_data

# 加载json文件
def load_json_file(url):
    with open(url, 'r') as f:
        data = json.load(f)
        return data
        
# 获取当前时间，格式化
def get_time():
    t = time.time()
    return [t, int(round(t * 1000)), datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') ]

    # nowTime = lambda:int(round(t * 1000))
    # print nowTime();              #毫秒级时间戳，基于lambda
