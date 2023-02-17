import requests as requests
from flask import Flask, request, render_template
import pickle
import json
import socket
app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    return "Hello World"

@app.route('/login', methods=['POST'])
def login():
    username = request.get_json()['username']
    password = request.get_json()['password']
    print("Hello World")
    print("request data 1-{} 2-{} ".format(username, password))
    f = open('db.json')
    data = json.load(f)
    data = data['Users']
    for obj in data:
        if username == obj['ShortName']:
            if password == obj['Password']:
                return app.response_class(status=200)
    return app.response_class(status=400)

if __name__ == '__main__':
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print("My IP address is:", ip_address)
    app.run(host='0.0.0.0', port=5000)
