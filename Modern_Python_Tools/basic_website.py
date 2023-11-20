from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my website!"

app.run(host='0.0.0.0')