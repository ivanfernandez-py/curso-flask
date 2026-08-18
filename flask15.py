from flask import Flask, render_template, request

app = Flask(__name__)

eventos = []

@app.route("/", methods = ["GET","POST"])
def inicio():
    errores = []
    
    if request.method == "POST":
        
        cliente = request.form.get("cliente")
        telefono = request.form.get("telefono")
        ordenes = request.form.get("ordenes")
        
        if not cliente:
            errores.append("El campo 'Cliente' es obligatorio. ")
        if not telefono:
            errores.append("El campo 'Teléfono' es obligatorio. ")
        if not ordenes:
            errores.append("El campo 'Ordenes' es obligatorio. ")
        if len(telefono) != 10:
            errores.append("El campo 'Telefono' debe tener 10 digitos. ")
        
            
        if not errores:
            
            ordenes = int(ordenes)
            
            nuevo_evento = {
                "cliente" : cliente,
                "telefono" : telefono,
                "ordenes" : ordenes
            }
            
            eventos.append(nuevo_evento)
    
    return render_template(
        "index24.html",
        eventos = eventos,
        errores = errores
    )
app.run(debug=True)