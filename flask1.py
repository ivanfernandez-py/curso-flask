from flask import Flask

app = Flask(__name__)

@app.route("/")

def inicio():
    return "Mi primer servidor en Flask"

app.run(debug=True)