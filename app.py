from flask import Flask
app = Flask(__name__)

@app.route('/login')
def login():
    return 'TODO!'

@app.route('/fetch', methods=['POST'])
def fetch():
    return 'TODO!'

@app.route('/taken', methods=['POST'])
def taken():
    return 'TODO!'
