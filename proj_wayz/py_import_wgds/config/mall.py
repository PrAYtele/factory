
# -*- coding: utf-8 -*-

import os
import sys

# 引入本地文件
sys.path.append("..")

import py_import_wgds.lib.check as CHECK
import py_import_wgds.lib.coordTransform as CTF
import py_import_wgds.lib.base as BASE
import py_import_wgds.lib.sql as SQL

param_info = []

# 数据入库
def start_into_pg(insert_sql, param_info):
    try:
        # CUR.execute(insert_sql, param_info)
        SQL.CUR.executemany(insert_sql, param_info)
        SQL.CONN.commit()
        param_info = []
    except Exception as e:
        BASE.log(["入库警告", e])
        SQL.CONN.rollback()
        SQL.close_fun()
        sys.exit()

# 异常未入库统计
warn_count = 0
# 不允许修改
insert_sql = " (name,code,category_ids,category_names,image_urls,brands,opening_hours,phone_numbers,website,chains,postcode,business_area,address,price,\
            overall_rating,stars,facility_rating,service_rating,environment_rating,recommend_rating,hit_total_count,hit_monthly_count,\
            comment_count,customized_id,source_ids,geometry) \
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,ST_PointFromText('POINT(%s %s)', 4326))"
# 版本信息，按需更改
edit_version = 'v0.1' #数据版本
data_src = 'office' #数据源
edit_user = 'shawn'  #入库人


# 允许修改字段对应值， 字段映射, 按需更改
def insert_info(row):
    global param_info
    global warn_count

    # 无值时一律填 None

    name = CHECK.check_value(row[1])  #必填 字符串
    code = None #可选 行政区划ID
    category_ids = [40100] #必填 整型数组
    category_names = ['商场'] #必填 字符串数组
    image_urls = CHECK.check_value([row[45].split('%')[0]]) #可选 字符串数组
    brands = None #可选 整型数组 品牌ID
    opening_hours = CHECK.check_value(row[30]) #可选 字符串
    phone_numbers = [] # 可选 字符串数组
    if row[18] != '':
        phone_numbers.append(row[18])
    if row[19] != '':
        phone_numbers.append(row[19])
    phone_numbers = CHECK.check_value(phone_numbers)
    website = None # 可选 字符串
    chains = None # 可选 bool类型
    postcode = None #可选 整型
    business_area = CHECK.check_value(row[8]) # 可选 字符串
    address = CHECK.check_value(row[2]) # 必填 字符串
    price = CHECK.check_value(row[37]) #可选 整型
    overall_rating = None # 可选 浮点 整体评分
    stars = CHECK.check_value(int(row[36])/10) # 可选 浮点 最高5星
    facility_rating = CHECK.check_value(row[42]) #可选 浮点 设施评分
    service_rating = CHECK.check_value(row[44]) #可选 浮点 服务评分
    environment_rating = CHECK.check_value(row[43]) #可选 浮点 环境评分
    recommend_rating = None #可选 浮点 推荐指数
    hit_total_count = CHECK.check_value(row[47]) #可选 整型
    hit_monthly_count = CHECK.check_value(row[51]) #可选 整型
    comment_count = CHECK.check_value(row[56]) #可选 整型 评论总数
    customized_id = CHECK.check_value(row[0]) #必填 原始ID 字符串
    source_ids = [data_src+":"+edit_version+ customized_id ] # 必填 来源+v0.1+原始ID 字符串数组
    lng = float(row[3]) #必填 火星坐标 浮点
    lat = float(row[4]) #必填 火星坐标 浮点

    # 必须验证
    if CHECK.check_lnglat_zh(lng, lat) is False:
        warn_count += 1
        return param_info
    # 不允许改
    param_info.append([name,code,category_ids,category_names,image_urls,brands,opening_hours,phone_numbers,website,chains,postcode,business_area,address,price,\
            overall_rating,stars,facility_rating,service_rating,environment_rating,recommend_rating,hit_total_count,hit_monthly_count,\
            comment_count,customized_id,source_ids,lng,lat])

    return param_info
