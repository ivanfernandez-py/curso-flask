from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    eventos = [
        "Boda",
        "Cumpleaños",
        "Evento empresarial",
        "Quinceañera"
    ]
    return render_template(
        "index6.html",
        eventos = eventos
    )
    

app.run(debug=True)