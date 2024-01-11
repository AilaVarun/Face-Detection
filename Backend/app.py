# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 23:11:20 2024

@author: Laxmi Narayana
"""
from flask import Flask

app=Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, world2"
    

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
    app.run(debug=True)
    