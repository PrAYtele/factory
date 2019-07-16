
# -*- coding: utf-8 -*-


# 判断模型表是否在配置文件
def inSchema(table, configs):
    schemaArr = configs['entity']['schemas']
    for value in schemaArr:
        if value['table'] == table:
            return value
    return False

# 创建表
def create_sql(pg_info, schema_config):
    name = pg_info['table']
    common_field = schema_config['common_field']
    
    sql = 'create table if not exists '+name +' ( '
    count_field = 0

    place= common_field['place']
    count_field += len(place)
    for value in place:
        sql += value['name'] + ' ' +value['type'] + ', '

    entity= schema_config['entity']['common_field']
    count_field += len(entity)
    for value in entity:
        sql += value['name'] + ' ' +value['type'] + ', '

    process= common_field['process']
    count_field += len(process)
    for value in process:
        sql += value['name'] + ' ' +value['type'] + ', '
    
    address= common_field['address']
    count_field += len(address)
    for value in address:
        sql += value['name'] + ' ' +value['type'] + ', '

    fields = pg_info['fields']
    count_field += len(fields)
    for value in fields:
        sql += value['name'] + ' ' +value['type'] + ', '


    edition= common_field['edition']
    count_field += len(edition)
    for value in edition:
        sql += value['name'] + ' ' +value['type'] + ', '
    
    sql = sql[:-2]
    sql += ' )'
    return {'sql':sql, 'count': count_field}
