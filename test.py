# from http.server import BaseHTTPRequestHandler, HTTPServer
# import time

# hostName = "localhost"
# hostPort = 9000

# class MyServer(BaseHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header("Content-type", "text/html")
#         self.end_headers()
#         self.wfile.write(bytes("<html><head><title>Title goes here.</title></head>", "utf-8"))
#         self.wfile.write(bytes("<body><p>This is a test.</p>", "utf-8"))
#         self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))
#         self.wfile.write(bytes("</body></html>", "utf-8"))

# myServer = HTTPServer((hostName, hostPort), MyServer)
# print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

# try:
#     myServer.serve_forever()
# except KeyboardInterrupt:
#     pass

# myServer.server_close()
# print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))

from templetes import Templetes
class myHtml(Templetes):
    def Randar(self):
        self.shadhin = "shadhin"
        self.username = "nathing"
        return self.templting("src/index")
s = myHtml()
print(s.Randar())