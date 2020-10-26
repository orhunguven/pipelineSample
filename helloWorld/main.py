from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_www():
    return "Hello World Wide Web! I'm testing Poll SCM on Jenkikns."
