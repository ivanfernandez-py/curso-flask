from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index11.html")

@app.route("/saludo", methods=["POST"])
def saludo():
    nombre = request.form["nombre"]
    
    return redirect(url_for("mostrar_saludo", nombre=nombre))

@app.route("/saludo/<nombre>")
def mostrar_saludo(nombre):
    return render_template(
        "saludo.html",
        nombre = nombre
    )
    
app.run(debug=True)