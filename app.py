import os, json
from flask import Flask, flash, jsonify, render_template, request, redirect, url_for
from flask_script import Manager

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' # Remind yourself why you need this?
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://bbearce:Alak3_N3van@localhost/gratefulbrauer"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from models import db  # <-- this needs to be placed after app is created

manager = Manager(app)

# Grab DB table column names
import models

# Make convenient columns variables for recipe

recipe_columns = [column.key for column in models.Recipe.__table__.columns][1:]
for recipe_table in ['system','mash','fermentables','hops','yeast','water','fermentation','chemistry']:
    exec("{}_columns = [column.key for column in models.Recipe_{}.__table__.columns][2:]".format(recipe_table,recipe_table.capitalize())) 


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


### Brewculator ###

# Begin Views or more correctly, routes...
@app.route('/load')
def load():

    recipe = request.args.get('recipe', 0, type=str)

    try:

        ### Recipe Data ###

        # If id exists and this doesn't fail, we can load the recipe.
        Recipe = models.Recipe.query.filter_by(recipe = recipe).first()
        Recipe.id # this tests for AttributeError

        # Single row tables
        for table in ['System','Mash','Yeast','Water','Fermentation','Chemistry']:
            exec('{} = models.Recipe_{}.query.filter_by(recipe_id = Recipe.id).first()'.format(table, table))

        # Multiple row tables
        for table in ['Fermentables','Hops']:
          exec('{} = models.Recipe_{}.query.filter_by(recipe_id = Recipe.id).all()'.format(table, table))

        # Build data json dictionary based on models.

        data = {'Recipe':{}}

        recipe_dict = {}
        for r in recipe_columns:
            recipe_dict[r] = getattr(Recipe, r)

        system_dict = {}
        for s in system_columns:
            system_dict[s] = getattr(System, s)        

        fermentables_list = []
        for F in Fermentables:
            fermentables_dict = {}
            for f in fermentables_columns:
                fermentables_dict[f] = getattr(F, f)
            fermentables_list.append(fermentables_dict)

        hops_list = []
        for H in Hops:
            hops_dict = {}
            for h in hops_columns:
                hops_dict[h] = getattr(H, h)
            hops_list.append(hops_dict)

        mash_dict = {}
        for m in mash_columns:
            mash_dict[m] = getattr(Mash, m)

        yeast_dict = {}
        for y in yeast_columns:
            yeast_dict[y] = getattr(Yeast, y)

        water_dict = {}
        for w in water_columns:
            water_dict[w] = getattr(Water, w)

        fermentation_dict = {}
        for f in fermentation_columns:
            fermentation_dict[f] = getattr(Fermentation, f)

        chemistry_dict = {}
        for c in chemistry_columns:
            chemistry_dict[c] = getattr(Chemistry, c)

        data['Recipe']['gb_recipe_master'] = recipe_dict
        data['Recipe']['gb_recipe_system'] = system_dict
        data['Recipe']['gb_recipe_fermentables'] = fermentables_list
        data['Recipe']['gb_recipe_hops'] = hops_list
        data['Recipe']['gb_recipe_mash'] = mash_dict
        data['Recipe']['gb_recipe_yeast'] = yeast_dict
        data['Recipe']['gb_recipe_water'] = water_dict
        data['Recipe']['gb_recipe_fermentation'] = fermentation_dict
        data['Recipe']['gb_recipe_chemistry'] = chemistry_dict




        ####### CONSIDER CLEANING BELOW COMPLETELY OUT #########





        # dict_string = "data = {'recipe':recipe,"
        # for s in system_columns:
        #     dict_string = dict_string + " '{}':System.{},".format(s,s)

        # num_of_ingredients = 5
        # for fermentables in fermentables_columns:
        #     for i in range(0,num_of_ingredients):
        #         dict_string = dict_string + " '{}{}':Fermentables[{}].{},".format(fermentables,i+1,i,fermentables)

        # num_of_ingredients = 3
        # for h in hops_columns:
        #     for i in range(0,num_of_ingredients):
        #         dict_string = dict_string + " '{}{}':Hops[{}].{},".format(h,i+1,i,h)

        # for m in mash_columns:
        #     dict_string = dict_string + " '{}':Mash.{},".format(m,m)

        # for y in yeast_columns:
        #     dict_string = dict_string + " '{}':Yeast.{},".format(y,y)

        # for w in water_columns:
        #     dict_string = dict_string + " '{}':Water.{},".format(w,w)

        # for fermentation in fermentation_columns:
        #     dict_string = dict_string + " '{}':Fermentation.{},".format(fermentation,fermentation)

        # for c in chemistry_columns:
        #     dict_string = dict_string + " '{}':Chemistry.{},".format(c,c)

        # dict_string = dict_string + "}"

        # exec(dict_string)

        ### Constants Data ###

        # fermentables_list = []
        # for F in data['Recipe']['gb_recipe_fermentables']:
        #     fermentable = models.Fermentables.query.filter_by(ingredients =F['ingredient']).first()
        #     fermentables_dict = {}
        #     count=1;
        #     for f in fermentable.__table__.columns._data:
        #         if count != 1:
        #             fermentables_dict[f] = getattr(fermentable, f)
        #         count = count+1;
        #     fermentables_list.append(fermentables_dict)

        # hops_list = []
        # for H in data['Recipe']['gb_recipe_hops']:
        #     hop = models.Hops.query.filter_by(hops =H['hop']).first()
        #     hops_dict = {}
        #     count=1;
        #     for h in hop.__table__.columns._data:
        #         if count != 1:
        #             hops_dict[f] = getattr(hop, h)
        #         count = count+1;
        #     hops_list.append(hops_dict)

        # yeast = models.Yeast.query.filter_by(yeastStrain = data['Recipe']['gb_recipe_yeast']['yeast_name']).first()
        # yeast_dict = {}
        # count=1;
        # for y in yeast.__table__.columns._data:
        #     if count != 1:
        #         yeast_dict[y] = getattr(yeast, y)
        #     count = count + 1;

        # style = models.Styles.query.filter_by(styles = data['Recipe']['gb_recipe_master']['style']).first()
        # style_dict = {}
        # count=1;
        # for s in style.__table__.columns._data:
        #     if count != 1:
        #         style_dict[s] = getattr(style, s)
        #     count = count + 1;

        # gcc_list = []
        # for G in models.gravity_correction_chart.query.all():
        #     gcc_dict = {}
        #     count=1;
        #     for g in G.__table__.columns._data:
        #         if count != 1:
        #             gcc_dict[g] = getattr(G, g)
        #         count = count+1;
        #     gcc_list.append(gcc_dict)

        # data['Constants'] = {}

        # data['Constants']['gb_constants_fermentables'] = fermentables_list
        # data['Constants']['gb_constants_hops'] = hops_list
        # data['Constants']['gb_constants_yeast'] = yeast_dict
        # data['Constants']['gb_constants_style'] = style_dict
        # data['Constants']['gb_constants_gcc'] = gcc_list


        ####### CONSIDER CLEANING ABOVE COMPLETELY OUT #########


        return jsonify(data=data)

    except AttributeError as error:
        print("this recipe doesn't exist so we can't load it.")

        recipe = "that recipe doesn't exist"

        return jsonify(recipe=recipe)
 

