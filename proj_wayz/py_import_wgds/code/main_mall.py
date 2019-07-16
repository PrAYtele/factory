
# -*- coding: utf-8 -*-
import sys
from tqdm import tqdm


# 引入本地模块
sys.path.append('..')
import py_import_wgds.lib.base as BASE
import py_import_wgds.lib.check as CHECK
import py_import_wgds.lib.sql as SQL

# ！！！！！！！！！！
# 按需要引入模型配置
# ！！！！！！！！！！
import py_import_wgds.config.mall as CONFIG

# 入库mall

def main(insert_sql):
    ipt_data = list(BASE.read_csv(result_file))
    # ipt_data = BASE.load_json_file(result_file)
    ipt_len = len(ipt_data)

    pbar = tqdm(total=ipt_len)

    for row in ipt_data:
        pbar.update(1)
        if len(row) == 0:
            continue
        if row[0] == 'shopId':
            continue
        param_info = CONFIG.insert_info(row)
        if len(param_info) == 5000:
            # 数据入库
            CONFIG.start_into_pg(insert_sql, param_info)
    if len(param_info):
        # 数据入库
        CONFIG.start_into_pg(insert_sql, param_info)
    pbar.close()

# 数据库名称
# pg_dp_shop_db = 'py_brand_wgds_0709'
pg_dp_shop_db = 'ttt'
# 要存入的表
schema_name = 'mall'
# 读取的文件
result_file = '/Users/liuxiao/Desktop/GE/Maps-Platform/py_dianping/dp_mall/result_data/北京_mall_0618.csv'


if __name__ == '__main__':
    start = BASE.get_time()[0]
    
    if CHECK.isFile(result_file) is False:
        BASE.log(['文件不存在：', result_file])
        sys.exit()

    # 数据库名称， 用户名， 密码， ip， 端口
    SQL.connServer(pg_dp_shop_db,'postgres','aimap2017','127.0.0.1','5432')
    # SQL.connServer(pg_dp_shop_db,'postgres','wayzpg@1234','172.3.0.107', '5432')

    if SQL.check_schema(schema_name) is False:
        sys.exit()

    BASE.log(['db:',pg_dp_shop_db,'schema:', schema_name, 'processing ...'])

    insert_sql = SQL.create_insert_sql(schema_name, CONFIG.insert_sql)

    main(insert_sql)

    # 更新编辑信息
    update_sql = SQL.create_update_edit(schema_name)
    edit_time = BASE.get_time()[1]
    SQL.up_edit(update_sql, (CONFIG.edit_user,'add',CONFIG.edit_version,edit_time,edit_time ) )

    SQL.close_fun()

    end = BASE.get_time()[0]
    BASE.log(['db:',pg_dp_shop_db,'schema:',schema_name, 'success over, 耗时: ', str((end - start)/60), "分钟,未入库:", CONFIG.warn_count])
