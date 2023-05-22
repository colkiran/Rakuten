
import  pymysql

# connection string
conn = pymysql.connect(host="localhost", user='root', password="", port=3306)

cursor = conn.cursor()

query = "create database rakuten"

cursor.execute(query)

conn.close()