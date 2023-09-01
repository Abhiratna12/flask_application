from flask import Flask,jsonify,request,Blueprint
import numpy as np
from helper import helper
import logging
import os
import jwt
from functools import wraps

logging.basicConfig(level=logging.DEBUG,
                   format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(os.getpid()),
                   datefmt='%Y-%m-%d %H:%M:%S',
                   handlers=[logging.StreamHandler()])


config=helper.get_config()
helper= helper.helper()
logger = logging.getLogger()

# Authentication decorator
def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'error': 'Missing authorization token'}), 401

        try:
            token = auth_header.split()[1]
            jwt.decode(config["token"], config["secret_key"], algorithms=config["algorithms"])
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token has expired'}), 401
        except (jwt.InvalidTokenError, IndexError):
            return jsonify({'error': 'Invalid token'}), 401

        return func(*args, **kwargs)

    return wrapper

app=Flask(__name__)

@app.route("/api/",methods=["GET"])
@authenticate
def home():
    logger.info("### Welcome to get_float function ###")
    
    return "<h1>"+"### Welcome to get_float function ##"+"<h1>"

@app.route("/api/get_float",methods=["GET","POST"])
@authenticate
def get_float():
    logger.info("### Into get_float function ##")
    text= request.args.get('text')
    if (text):
        json_array= helper.generate_float() ## function definition in helper/helper.py

    logger.info("### calculated get_float successfully ##")
    return json_array,200

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True,port=8008)