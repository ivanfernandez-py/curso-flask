from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    eventos = [
        {
            "nombre": "Boda",
            "cliente": "Juan",
            "invitados": 150
        },
        {
            "nombre": "Cumpleaños",
            "cliente": "María",
            "invitados": 50
        },
        {
            "nombre": "Evento empresarial",
            "cliente": "Carlos",
            "invitados": 300
        },
    ]
    return render_template(
        "index7.html",
        eventos = eventos
    )
    
app.run(debug=True)