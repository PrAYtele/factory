import json
import lib.sql as sql

with open('../data/out_data/SUBWAY.json', 'r') as f:
    data = json.load(f)

conn = sql.postgre()
cur = conn.cursor()
for i in range(len(data)):
    data[i]['TEL'].replace('"','')
    cur.execute("""INSERT INTO food (name,address,opening_hours,phone_numbers,source_ids,geometry )
                         VALUES (%s,%s,%s,%s,%s,ST_PointFromText('POINT(%s %s)', 4326));""", (
    data[i]['ShopNameCN'], data[i]['Address'],data[i]['StoreHours'], [data[i]['TEL']],['office:v0.1:'+data[i]['ShopID']],float(data[i]['BaiduLon']),float(data[i]['BaiduLat'])), )
    conn.commit()
conn.close()