
# -*- coding: utf-8 -*-

import sys

# 引入本地模块
sys.path.append('..')
import py_import_wgds.lib.base as BASE
import py_import_wgds.lib.check as CHECK
import py_import_wgds.lib.sql as SQL
import py_import_wgds.lib.schema_config as SC_FIG


''' 
    本模块用于生成WGDS规范里Enity下的各个Schema表单
    1，输入要创建的表单，
    2，判断该表单是否存在于规范
        若存在
            数据库已有该表单则跳过创建
            数据库无该表单则创建
        若不存在
            跳过该表单，并在控制台输出该表单名称，提示错误信息
'''


# 检查配置文件是否存在
def check_file(file):
    if CHECK.isFile(file) is False:
        CHECK.log(['文件路径不存在：', file])
        sys.exit()

def init_schema(schema_list, wgds_schema):
    for table_name in schema_list:
        config_schema = SC_FIG.inSchema(table_name, wgds_schema)
        if config_schema is False :
            BASE.log(['当前表: ', table_name, ' 未在配置表中'])
            continue

        if SQL.check_schema(table_name):
            continue
        
        create_sch_info = SC_FIG.create_sql(config_schema, wgds_schema)
        SQL.CUR.execute(create_sch_info['sql'])
        SQL.CONN.commit()

        BASE.log([table_name, create_sch_info['count'] ])

''' 
WGDS 0709日 全部Entity表单

"Airport" "AutoService" "Bank" "Venue" "Chemist" "College" "Education" "EnergyStation" "Entertainment" "Entity" "Factory" 
"Farm" "Food" "ForeignInstitution" "Government" "Hall" "Health" "Hospital" "Hotel" "Institute" "Kindergarten" "Mall" 
"Market" "Mine" "Office" "Organization" "Park" "Parking" "Pet" "Port" "Residential" "RoadEntrance" "Scenic" "School" 
"Service" "ServiceArea" "Shop" "Sports" "Station" "Supermarket" "Theater" "Toll" "Tower"

'''

# WGDS规格的Schema配置文件
config_schema_path = 'lib/wayz_dianping.json'

# 要创建的表单, 按需更改
schema_list = ["Bank","Mall","Food"]

if __name__ == "__main__":

    check_file(config_schema_path)

    wgds_schema = BASE.load_json_file(config_schema_path)

    # 数据库名称， 用户名， 密码， ip， 端口
    # 按需更改
    # connServer('py_brand_wgds_0709','postgres','wayzpg@1234','172.3.0.107','5432')
    SQL.connServer('info','postgres','971213','127.0.0.1','5432')

    init_schema(schema_list, wgds_schema)

    SQL.close_fun()

    BASE.log(['\n!!! success over !!!\n'])
