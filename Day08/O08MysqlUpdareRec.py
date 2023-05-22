
import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", database="rakuten", port=3306)

cur = conn.cursor()

query = "update players set plyName = 'Pusarla Venkata Sindhu' where plyid = 'PLY05'"

cur.execute(query)

conn.commit()

conn.close()

