
# -*- coding: utf-8 -*-

import os
import sys
from tqdm import tqdm

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
insert_sql = " (name,name_en,code,category_ids,category_names,image_urls,brands,opening_hours,phone_numbers,website,chains,postcode,business_area,address,price,\
            overall_rating,stars,facility_rating,service_rating,environment_rating,taste_rating,product_rating,\
            comment_count,customized_id,source_ids,geometry) \
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,ST_PointFromText('POINT(%s %s)', 4326))"

# 版本信息，按需更改
edit_version = 'v0.1' #数据版本
data_src = 'office' #数据源
edit_user = 'rui.hou'  #入库人

# 读取的文件, 按需更改
result_file = 'E:/py_brand/data/out_data/xlk.json'

#  按需更改
def main(insert_sql):
    # ipt_data = list(BASE.read_csv(result_file))
    ipt_data = BASE.load_json_file(result_file)['data']['list']
    ipt_len = len(ipt_data)

    pbar = tqdm(total=ipt_len)

    for row in ipt_data:
        pbar.update(1)
        param_info = insert_info(row)
        if len(param_info) == 5000:
            # 数据入库
            start_into_pg(insert_sql, param_info)
    if len(param_info):
        # 数据入库
        start_into_pg(insert_sql, param_info)
    pbar.close()


# 允许修改字段对应值， 字段映射, 按需更改

def insert_info(row):
    global param_info
    global warn_count

    # 无值时一律填 None

    name = CHECK.check_value(row.get('store_title', None)).replace('（','(').replace('）',')') #必填 字符串
    name_en = None #可选 字符串
    code = None #可选 行政区划ID
    category_ids = [30101] #必填 整型数组 类别ID，参考WGDS规范
    category_names = ['中餐'] #必填 字符串数组 与category_ids对应
    image_urls = None #可选 字符串数组
    brands = [62600120] #必填 整型数组 品牌ID
    opening_hours = CHECK.check_value(row.get('business_hours', None)) #可选 字符串
    phone_numbers = [] # 可选 字符串数组
    phone_numbers.append( CHECK.check_value( CHECK.del_chinese(row.get('store_phone', '').replace(' ','')) ) )
    phone_numbers = CHECK.check_value(phone_numbers)
    website = None # 可选 字符串
    chains = True # 可选 bool类型
    postcode = None #可选 整型
    business_area = None # 可选 字符串
    address = CHECK.check_value(row.get('store_address', None)) # 必填 字符串
    price = None #可选 整型
    overall_rating = None # 可选 浮点 整体评分
    stars = None # 可选 浮点 最高5星
    facility_rating = None #可选 浮点 设施评分
    service_rating = None #可选 浮点 服务评分
    environment_rating = None #可选 浮点 环境评分
    taste_rating = None #可选 浮点 口味评分
    product_rating = None  #可选 浮点 产品评分
    comment_count = None #可选 整型 评论总数
    customized_id = CHECK.check_value(row.get('store_id', None))  #必填 原始ID 字符串
    source_ids = [data_src+":"+edit_version+ ':'+customized_id ] # 必填 来源+v0.1+原始ID 字符串数组

    try:
        lng = float(row.get('longitude1', None)) #必填 火星坐标 浮点
        lat = float(row.get('latitude1', None)) #必填 火星坐标 浮点
    except Exception as e:
        # BASE.log(['xy warning...', row])
        warn_count += 1
        return param_info

    xy = CTF.bd09_to_gcj02(lng, lat)
    if xy is False:
        warn_count += 1
        return param_info
    lng = xy[0]
    lat = xy[1]

    # 必须验证
    if CHECK.check_lnglat_zh(lng, lat) is False:
        warn_count += 1
        return param_info

    # 不允许改
    param_info.append([name,name_en,code,category_ids,category_names,image_urls,brands,opening_hours,phone_numbers,website,chains,postcode,business_area,address,price,\
            overall_rating,stars,facility_rating,service_rating,environment_rating,taste_rating,product_rating,\
            comment_count,customized_id,source_ids,lng,lat])

    return param_info
