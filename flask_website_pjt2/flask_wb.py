from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "We will be so tired of winning and you shout please stop stop its too much winning"

app.run(host="0.0.0.0", port=5000)
