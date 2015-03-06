import pymysql as MySQLdb
import pystache
import codecs

db = MySQLdb.connect( host = "127.0.0.1", user = "root", passwd = "", db = "victor", charset = 'utf8' )
cursor = db.cursor()

sql = "select * from firms"
cursor.execute(sql)

r = cursor.fetchone()
ft = codecs.open( "firms.html", "r", "utf-8" )
_templ_res = ft.read()

while r is not None:
    res = pystache.render( _templ_res, {"company_name" :  r[1] } )
    print( res )
    r = cursor.fetchone()