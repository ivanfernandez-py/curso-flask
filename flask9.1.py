from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
@app.route("/")
def inicio():
    return render_template("index12.html")

@app.route("/confirmacion", methods=["POST"])
def confirmacion():
    evento = request.form["evento"]
    cliente = request.form["cliente"]
    return redirect(url_for("mostrar_confirmacion",evento=evento,cliente=cliente))

@app.route("/confirmacion/<evento>/<cliente>")
def mostrar_confirmacion(evento,cliente):
    return render_template(
        "confirmacion.html",
        evento = evento,
        cliente = cliente
    )
    
app.run(debug=True)