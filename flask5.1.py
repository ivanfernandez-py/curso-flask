from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template(
        "index4.html",
        nombre = "Iván",
        edad= 24,
        estudiante = True
    )

app.run(debug=True)