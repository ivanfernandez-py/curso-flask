# Ordenes es string cuando flask lo recibe de HTML
# Queremos que el diccionario eventos guarde ordenes en entero.

from flask import Flask, render_template,request

app = Flask(__name__)

eventos = []

@app.route("/", methods = ["POST", "GET"])
def inicio():
    if request.method == "POST":
        cliente = request.form.get("cliente")
        telefono = request.form.get("telefono")
        ordenes = request.form.get("ordenes")
        
        ordenes = int(ordenes)
        
        nuevo_evento = {
            "cliente" : cliente,
            "telefono" : telefono,
            "ordenes" : ordenes
        }
        
        eventos.append(nuevo_evento)
    
    
    return render_template(
        "index23.html",
        eventos = eventos
    )
    
app.run(debug=True)