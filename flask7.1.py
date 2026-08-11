from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    eventos = [
    {
        "nombre": "Boda",
        "cliente": "Juan",
        "invitados": 150,
        "confirmado": True
    },
    {
        "nombre": "Cumpleaños",
        "cliente": "María",
        "invitados": 50,
        "confirmado": False
    },
    {
        "nombre": "Evento empresarial",
        "cliente": "Carlos",
        "invitados": 300,
        "confirmado": True
    },
]
    return render_template(
        "index8.html",
        eventos = eventos)

    
app.run(debug=True)