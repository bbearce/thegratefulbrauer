import os
from flask import Flask, render_template
app = Flask(__name__)
 
@app.route("/")
def index():
    return render_template("index.html") 

@app.route("/Ales")
def Ales():
    return render_template("Ales.html") 

@app.route("/Ales/<name>")
def Specific_Ales(name):
    return render_template("Ales/"+name)

@app.route("/Lagers")
def Lagers():
    return render_template("Lagers.html")

@app.route("/Lagers/<name>")
def Specific_Lagers(name):
    return render_template("Lagers/"+name) 

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 33507))
    app.run(host='0.0.0.0', port=port)