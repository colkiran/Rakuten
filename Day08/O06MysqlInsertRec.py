
import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", database="rakuten", port=3306)

cur = conn.cursor()

FL = open("sqlStatement.txt", "r")

lines = FL.readlines()

for line in lines:
    cur.execute(line)

conn.commit()
FL.close()
conn.close()

