import psycopg2

def connection_db():
    conn = psycopg2.connect(
        database="all_penjat",
        user="user",
        password="pass",
        host="localhost",
        port="5432"
    )
    return conn

connect = connection_db
print(connect)
