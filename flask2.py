# First HTML

from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <h1>Mi primera pagina con Flask </h1>
    <p>Estoy aprendiendo Flask y HTML </p>
    """
    
app.run(debug=True)