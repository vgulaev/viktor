import requests
import codecs

r = requests.get( "http://yandex.ru" )

f = codecs.open( "ans.html", "w", "utf-8" )
f.write( r.text )