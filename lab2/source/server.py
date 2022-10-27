#!/usr/bin/env python3
import http.server
import socketserver
import os
from datetime import datetime

#print('source code for "http.server":', http.server.__file__)

class web_server(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):

        print(self.path)
        
        if self.path == '/':
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=UTF-8")
            self.end_headers()            
            self.wfile.write(b"Hello World!\n")
            
        elif self.path == '/?cmd=time':
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=UTF-8")
            self.end_headers()       
            now = datetime.now()
            self.wfile.write(now.strftime("%H:%M:%S").encode("UTF-8"))     
        else:
           
            params = self.path.split('&')
            
            first = params[0]
            first = first[2:].split('=')
            second = params[1].split('=')
            
            first_name=first[0]
            first_val=first[1]
            second_name=second[0]
            second_val=second[1]
            
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=UTF-8")
            self.end_headers() 
            self.wfile.write(second_val.encode("UTF-8"))
            #if len(params) == 2 :
            #	cmd = param[0]
            #	str = param[1]
        
            #super().do_GET()
    
# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()
