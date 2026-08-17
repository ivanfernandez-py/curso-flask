from flask import Flask, render_template, request

app = Flask(__name__)

eventos = []

@app.route("/", methods = ["GET","POST"])
def inicio():
    mensaje = None
    
    if request.method == "POST":
        cliente = request.form.get("cliente")
        telefono = request.form.get("telefono")
        ordenes = request.form.get("ordenes")
        
        nuevo_evento = {
            "cliente": cliente,
            "telefono": telefono,
            "ordenes": ordenes
        }
        eventos.append(nuevo_evento)
    
    mensaje = "Evento registrado correctamente"
    
    return render_template(
        "index20.html",
        eventos = eventos,
        mensaje = mensaje
    )
app.run(debug=True)