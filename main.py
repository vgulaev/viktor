from http.server import HTTPServer, CGIHTTPRequestHandler

def Run(server, request):
	server_address = ( "127.0.0.1", 8081 )
	httpd = server( server_address, request )
	httpd.serve_forever()
	
Run(HTTPServer, CGIHTTPRequestHandler)
