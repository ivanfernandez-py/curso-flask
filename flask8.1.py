from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def inicio():
    evento = None
    cliente = None
    invitados = None
    
    if request.method == "POST":
        evento = request.form["evento"]
        cliente = request.form["cliente"]
        invitados = request.form["invitados"]
    
    return render_template(
        "index10.html",
        evento = evento,
        cliente = cliente,
        invitados = invitados
    )
    
app.run(debug=True)