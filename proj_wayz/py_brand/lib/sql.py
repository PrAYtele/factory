import psycopg2
def postgre():
    conn = psycopg2.connect(dbname="py_brand_wgds_0709",
                user="postgres",
                password="wayzpg@1234",
                host="172.3.0.107",
                port="5432")
    return conn