from http.server import HTTPServer, CGIHTTPRequestHandler
server_data = ("Localhost",8080)
server = HTTPServer(server_data, CGIHTTPRequestHandler)
server.serve_forever()
1 333

333333