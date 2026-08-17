from flask import Flask, render_template, request

app = Flask(__name__)

eventos = []

@app.route("/", methods = ["GET","POST"])
def inicio():
    if request.method == "POST":
        
        cliente = request.form.get("cliente")
        telefono = request.form.get("telefono")
        ordenes = request.form.get("ordenes")
        confirmado = request.form.get("confirmado")
        
        if cliente and telefono:
            
            if confirmado == "si":
                confirmado = True
            if confirmado == "no":
                confirmado = False
                
            nuevo_evento = {
                "cliente" : cliente,
                "telefono": telefono,
                "ordenes" : ordenes,
                "confirmado" : confirmado
            }            

            eventos.append(nuevo_evento)
            
    return render_template(
        "index22.html",
        eventos = eventos
    )
    
app.run(debug=True)