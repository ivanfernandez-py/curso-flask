from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

eventos = [{
    "cliente": "Ivancho",
    "telefono": "6143635380",
    "ordenes": 150,
    "fecha": "15 de octubre",
    "hora": "18:00",
    "ubicacion": "Quinta Fulanita",
    },
    {
    "cliente": "María",
    "telefono": "6141234567",
    "ordenes": 80,
    "fecha": "20 de octubre",
    "hora": "14:00",
    "ubicacion": "Salón las Palmas",
    },
    {
    "cliente": "Carlos",
    "telefono": "6149876543",
    "ordenes": 300,
    "fecha": "25 de octubre",
    "hora": "19:00",
    "ubicacion": "Jardín San Miguel",
    }]

@app.route("/")
def inicio():
    return render_template(
        "index17.html",
        eventos = eventos
    )
    
app.run(debug=True)