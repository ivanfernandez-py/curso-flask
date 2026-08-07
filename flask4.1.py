from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template(
        "index2.html",
        nombre = "Iván",
        lenguaje = "Python",
        nivel = "Principiante"
    )
    
app.run(debug=True)