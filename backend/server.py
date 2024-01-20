import os
from flask import Flask, send_from_directory
from flask_pymongo import PyMongo
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['MONGO_URI'] = os.environ['MONGO_URI']
mongo = PyMongo(app)

@app.route('/')
def base():
    return send_from_directory('../frontend', 'index.html')

@app.route('/<path:path>')
def home(path):
    return send_from_directory('../frontend', path)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)