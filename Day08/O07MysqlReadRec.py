
import pymysql
from prettytable import from_db_cursor

conn = pymysql.connect(host="localhost", user="root", password="", database="rakuten", port=3306)

cur = conn.cursor()

query = "select * from players"

cur.execute(query)

pt = from_db_cursor(cur)

# for row in cur.fetchall():
#     print(row)

conn.close()

print(pt)