from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_www():
    return "Hello World Wide Web! I'm testing Poll SCM on Jenkikns."
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
