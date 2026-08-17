from flask import Flask, render_template, request

app = Flask(__name__)
eventos = []

@app.route("/", methods = ["GET","POST"])
def inicio():
    mensaje = None
    
    if request.method == "POST":
        cliente = request.form.get("cliente")
        telefono = request.form.get("telefono")

        if cliente and telefono:
            nuevo_evento = {
                "cliente" : cliente,
                "telefono" : telefono
            }
            
            eventos.append(nuevo_evento)
            mensaje = "Evento registrado correctamente."
        else: 
            mensaje = "Faltan campos obligatorios. "
    
    return render_template(
        "index21.html",
        mensaje = mensaje,
        eventos = eventos
    )
    
app.run(debug=True)