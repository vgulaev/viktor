import pymysql as MySQLdb
#db = "vg_site_db"
db = MySQLdb.connect( host = "127.0.0.1", user = "root", passwd = "", charset = 'utf8' )
cursor = db.cursor()

sql = "CREATE DATABASE IF NOT EXISTS victor"
cursor.execute(sql)
db.commit()

db = MySQLdb.connect( host = "127.0.0.1", user = "root", passwd = "", db = "victor", charset = 'utf8' )
cursor = db.cursor()
sql = "CREATE TABLE t (c CHAR(20) CHARACTER SET utf8 COLLATE utf8_bin);"
cursor.execute(sql)
db.commit()