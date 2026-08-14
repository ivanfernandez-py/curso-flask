from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def inicio():
    
    cliente = None
    telefono = None
    mensaje = None
    
    
    if request.method == "POST":
        cliente = request.form.get("cliente")
        telefono = request.form.get("telefono")
        if not cliente or not telefono:
            if not cliente: 
                campo = "'cliente'"
            if not telefono: 
                campo = "'telefono'"
            if not cliente and not telefono:
                campo = "'cliente' y 'telefono'"
                
            string = f"El campo {campo} es obligatorio"
            mensaje = string
        
    return render_template(
        "index15.html",
        cliente = cliente,
        telefono = telefono,
        mensaje = mensaje
    )
    
app.run(debug=True)