import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
#
# # Database - Start
# class Fermentables(db.Model):
#     __tablename__ = 'fermentables'
#     id = db.Column(db.Integer, primary_key=True)
#     ingredients = db.Column(db.String(64), unique=True)
#     degree_linter = db.Column(db.String(5))
#     value = db.Column(db.Integer)
#     ppg = db.Column(db.Float)
#     srm = db.Column(db.Float)
#     ez_water_code = db.Column(db.Integer)
#     flavor_profile = db.Column(db.Text)
#     dp = db.Column(db.Integer)
#     is_grain = db.Column(db.Integer)
#
#     def __repr__(self):
#         return '<Role %r>' % self.ingredients
#
# class Hops(db.Model):
#     __tablename__ = 'hops'
#     id = db.Column(db.Integer, primary_key=True)
#     hops = db.Column(db.String(64), unique=True)
#     value = db.Column(db.Float)
#     alphaLow = db.Column(db.Float)
#     alphaHigh = db.Column(db.Float)
#     flavorProfile = db.Column(db.String(200))
#     possibleSubstitutions = db.Column(db.String(64))
#     orgin = db.Column(db.String(64))
#     storage = db.Column(db.String(64))
#     additionalInformation_History = db.Column(db.Text)
#
#     def __repr__(self):
#         return '<Role %r>' % self.hops
#
# class Yeast(db.Model):
#     __tablename__ = 'yeast'
#     id = db.Column(db.Integer, primary_key=True)
#     yeastStrain = db.Column(db.String(64), unique=True)
#     value = db.Column(db.Float)
#     attenuation = db.Column(db.Float)
#     temperatureRangeLow = db.Column(db.Integer)
#     temperatureRangeHigh = db.Column(db.Integer)
#     flocculation = db.Column(db.String(64))
#     alcoholTolerancePercentLow = db.Column(db.Float)
#     alcoholTolerancePercentHigh = db.Column(db.Float)
#     flavorCharacteristics = db.Column(db.Text)
#     recommendedStyles = db.Column(db.String(64))
#     brewery = db.Column(db.String(64))
#
#     def __repr__(self):
#         return '<Role %r>' % self.yeastStrain
#
# class Styles(db.Model):
#     __tablename__ = 'styles'
#     id = db.Column(db.Integer, primary_key=True)
#     generalStyle = db.Column(db.String(64))
#     styles = db.Column(db.String(64))
#     OGRangeLow = db.Column(db.Float)
#     OGRangeHigh = db.Column(db.Float)
#     FGRangeLow = db.Column(db.Float)
#     FGRangeHigh = db.Column(db.Float)
#     bitterLow = db.Column(db.Float)
#     bitterHigh = db.Column(db.Float)
#     SRMRangeLow = db.Column(db.Float)
#     SRMRangeHigh = db.Column(db.Float)
#
#     def __repr__(self):
#         return '<Role %r>' % self.styles
#
# class gravity_correction_chart(db.Model):
#     __tablename__ = 'gravity_correction_chart'
#     id = db.Column(db.Integer, primary_key=True)
#     temperature_F= db.Column(db.Integer)
#     temperature_C= db.Column(db.Integer)
#     add_SG = db.Column(db.Integer)
#
#     def __repr__(self):
#         return '<Role %r>' % self.temperature_C

# Database - End

@app.route("/")
def index():
    #all_fermentables = Fermentables.query.all()
    return render_template("index.html")#, all_fermentables = all_fermentables)

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
