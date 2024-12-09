from flask import Flask, request, jsonify,send_file
import requests
from flask_cors import CORS
app = Flask(__name__)

CORS(app)


class UserData:
    def __init__(self, username, name):
        self.username = username
        self.name = name
   
    
    def to_dict(self):
        return {
            'username': self.username,
            'name': self.name
        }


@app.route('/', methods=['POST'])
def api_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    payload = {
        'LoginForm[username]': username,
        'LoginForm[password]': password
    }
   
    