@app.route('/save')
def save():
    
    # Common to all
    recipe = request.args.get('recipe', 0, type=str)
    style = request.args.get('style', 0, type=str)

    # Grab all input values from html pages
    for s in system_columns:
        exec("{} = request.args.get('{}', 0, type=str)".format(s,s))

    num_of_ingredients = 5
    for fermentables in fermentables_columns:
        for i in range(0,num_of_ingredients):
            exec("{}{} = request.args.get('{}{}', 0, type=str)".format(fermentables,i+1,fermentables,i+1))

    num_of_ingredients = 3
    for h in hops_columns:
        for i in range(0,num_of_ingredients):
            exec("{}{} = request.args.get('{}{}', 0, type=str)".format(h,i+1,h,i+1))

    for m in mash_columns:
        exec("{} = request.args.get('{}', 0, type=str)".format(m,m))

    for y in yeast_columns:
        exec("{} = request.args.get('{}', 0, type=str)".format(y,y))

    for w in water_columns:
        exec("{} = request.args.get('{}', 0, type=str)".format(w,w))

    for fermentation in fermentation_columns:
        exec("{} = request.args.get('{}', 0, type=str)".format(fermentation,fermentation))

    for c in chemistry_columns:
        exec("{} = request.args.get('{}', 0, type=str)".format(c,c))

    # check if this already exists

    Recipe = models.Recipe(recipe=recipe, style=style)

    try:
      # If id exists and this doesn't fail, we have a duplicate and we need to just send a message.
      models.Recipe.query.filter_by(recipe=Recipe.recipe).all()[-1].id
      recipe = "that recipe already exists"

    except IndexError as error:
        print("this recipe doesn't exist so we are adding it.")

        db.session.add(Recipe)
        db.session.commit()

        # System
        system_string = "System = models.Recipe_System(recipe_id=Recipe.id,"
        for s in system_columns:
            system_string = system_string + " {}={},".format(s,s)

        system_string = system_string + ")"; exec(system_string)

        # Fermentables
        num_of_ingredients = 5
        for i in range(0,num_of_ingredients):
            fermentables_string = "Fermentables{} = models.Recipe_Fermentables(recipe_id=Recipe.id,".format(i+1)
            for fermentables in fermentables_columns:
                fermentables_string = fermentables_string + " {}={}{},".format(fermentables,fermentables,i+1)
            fermentables_string = fermentables_string + ")"; exec(fermentables_string)

        # Hops
        num_of_ingredients = 3
        for i in range(0,num_of_ingredients):
            hops_string = "Hops{} = models.Recipe_Hops(recipe_id=Recipe.id,".format(i+1)
            for hops in hops_columns:
                hops_string = hops_string + " {}={}{},".format(hops,hops,i+1)
            hops_string = hops_string + ")"; exec(hops_string)
        
        # Mash
        mash_string = "Mash = models.Recipe_Mash(recipe_id=Recipe.id,"
        for m in mash_columns:
            mash_string = mash_string + " {}={},".format(m,m)

        mash_string = mash_string + ")"; exec(mash_string)
        
        # Yeast
        yeast_string = "Yeast = models.Recipe_Yeast(recipe_id=Recipe.id,"
        for y in yeast_columns:
            yeast_string = yeast_string + " {}={},".format(y,y)

        yeast_string = yeast_string + ")"; exec(yeast_string)

        # Water
        water_string = "Water = models.Recipe_Water(recipe_id=Recipe.id,"
        for w in water_columns:
            water_string = water_string + " {}={},".format(w,w)

        water_string = water_string + ")"; exec(water_string)        

        # Fermentation
        fermentation_string = "Fermentation = models.Recipe_Fermentation(recipe_id=Recipe.id,"
        for fermentation in fermentation_columns:
            fermentation_string = fermentation_string + " {}={},".format(fermentation,fermentation)

        fermentation_string = fermentation_string + ")"; exec(fermentation_string)

        # Chemistry
        chemistry_string = "Chemistry = models.Recipe_Chemistry(recipe_id=Recipe.id,"
        for c in chemistry_columns:
            chemistry_string = chemistry_string + " {}={},".format(c,c)

        chemistry_string = chemistry_string + ")"; exec(chemistry_string)
       

        Fermentables = [Fermentables1, Fermentables2, Fermentables3, Fermentables4, Fermentables5]

        Hops = [Hops1, Hops2, Hops3]
        db.session.add_all(Fermentables + Hops + [Mash, Water, Fermentation, Yeast, Chemistry, System])
        db.session.commit()
   
    return jsonify(recipe=recipe)


