from flask import Flask, render_template, request

app = Flask(__name__)

eventos = [
    {
        "cliente" : "Ivancho",
        "telefono" : "6143635380",
        "ordenes" : 150,
        "fecha" : "15 DE OCTUBRE",
        "hora" : "18:00",
        "ubicacion" : "Quinta Fulanita",
    }
]

@app.route("/", methods = ["GET","POST"])
def inicio():
    if request.method == "POST":
        cliente = request.form.get("cliente")
        telefono = request.form.get("telefono")
        ordenes = request.form.get("ordenes")
        fecha = request.form.get("fecha")
        hora = request.form.get("hora")
        ubicacion = request.form.get("ubicacion")

        nuevo_evento = {
            "cliente": cliente,
            "telefono": telefono,
            "ordenes": ordenes,
            "fecha": fecha,
            "hora": hora,
            "ubicacion": ubicacion
    }

        eventos.append(nuevo_evento)
    

    return render_template(
        "index19.html",
        eventos = eventos
        )
    
app.run(debug=True)