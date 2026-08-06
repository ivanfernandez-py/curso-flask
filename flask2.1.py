from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
        <h1> TITULO </h1>
            <p> Este curso tiene la finalidad </p>
            <p> de aprender Flask y HTML al   </p>
            <p> mismo tiempo.  </p>
            
            <ul>
                <li>Python</li>
                <li>Flask</li>
                <li>HTML</li>
            </ul>     
    """
    
app.run(debug=True)