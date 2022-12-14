#!/usr/bin/env python3
import http.server
import socketserver
import os
import json
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
        elif self.path.startswith('/?str='):
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=UTF-8")
            self.end_headers()       
            
            tab = self.path.split('/?str=')
            string = tab[1]
            

            uppercase_count = sum(1 for char in string if char.isupper())
            lowercase_count = sum(1 for char in string if char.islower())
            digit_count = sum(1 for char in string if char.isdigit())
            special_count = len(string)-uppercase_count-lowercase_count-digit_count

            show = str(uppercase_count) + " " + str(lowercase_count) + " " + str(digit_count) +" "+str(special_count)
            myList = [{"lowercase": lowercase_count, "uppercase": uppercase_count, "digits":digit_count, "special":special_count}]
            jsonString = json.dumps(myList, indent=4)

            self.wfile.write(jsonString.encode("UTF-8")) 

        else:
            tab = self.path.split('/?str=')
    
# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()
