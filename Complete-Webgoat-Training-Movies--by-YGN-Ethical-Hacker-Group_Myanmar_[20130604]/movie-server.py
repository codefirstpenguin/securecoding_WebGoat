import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler


HandlerClass = SimpleHTTPRequestHandler
ServerClass  = BaseHTTPServer.HTTPServer
Protocol     = "HTTP/1.0"

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 1337
server_address = ('0.0.0.0', port)

HandlerClass.protocol_version = Protocol
httpd = ServerClass(server_address, HandlerClass)

sa = httpd.socket.getsockname()
print ''''
 ..|||||   \'|| \'||\'  \'|\'     |      .|\'\'\'.|  \'||\'\'|.  
.|\'    ||   \'|. \'|.  .\'     |||     ||..  \'   ||   || 
||      ||   ||  ||  |     |  ||     \'\'|||.   ||...|\' 
\'|.     ||    ||| |||     .\'\'\'\'|.  .     \'||  ||      
 ||...||       |   |      .|.  .||. |\'....|\' .||.    

'''
print "Serving OWASP WebGoat Movies on HTTP on", sa[0], "port", sa[1], "..."
httpd.serve_forever()
