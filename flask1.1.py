# CHALLENGE: Different Routes

from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Hola, estoy aprendiendo flask."

@app.route("/producto")
def producto():
    return "Hola, esto es un producto."

app.run(debug=True)