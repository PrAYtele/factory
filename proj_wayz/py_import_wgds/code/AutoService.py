
# -*- coding: utf-8 -*-
import sys


# 引入本地模块
sys.path.append('..')
import py_import_wgds.lib.base as BASE
import py_import_wgds.lib.check as CHECK
import py_import_wgds.lib.sql as SQL

# ！！！！！！！！！！
# 按需要引入模型配置 , 按需更改
# ！！！！！！！！！！
import py_import_wgds.config.AutoService as CONFIG

# 入库food

# 数据库名称 , 按需更改
pg_dp_shop_db = 'py_brand_wgds_0709'
#pg_dp_shop_db = 'ttt'
# 要存入的表
schema_name = 'AutoService'

if __name__ == '__main__':
    start = BASE.get_time()[0]
    
    if CHECK.isFile(CONFIG.result_file) is False:
        BASE.log(['文件不存在：', CONFIG.result_file])
        sys.exit()

    # # 数据库名称， 用户名， 密码， ip， 端口
    # 按需更改
    #SQL.connServer(pg_dp_shop_db,'postgres','aimap2017','127.0.0.1','5432')
    SQL.connServer(pg_dp_shop_db,'postgres','wayzpg@1234','172.3.0.107', '5432')

    if SQL.check_schema(schema_name) is False:
        sys.exit()

    BASE.log(['db:',pg_dp_shop_db,'schema:', schema_name, 'processing ...'])

    insert_sql = SQL.create_insert_sql(schema_name, CONFIG.insert_sql)
    CONFIG.main(insert_sql)

    # 更新编辑信息
    update_sql = SQL.create_update_edit(schema_name)
    edit_time = BASE.get_time()[1]
    SQL.up_edit(update_sql, (CONFIG.edit_user,'add',CONFIG.edit_version,edit_time,edit_time ) )

    SQL.close_fun()

    end = BASE.get_time()[0]
    BASE.log(['db:',pg_dp_shop_db,'schema:',schema_name, 'success over, 耗时: ', str((end - start)/60), "分钟,未入库:", CONFIG.warn_count])
