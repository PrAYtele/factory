import psycopg2
def create_table():
    conn = psycopg2.connect(dbname="info", user="postgres",password="971213", host="127.0.0.1", port="5432")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE 维也纳酒店
           (keys SERIAL PRIMARY KEY,
           PRICE            char(2000),     
           ADDRESS          char(2000),
           SCORE            char(2000),
           id               char(2000),
           name             char(2000),
           picture         char(2000),
           xy               char(2000));''')
    conn.commit()
    conn.close()
create_table()