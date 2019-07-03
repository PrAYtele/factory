import psycopg2
def create_table():
    conn = psycopg2.connect(dbname="info", user="postgres",password="971213", host="127.0.0.1", port="5432")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE wyn_hotel
           (keys SERIAL PRIMARY KEY,
           PRICE            int ,     
           ADDRESS          varchar,
           star           float,
           source_id        int,
           name             varchar,
           picture         varchar,
           x               varchar ,
           y                varchar ,
           sale             varchar,
           equip            varchar,
           category_ids             integer[] ,
           xy_status        int   );''')
    conn.commit()
    conn.close()
create_table()