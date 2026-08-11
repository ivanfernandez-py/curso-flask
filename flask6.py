from flask import Flask, render_template

app = Flask("__name__")

@app.route("/")
def inicio():
    lenguajes = [
        "Python",
        "C",
        "SQL",
        "HTML"
    ]
    return render_template(
        "index5.html",
        lenguajes = lenguajes
    )
    
app.run(debug=True)