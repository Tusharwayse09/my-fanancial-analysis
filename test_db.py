import pymysql

print("TRYING TO CONNECT...")

conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="finance",
    port=3306,
    connect_timeout=5
)

print("CONNECTED SUCCESSFULLY ✅")
conn.close()
