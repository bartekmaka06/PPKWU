#!/usr/bin/env python3
import http.server
import socketserver
import os
import json
from datetime import datetime
from urllib.parse import urlparse
from urllib.parse import parse_qs


#print('source code for "http.server":', http.server.__file__)

class web_server(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):

        print(self.path)
        o = urlparse(self.path)
        self.protocol_version = 'HTTP/1.1'
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=UTF-8")
        self.end_headers()            
        url = 'https://www.example.com/some_path?some_key=some_value'
        #parsed_url = urlparse(url)
        parsed_url = urlparse(self.path)

        params = parse_qs(parsed_url.query)
        if len(params)==2:
            num1=params['num1'][0]
            num2=params['num2'][0]

            self.wfile.write(num1.encode("UTF-8"))
            self.wfile.write(b"\n")
            self.wfile.write(num2.encode("UTF-8"))


        #self.wfile.write(b"Hello World!\n")
        # if self.path == '/':
        #     self.protocol_version = 'HTTP/1.1'
        #     self.send_response(200)
        #     self.send_header("Content-type", "text/html; charset=UTF-8")
        #     self.end_headers()            
        #     self.wfile.write(b"Hello World!\n")
        # elif self.path.startswith('/?str='):
        #     self.protocol_version = 'HTTP/1.1'
        #     self.send_response(200)
        #     self.send_header("Content-type", "text/html; charset=UTF-8")
        #     self.end_headers()       
            
        #     tab = self.path.split('/?str=')
        #     string = tab[1]
            

        #     uppercase_count = sum(1 for char in string if char.isupper())
        #     lowercase_count = sum(1 for char in string if char.islower())
        #     digit_count = sum(1 for char in string if char.isdigit())
        #     special_count = len(string)-uppercase_count-lowercase_count-digit_count

        #     show = str(uppercase_count) + " " + str(lowercase_count) + " " + str(digit_count) +" "+str(special_count)
        #     myList = [{"lowercase": lowercase_count, "uppercase": uppercase_count, "digits":digit_count, "special":special_count}]
        #     jsonString = json.dumps(myList, indent=4)

        #     self.wfile.write(jsonString.encode("UTF-8")) 

        # else:
        #     tab = self.path.split('/?str=')
    
# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()
