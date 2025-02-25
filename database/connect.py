import psycopg2

def connection_db():
    conn = psycopg2.connect(
        database="all_penjat",
        password="pass",
        user="user",
        host="localhost",
        port="5432"
    )
    return conn
print (connection_db)
