from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def base():
    return send_from_directory('../frontend', 'index.html')

@app.route('/<path:path>')
def home(path):
    return send_from_directory('../frontend', path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)