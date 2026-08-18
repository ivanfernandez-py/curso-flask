from flask import Flask, render_template, request

eventos = []

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def inicio():
    errores = []
    
    cliente = request.form.get("cliente")
    telefono = request.form.get("telefono")
    ordenes = request.form.get("ordenes")
    
    if request.method == "POST":
        if not cliente:
            errores.append("El campo 'Cliente' es obligatorio.")
        if not ordenes:
            errores.append("El campo 'Ordenes' es obligatorio.")
        if not telefono: 
            errores.append("El campo 'Telefono' es obligatorio.")
        else : 
            if len(telefono) != 10:
                errores.append("El numero de telefono debe tener 10 digitos. ")
        if not errores:
            ordenes = int(ordenes)
            
            nuevo_evento = {
                "cliente" : cliente,
                "telefono" : telefono,
                "ordenes" : ordenes
            }
            
            eventos.append(nuevo_evento)
            
    
    return render_template(
        "index25.html",
        eventos = eventos, 
        errores = errores
    )
app.run(debug=True)