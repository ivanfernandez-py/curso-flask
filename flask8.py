from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def inicio():
    nombre = None
    
    if request.method == "POST":
        nombre = request.form["nombre"]
    
    return render_template(
        "index9.html",
        nombre = nombre
    )
    
app.run(debug=True)