from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import datetime
import urllib

class HTTPRequestHandler( BaseHTTPRequestHandler ):
    def do_GET( self ):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        o = urllib.parse.urlparse( self.path )
        f = open( "hello.html", "rb" )
        ans = f.read()
        ans1 = """
        привет
        """
        #bs = bytes( ans, "utf-8" )
        self.wfile.write( ans )
        print( o.path )

def run( server_class = HTTPServer, handler_class = HTTPRequestHandler ):
    server_address = ( "127.0.0.1", 8080 )
    httpd = server_class( server_address, handler_class )
    httpd.serve_forever()

if __name__ == '__main__':
    print( "Start at {date}".format(date = datetime.datetime.now()) )
    run()