@app.route('/delete')
def delete():
    
    import models

    # Common to all
    recipe = request.args.get('recipe', 0, type=str)

    try:
        Recipe = models.Recipe.query.filter_by(recipe=recipe).all()[0]
        db.session.delete(Recipe)
        db.session.commit()
        print("We deleted something")

    except IndexError as error:
        recipe = "that recipe does not exist"

        
    return jsonify(recipe=recipe)

    
@app.route('/brewculator')
def brewculator():
    
    # Get fermentables (not recipe values but constants)
    Styles = models.Styles.query.all()
    Fermentables = models.Fermentables.query.all()
    Hops = models.Hops.query.all()
    Yeast = models.Yeast.query.all()
    gcc = models.gravity_correction_chart.query.all()
    ut = models.utilization_table.query.all()

    ### Constants Data ###

    fermentables_list = []
    for F in Fermentables:
        fermentables_dict = {}
        for f in [i for i in F.__table__.columns._data]:
            fermentables_dict[f] = getattr(F, f)
        fermentables_list.append(fermentables_dict)

    hops_list = []
    for H in Hops:
        hops_dict = {}
        for h in [i for i in H.__table__.columns._data]:
            hops_dict[h] = getattr(H, h)
        hops_list.append(hops_dict)

    yeast_list = []
    for Y in Yeast:
        yeast_dict = {}
        for y in [i for i in Y.__table__.columns._data]:
            yeast_dict[y] = getattr(Y, y)
        yeast_list.append(yeast_dict)

    style_list = []
    for S in Styles:
        style_dict = {}
        for s in [i for i in S.__table__.columns._data]:
            style_dict[s] = getattr(S, s)
        style_list.append(style_dict)

    gcc_list = []
    for G in models.gravity_correction_chart.query.all():
        gcc_dict = {}
        for g in G.__table__.columns._data:
            gcc_dict[g] = getattr(G, g)
        gcc_list.append(gcc_dict)

    ut_list = []
    for U in models.utilization_table.query.all():
        ut_dict = {}
        for u in U.__table__.columns._data:
            ut_dict[u] = getattr(U, u)
        ut_list.append(ut_dict)

    data = {}
    data['Constants'] = {}

    data['Constants']['gb_constants_fermentables'] = fermentables_list
    data['Constants']['gb_constants_hops'] = hops_list
    data['Constants']['gb_constants_yeast'] = yeast_list
    data['Constants']['gb_constants_style'] = style_list
    data['Constants']['gb_constants_gcc'] = gcc_list
    data['Constants']['gb_constants_ut'] = ut_list



    # Dynamic Control for Fermentables Inputs
    num_of_inputs = 5
    fcolumns = [zip(fermentables_columns,[i]*(len(fermentables_columns)+1)) for i in range(1,num_of_inputs+1)]

    # Dynamic Control for Hops Inputs
    num_of_inputs = 3
    hcolumns = [zip(hops_columns,[i]*(len(hops_columns)+1)) for i in range(1,num_of_inputs+1)]



    return render_template('/brewculator/brewculator.html',
                           Data = json.dumps(data),
                           Styles = Styles,
                           Fermentables = Fermentables,
                           Hops = Hops,
                           Yeast = Yeast,

                           system_columns=system_columns,
                           fermentables_columns=fcolumns, # look above for special variable construction
                           hops_columns=hcolumns, # look above for special variable construction
                           mash_columns=mash_columns,
                           yeast_columns=yeast_columns,
                           water_columns=water_columns,
                           fermentation_columns=fermentation_columns,
                           chemistry_columns=chemistry_columns)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 33507))
    manager.run()
    #app.run(host='0.0.0.0', port=port)
