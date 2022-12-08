#!/usr/bin/env python3
from flask import Flask, request, jsonify
import re

app = Flask(__name__)


@app.route("/", methods=['POST'])
def main():
    request_json = request.get_json()
    inputStr = request_json.get("str")
    num1 = request_json.get("num1")
    num2 = request_json.get("num2")
    
    output={
        "str":inputStr,
        "num1":num1,
        "num2":num2

    }
    return output


app.run(port=4080, host='0.0.0.0')