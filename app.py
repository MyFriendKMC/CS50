from flask import Flask
#LOL make sure you put a capital F.

app = Flask(__name__)

@app.route("/")
def index():
    return 'Hello world'

@app.route("/Kyle")
def kyle():
    return "Hello Kyle"

@app.route("/John")
def john():
    return "Hello John"
