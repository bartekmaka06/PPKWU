#!/usr/bin/env python3
from flask import Flask, request, jsonify
import re

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
    return{
        "sum": num1+num2,
        "sub":num1-num2,
        "mul":num1*num2,
        "div":num1//num2,
        "mod":num1%num2
    }

def calculateAll(ss: str,num1:int,num2:int):
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
    request_json = request.get_json()
    inputStr = request_json.get("str")
    num1 = request_json.get("num1")
    num2 = request_json.get("num2")
    
    if inputStr is not None and num1 is not None and num2 is not None:
        output = calculateAll(inputStr,num1,num2)
    else:
        if num1 is not None and num2 is not None:
            output = calculateNumbers(num1,num2)
        else:
            output=calculateString(inputStr)

    return output


app.run(port=4080, host='0.0.0.0')