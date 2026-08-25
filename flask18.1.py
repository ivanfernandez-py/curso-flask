from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

eventos = []

def validar_cliente(cliente):
    errores = []
    
    if not cliente:
        errores.append("El campo 'Cliente' es obligatorio")
    else:
        for palabra in cliente.split():
            if not palabra.isalpha():
                errores.append("Solo letras se aceptan en Cliente.")    
    return errores, cliente

def validar_telefono(telefono):
    errores_telefono = []
    
    if not telefono:
        errores_telefono.append("El campo 'Teléfono' es obligatorio. ")
    else:
        if not telefono.isdigit():
            errores_telefono.append("Solo números se aceptan en 'Teléfono'. ")
        if len(telefono) != 10:
            errores_telefono.append("El teléfono debe tener 10 dígitos. ")
            
    return errores_telefono, telefono

def validar_ordenes(ordenes):
    errores_ordenes = []
    
    if not ordenes:
        errores_ordenes.append("El campo 'Ordenes' es obligatorio. ")
    else:
        if not ordenes.isdigit():
            errores_ordenes.append("El campo 'Ordenes' debe contener un numero. ")  
        else:    
                ordenes = int(ordenes)
    return errores_ordenes, ordenes

def validar_fecha(fecha):
    errores_fecha = []

    if fecha: 
        fecha = datetime.strptime(fecha, "%Y-%m-%d")
        if fecha.date() < datetime.now().date():
            errores_fecha.append("La fecha del evento no puede ser anterior a hoy. ")
    
    else:
        errores_fecha.append("El campo 'Fecha' es obligatorio. ")
         
    return errores_fecha, fecha

def validar_hora(hora):
    errores_hora = []
    
    if hora:
        hora = datetime.strptime(hora, "%H:%M")
    else:
        errores_hora.append("El campo 'Hora' es obligatorio. ")
    
    return errores_hora, hora

@app.route("/",methods = ["GET", "POST"])
def inicio():

    errores = []
    if request.method == "POST":
        errores_cliente, cliente = validar_cliente(request.form.get("cliente"))
        errores_telefono, telefono = validar_telefono(request.form.get("telefono"))
        errores_ordenes, ordenes = validar_ordenes(request.form.get("ordenes"))
        errores_fecha, fecha = validar_fecha(request.form.get("fecha"))
        errores_hora, hora = validar_hora(request.form.get("hora"))
        ubicacion = request.form.get("ubicacion")

        errores += errores_cliente + errores_telefono + errores_ordenes + errores_fecha + errores_hora
    
        if not errores:
            evento_nuevo = {
                "cliente" : cliente,
                "telefono" : telefono,
                "ordenes" : ordenes,
                "fecha" : fecha,
                "hora" : hora,
                "ubicacion" : ubicacion
            }
            eventos.append(evento_nuevo)
    
    return render_template(
        "index26.html",
        eventos = eventos,
        errores = errores
    )
    
app.run(debug=True)