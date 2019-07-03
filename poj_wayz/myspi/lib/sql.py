import psycopg2
def postgre():
    conn = psycopg2.connect(dbname="info", user="postgres", password="971213", host="127.0.0.1", port="5432")
    cur = conn.cursor()
    return conn