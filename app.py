from flask import Flask
app = Flask(__name__)

@app.route('/api/two-numbers', methods=['POST'])
def hello_world():
    return 'Hello, World!'