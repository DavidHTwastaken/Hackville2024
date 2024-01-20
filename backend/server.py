import os
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_pymongo import PyMongo
from dotenv import load_dotenv
from services.chat_bot import flirt_respond
from werkzeug.security import generate_password_hash, check_password_hash
load_dotenv()

app = Flask(__name__)

app.config['MONGO_URI'] = os.environ['MONGO_URI']
app.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET_KEY']

mongo = PyMongo(app)
jwt = JWTManager(app)


@app.route('/')
def base():
    return 'Bad request'


@app.route('/chat', methods=['POST'])
@jwt_required()
def chat():
    return jsonify({'msg': flirt_respond(request.form['message'])}), 200


@app.route('/signup', methods=['POST'])
def signup():
    user = request.json.get('user', None)
    pw = request.json.get('password', None)
    if not user or not pw:
        return jsonify({'error': 'Bad username or password'}), 401
    access_token = create_access_token(identity=user)
    return jsonify(access_token=access_token)


@app.route('/login', methods=['POST'])
def login():
    user = request.json['user']
    pw = request.json['password']
    if not user or not pw:
        return jsonify({'error': 'Bad username or password'}), 401
    data = mongo.db.find_one({'user': user, 'password': pw})
    if not data:
        return jsonify({'error': 'Bad username or password'}), 401
    access_token = create_access_token(identity=user)
    return jsonify(access_token=access_token), 201


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)
