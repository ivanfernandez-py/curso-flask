# RETO: Salida esperada
# Hola Iván
# Iván es estudiante.
# Es mayor de edad.

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template(
        "index3.html",
        nombre = "Iván",
        nivel = "Principiante"
    )
    
app.run(debug=True)