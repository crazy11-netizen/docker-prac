from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    with open('/data/notes.txt', 'a') as f:
        f.write("shivashankar\n")

    return "Saved note"
app.run(host="0.0.0.0", port = 5000)
