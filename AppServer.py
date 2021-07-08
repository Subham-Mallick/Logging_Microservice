from flask import Flask, jsonify, request
import json
import sys
import os
import inspect
from datetime import datetime
from customLog import produceLog
import time

app = Flask(__name__)
portNo = 0
begin =0
levels = {
    0:"DEBUG",
    1:"INFO",
    2:"WARNING",
    3:"ERROR",
}

def sendLog(message, level):
    timestamp = datetime.now().strftime("%m/%d/%Y-%H:%M:%S")
    message = {'logLevel':levels[level],
                'message':message,
                'logCreated':timestamp}
    produceLog(message)
    return jsonify(message)


@app.route("/")
def root():
    p = sendLog("Running on PID: {}".format(os.getpid()),0)
    return ""

# @app.before_request
# def before():
#     begin = time.time()
#     sendLog("Started on PID: {}".format(os.getpid()),0)

# @app.after_request
# def after(response):
#     end = time.time()
#     sendLog("Left PID: {} in {} seconds".format(os.getpid(),end-begin),0)
#     return response


@app.route("/insert", methods = ['POST'])
def insert():
    message = request.data
    return sendLog(message.decode(),1)

if __name__ == "__main__":
    portNo = sys.argv[1]
    app.run(port=portNo)