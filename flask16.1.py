from flask import Flask, render_template, request

eventos = []

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def inicio():
    errores = []
    ordenes_otras = None
    
    if request.method == "POST":
        
        cliente = request.form.get("cliente")
        telefono = request.form.get("telefono")
        ordenes = request.form.get("ordenes") 
        ordenes_otras = request.form.get("ordenes_otras")
        
        if not cliente:
            errores.append("El campo 'Cliente' es obligatorio.")
        else:
            for palabra in cliente.split():
                if not palabra.isalpha():
                    errores.append("Solo letras se permiten en 'Nombre'")
            
        if not ordenes:
            if not ordenes_otras:
                errores.append("El campo 'Ordenes' es obligatorio.")
   
            if ordenes_otras:
                if ordenes_otras.isdigit():
                    ordenes = ordenes_otras
                else:
                    errores.append("Ingresa número de ordenes válido. ")
                            
        if not telefono: 
            errores.append("El campo 'Telefono' es obligatorio.")
        else : 
            if len(telefono) != 10:
                errores.append("El numero de telefono debe tener 10 digitos. ")
            if not telefono.isdigit():
                errores.append("Caracteres no validos en telefono. ")
        
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