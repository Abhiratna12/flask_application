from flask import jsonify
import numpy as np
import jwt
import yaml

def get_config():
                
    try:
        with open(r"./config/config.yaml") as f:
            config= yaml.load(f,Loader=yaml.FullLoader)

        return config
    except Exception as e :
        raise "Issue with loading config file"
        

class helper():
    def __init__(self):
        self.config =get_config()
        self.secret_key=self.config["secret"]["secret_key"]
        self.algorithm=self.config["secret"]["algorithm"]

    # FUnction to generate random floatingpoint numbers 
    def generate_float(self):
        try:
            random_float= [np.random.uniform(0,1) for i in range(500)]
            return jsonify({"result":random_float})

        except Exception as e :
            return jsonify({"error":str(e)}),400
    # Function to generate JWT token
    def generate_token(self):
        payload = {'user': 'ml_engineer'}
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)