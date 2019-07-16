
# -*- coding: utf-8 -*-
import sys
import os
import time
import psycopg2

# 引入本地模块
sys.path.append('..')
import py_import_wgds.lib.base as BASE

# 数据库操作相关

CONN = None
CUR = None

# 链接数据库
def connServer(db_name,user,pwd,host,port):
    global CONN
    global CUR
    try:
        CONN = psycopg2.connect(dbname=db_name, user=user,
                                password=pwd, host=host, port=port)
    except Exception as e:
        BASE.log(["数据库连接失败！！！", e])
        sys.exit()
    CUR = CONN.cursor()
    BASE.log('数据库连接成功')

# 断开数据库，使用完数据库后必须断开，程序异常退出也要断开链接
def close_fun():
    CUR.close()
    CONN.close()

# 验证表是否存在，表名均为小写
def table_verify(table_name):
    sql = "select count(*) from pg_class where relname = '"+ table_name.lower() + "'"
    return sql

# 检查表是否存在
def check_schema(schema_name):
    verify_1 = table_verify(schema_name)
    CUR.execute(verify_1)
    verify_1_result = CUR.fetchone()[0]
    if verify_1_result == 0:
        BASE.log(['当前表:',schema_name,'不存在,请创建。。。'])
        return False
    else:
        BASE.log(['当前表:',schema_name,'已存在'])
        return True

# 创建插入语句
def create_insert_sql(schema_name, parm):
    return "INSERT INTO "+schema_name+ parm

# 创建更新编辑语句
def create_update_edit(schema_name):
    return "UPDATE "+schema_name + " set modifier=%s,state=%s,version=%s,create_time=%s,update_time=%s where modifier is null"

def up_edit(update_sql, parm):
    try:
        CUR.execute(update_sql, parm)
        CONN.commit()
    except Exception as e:
        BASE.log(["入库警告", e])
        CONN.rollback()
        close_fun()
        sys.exit()
