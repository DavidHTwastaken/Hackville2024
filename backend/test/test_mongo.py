import os
from flask_pymongo import PyMongo
from flask import Flask, jsonify
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/hackville2024"
mongo = PyMongo(app)

@app.route('/test',methods=['POST'])
def test():
    mongo.db.people.insert_one({'name': 'Jakob'})
    data = mongo.db.people.find_one({'name':'Jakob'})
    return jsonify({'data':str(data)}), 200

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)
