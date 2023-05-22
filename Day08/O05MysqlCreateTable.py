
import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", database="rakuten", port=3306)

cur = conn.cursor()

query = """
create table players (
plyid varchar(6) PRIMARY KEY,
plyName varchar(50) not null,
sport varchar(30) not null,
country varchar(30) not null,
acheivement varchar(30) not null
)
"""

cur.execute(query)

conn.close()
