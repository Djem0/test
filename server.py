from http.server import HTTPServer, CGIHTTPRequestHandler
server_data = ("Localhost", 8080)
server = HTTPServer(server_data, CGIHTTPRequestHandler)
server.serve_forever()
a = 333
b = 333333
