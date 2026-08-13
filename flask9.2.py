# Base/Prototipo de registro de eventos para taco planner

from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index13.html")

@app.route("/confirmacion", methods=["POST"])
def confirmacion():
    cliente = request.form["cliente"]
    telefono = request.form["telefono"]
    ordenes = request.form["ordenes"]
    fecha = request.form["fecha"]
    hora = request.form["hora"]
    ubicacion= request.form["ubicacion"]
    return redirect(url_for("mostrar_confirmacion", cliente = cliente, telefono = telefono, ordenes = ordenes, fecha = fecha, hora=hora, ubicacion=ubicacion))

@app.route("/confirmacion/<cliente>/<telefono>/<ordenes>/<fecha>/<hora>/<ubicacion>")
def mostrar_confirmacion(cliente,telefono,ordenes,fecha,hora,ubicacion):
    return render_template(
        "confirmacion2.html",
         cliente = cliente,
         telefono = telefono,
         ordenes = ordenes,
         fecha = fecha,
         hora=hora,
         ubicacion=ubicacion
    )
    
app.run(debug=True)