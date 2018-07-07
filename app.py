import os
from flask import Flask, render_template
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
manager = Manager(app)


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
    manager.run()
    # app.run(host='0.0.0.0', port=port)
