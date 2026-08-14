from flask import Flask, url_for, redirect, request, render_template

app = Flask(__name__)

evento = {
    "cliente": "Ivancho",
    "telefono": "6143635380",
    "ordenes": 150,
    "fecha": "15 de octubre",
    "hora": "18:00",
    "ubicacion": "Quinta Fulanita"
}

@app.route("/")
def inicio():
    return render_template(
        "index16.html",
        evento = evento
    )

app.run(debug=True)