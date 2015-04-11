from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import datetime
import urllib
import time
import json


class HTTPRequestHandler( BaseHTTPRequestHandler ):
    def get_postdata( self ):
        self.send_response(200)
        self.send_header( "Content-type", "application/json" )
        self.end_headers()
        length = int( self.headers[ "Content-Length" ] )
        res = urllib.parse.parse_qs( self.rfile.read( length ).decode( "utf-8" ) )
        return res
    def do_POST( self ):
        post_data = self.get_postdata()
        print( post_data )
        ans = json.dumps( { "mes" : "I'm alive" })
        bs = bytes( ans, "utf-8" )
        self.wfile.write( bs )
    def ans_like_text_file( self, filename, contenttype ):
            if os.path.isfile( filename ):
                self.send_response( 200 )
                self.send_header( "Content-type", contenttype )
                exptime = time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime( time.time() + 60 * 60 ) )
                self.send_header( "expires", exptime )
                self.send_header( "cache-control", "public, max-age=86400" )
                #sebslf.send_header( "Last-Modified", common.env[ "HTTP-Modified-Since" ] )
                self.end_headers()
                f = open( filename, "r" )
                ans = f.read( )
                bs = bytes( ans, "utf-8" )
                #bs = 0/0
                self.wfile.write( bs )
            else:
                self.ans_like_404()
    def do_GET( self ):
        o = urllib.parse.urlparse( self.path )
        path = o.path
        if path[ -3: ] == ".js":
            self.ans_like_text_file( path[ 1: ], "text/javascript" )
        else:
            f = open( "index.html", "r" )
            ans = f.read()
            bs = bytes( ans, "utf-8" )
            self.wfile.write( bs )

def run( server_class = HTTPServer, handler_class = HTTPRequestHandler ):
    server_address = ( "127.0.0.1", 8080 )
    httpd = server_class( server_address, handler_class )
    httpd.serve_forever()

if __name__ == '__main__':
    print( "Start at {date}".format(date = datetime.datetime.now()) )
    run()