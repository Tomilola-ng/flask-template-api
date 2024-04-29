from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hey there, please visit "/api" route to get started!'

@app.route('/api')
def about():
    return 'Welcome to API'
