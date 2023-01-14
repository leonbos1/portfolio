import json
from flask import Flask, request, jsonify
import sqlite3
import datetime
from flask_cors import CORS
from flask_restful import Resource, Api, marshal_with, fields
from sqlalchemy import *
from flask_sqlalchemy import SQLAlchemy
import os
from functools import wraps
import jwt
import string
import random
import time
from time import sleep
import math


app = Flask(__name__)
api = Api(app)
CORS(app)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'portfoliodb.db')
app.config['SECRET_KEY'] = 'secretkey'
regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
db = SQLAlchemy(app)

class Log(db.Model):
    __tablename__ = 'log'	
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.String(100))
    ip_address = db.Column(db.String(100))
    user_agent = db.Column(db.String(100))

log_fields = {
    'id': fields.Integer,
    'datetime': fields.String,
    'ip_address': fields.String,
    'user_agent': fields.String
}

@app.route('/log', methods=['GET'])
@marshal_with(log_fields)
def get_log():
    logs = Log.query.all()
    return logs

@app.route('/log', methods=['POST'])
def add_log():
    datetime = time.strftime('%Y-%m-%d %H:%M:%S')
    ip_address = request.remote_addr

    if ip_address == '82.72.126.62':
        ip_address = 'None'

    try:
        user_agent = request.headers['User-Agent']
    except:
        user_agent = 'None'
    log = Log(datetime=datetime, ip_address=ip_address, user_agent=user_agent)
    db.session.add(log)
    db.session.commit()
    return "Success", 200

@app.route('/visitors', methods=['get'])
def get_visitors():
    #returns an int of the amount of visitors
    visitors = len(Log.query.all())
    obj = {'visitors': visitors}

    return jsonify(obj), 200

if __name__ == "__main__":
    while True:
        try:
            with app.app_context():
                db.create_all()
            app.run(host="192.168.178.220", port=5050,
                    debug=False, threaded=True)
        except Exception as e:
            sleep(10)
