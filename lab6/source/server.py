#!/usr/bin/env python3
from flask import Flask, request, jsonify
import re
from dict2xml import dict2xml
import xmltodict

app = Flask(__name__)

def calculateString(ss: str):
    uppercase_count = sum(1 for char in ss if char.isupper())
    lowercase_count = sum(1 for char in ss if char.islower())
    digit_count = sum(1 for char in ss if char.isdigit())
    special_count = len(ss)-uppercase_count-lowercase_count-digit_count
    return{
        "lowercase": lowercase_count,
        "uppercase": uppercase_count,
        "digits": digit_count,
        "special": special_count
    }

def calculateNumbers(num1:int,num2:int):
    num1 = int(num1)
    num2 = int(num2)
    return{
        "sum": num1+num2,
        "sub":num1-num2,
        "mul":num1*num2,
        "div":num1//num2,
        "mod":num1%num2
    }

def calculateAll(ss: str,num1:int,num2:int):
    num1 = int(num1)
    num2 = int(num2)
    uppercase_count = sum(1 for char in ss if char.isupper())
    lowercase_count = sum(1 for char in ss if char.islower())
    digit_count = sum(1 for char in ss if char.isdigit())
    special_count = len(ss)-uppercase_count-lowercase_count-digit_count
    return{
        "lowercase": lowercase_count,
        "uppercase": uppercase_count,
        "digits": digit_count,
        "special": special_count,
        "sum": num1+num2,
        "sub":num1-num2,
        "mul":num1*num2,
        "div":num1//num2,
        "mod":num1%num2
    }

@app.route("/", methods=['POST'])
def main():
    xml_req = xmltodict.parse(request.get_data("root"))
    root = xml_req.get("root")
    if root is not None:
        xml_req= xml_req["root"]
    mystr = xml_req.get("str")
    num1 = xml_req.get("num1")
    num2 = xml_req.get("num2")
    
    if mystr is not None and num1 is not None and num2 is not None:
        output = calculateAll(mystr,num1,num2)
    else:
        if num1 is not None and num2 is not None:
            output = calculateNumbers(num1,num2)
        else:
            output=calculateString(mystr)

    xml_out = {}
    xml_out["root"] = output
    out = ('<?xml version="1.0"encoding="UTF-8"?>\n' + dict2xml(xml_out)).encode('utf-8')
    return out


app.run(port=4080, host='0.0.0.0')