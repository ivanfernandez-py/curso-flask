from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

eventos = []


@app.route("/", methods = ["GET","POST"])
def inicio():
    errores = []
    if request.method == "POST":
        
        cliente = request.form.get("cliente")
        telefono = request.form.get("telefono")
        ordenes = request.form.get("ordenes")
        fecha = request.form.get("fecha")
        hora = request.form.get("hora")
        ubicacion = request.form.get("ubicacion")

        if fecha:
            fecha = datetime.strptime(fecha, "%Y-%m-%d")
            if fecha.date() < datetime.now().date():
                errores.append("La fecha no puede ser anterior a hoy.")
        else:
            errores.append("El campo 'Fecha' es obligatorio. ")
        
        if hora:
            hora = datetime.strptime(hora, "%H:%M")
            
        else:
            errores.append("El campo 'Hora' es obligatorio. ")
        
        
        if not errores:
            evento_nuevo = {
                "cliente" : cliente,
                "telefono" : telefono,
                "ordenes" : ordenes,
                "fecha" : fecha,
                "hora" : hora,
                "ubicacion" : ubicacion,
            }
            
            eventos.append(evento_nuevo)
    
    return render_template(
        "index26.html",
        eventos = eventos,
        errores = errores
    )
    
app.run(debug=True)