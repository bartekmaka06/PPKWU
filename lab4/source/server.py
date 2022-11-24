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
        parsed_url = urlparse(self.path)

        params = parse_qs(parsed_url.query)
        if len(params)==2:
            num1=params['num1'][0]
            num2=params['num2'][0]
            num1=int(num1)
            num2=int(num2)
            myList = [{"sum": int(num1+num2),
                        "sub": int(num1-num2), 
                        "mul": int(num1*num2), 
                        "div":int(num1/num2),
                        "mod":int(num1%num2)}]
            jsonString = json.dumps(myList, indent=4)
            self.wfile.write(jsonString.encode("UTF-8")) 
            print("hello")
            print(jsonString)
    
# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()
