# -*- coding: utf-8 -*-

import math
import os
import json
import time
import csv
import sys
import re


# 引入本地文件
sys.path.append("..")

import py_import_wgds.lib.base as base

# 判断文件路径是否存在，若不存在则创建
def mkdir_path(path):
    if os.path.isdir(path):
        base.log('has dirs')
        return
    else:
        base.log(['create dirs', path])
        os.makedirs(path)

# 判断文件是否存在
def isFile(pathfile):
    if os.path.isfile(pathfile):
        return True
    else:
        return False
        # os.unlink(pathfile)

# 检查经纬度（限中国）
def check_lnglat_zh(lng, lat):
    try:
        x = float(lng)
        y = float(lat)
    except:
        return False
    if x == 0 or y == 0:
        return False
    elif x < y:
        return False
    elif all([ 70 < x < 140 , 0 < y < 60]):
        return True
    else:
        return False

# 去除中文字符
def del_chinese(value):
    return re.sub(r'[^\x00-\x7f]', '', value)

# 检查入库值有效性
def check_value(value):
    if type(value) is list:
        if value:
            # 去重
            value = list(set(value))
            if value:
                # 去空值
                value = list(filter(lambda x: x != ' ', value))
                value = list(filter(lambda x: x != None, value))
            if value:
                return value
            else:
                return None
        else:
            return None
    elif type(value) is str:
        if any([value == 'None', value == '']):
            return None
        else:
            return value.replace(' ','').replace('"','')
    elif type(value) is float or type(value) is int:
        if value != 0:
            return value
        else:
            return None
    elif type(value) is dict:
        if value:
            return value
        else:
            return None
    return value