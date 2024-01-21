import os
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_pymongo import PyMongo
from dotenv import load_dotenv
from services.chat_bot import flirt_respond, evaluate_rizz
from flask_cors import CORS
load_dotenv()

app = Flask(__name__)

app.config['MONGO_URI'] = os.environ['MONGO_URI']
app.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET_KEY']

mongo = PyMongo(app)
jwt = JWTManager(app)
CORS(app)


@app.route('/')
def base():
    return 'Bad request'


@app.route('/chat', methods=['POST'])
@jwt_required()
def chat():
    try:
        message = request.json['message']
    except Exception as e:
        return jsonify({'error': f'Missing a message: {e}'}), 400
    history = None
    if 'history' in request.json:
        history = request.json['history']
    return jsonify({'msg': flirt_respond(message, message_history=history)}), 200

@app.route('/assess',methods=['POST'])
@jwt_required()
def assess():
    return jsonify({'score': evaluate_rizz(request.json['history'])})

@app.route('/signup', methods=['POST'])
def signup():
    user = request.json['email']
    pw = request.json['password']
    if not user or not pw:
        print(request.json)
        return jsonify({'error': 'Bad username or password'}), 401
    mongo.db.users.insert_one({'email': user, 'password': pw})
    access_token = create_access_token(identity=user)
    return jsonify(access_token=access_token), 201


@app.route('/login', methods=['POST'])
def login():
    user = request.json['email']
    pw = request.json['password']
    if not user or not pw:
        return jsonify({'error': 'Bad username or password'}), 401
    data = mongo.db.users.find_one({'email': user, 'password': pw})
    if not data:
        return jsonify({'error': 'Bad username or password'}), 401
    access_token = create_access_token(identity=user)
    return jsonify(access_token=access_token), 200


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)
