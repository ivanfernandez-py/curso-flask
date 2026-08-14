from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def inicio():
    
    cliente = None
    telefono = None
    
    if request.method == "POST":
        cliente = request.form.get("cliente")
        telefono = request.form.get("telefono")
        
    return render_template(
        "index14.html",
        cliente = cliente,
        telefono = telefono
    )

app.run(debug=True)