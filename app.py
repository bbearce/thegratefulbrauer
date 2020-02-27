import os, json, pdb
from flask import Flask, flash, jsonify, render_template, request, redirect, url_for
from flask_script import Manager
from flask_migrate import Migrate


# Forms
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

# Login
from flask_login import LoginManager, login_required, login_user, logout_user, UserMixin, current_user

# S3
import boto3


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' # Remind yourself why you need this? Answer:  must be set to use sessions...90% sure
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://bbearce:pass_;)_yeah_right@localhost/gratefulbrauer"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://xjedptgsjqocwi:25dfb7913372da245831b379d76ddb39eaf18eac98eade1b9542bc3ff0936dc4@ec2-23-21-229-48.compute-1.amazonaws.com:5432/d4hvr3omam72o1"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

manager = Manager(app)
migrate = Migrate(app, db)


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


# Login - https://www.youtube.com/watch?v=2dEM-s3mRLE
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class LoginForm(FlaskForm):
    name = StringField('username', validators=[DataRequired()])

class SignUpForm(FlaskForm):
    name = StringField('username', validators=[DataRequired()])

@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(int(user_id))


@app.route('/signup', methods=['POST'])
def signup():
    """
    Use this endpoint to add a username to the database
    """

    # We need this here because we only have 
    # one login page and it needs both forms
    login_form = LoginForm() 


    # Check if the user entered a name
    signup_form = SignUpForm()
    if signup_form.validate_on_submit():
        # First check to see if  we have that user already

        role = models.Role.query.filter_by(name='user')[0]
        user = models.User(username = signup_form.name.data, role_id = role.id)
        user_exists_already = False if models.User.query.filter_by(username=signup_form.name.data).first() is None else True

        if user_exists_already:
            flash('User \"{}\" already exists.')
            return redirect(url_for('login'))            

        

        db.session.add(user)
        db.session.commit()
        
        login_user(user)
        flash('Added {} to our users list!'.format(signup_form.name.data))    
        return redirect(url_for('brewculator'))    

    flash('Added {} to our users list!'.format(signup_form.name.data))

    return render_template('/brewculator/login.html', login_form=login_form, signup_form=signup_form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.

    # We need this here because we only have 
    # one login page and it needs both forms  
    signup_form = SignUpForm()

    login_form = LoginForm()
    if login_form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        user = models.User.query.filter_by(username=login_form.name.data).first()


        # If we don't have that user yet let them know and redirect to login page.
        if user is None:
            flash('Your username was not in our database. Please Sign up.')
            return redirect(url_for('login'))

        login_user(user)
        flash('User {} logged in successfully! Try out the Brewculator!'.format(login_form.name.data))
        return redirect(url_for('login'))

    return render_template('/brewculator/login.html', login_form=login_form, signup_form=signup_form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are logged out.')
    return redirect(url_for('index'))


### NOT BEING USED ###
# Upload file endpoint
@app.route('/media_upload', methods=['POST'])
def media_upload():


    # Get user'recipe_description_images/'+User+'/recipes/'+recipe_folder+file.filename
    User = current_user.username
    recipe_root = 'recipe_description_images/'+User+'/recipes/'

    file = request.files['file']
    recipe_folder = request.form['Recipe Folder']+'/' if request.form['Recipe Folder'] != '' else ''

    s3_key='recipe_description_images/'+User+'/recipes/'+recipe_folder+file.filename
    # load S3 images for current user
    # Let's use Amazon S3
    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket('thegratefulbrauer')

    # ContentType Notes: https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types
    my_bucket.put_object(Key=s3_key, Body=file, ContentType='image/jpeg')   

    flash('successfully uploaded: {}'.format(file.filename))

    # # Refresh Summaries
    # summaries = my_bucket.objects.all()
    # summaries = []
    # for s in my_bucket.objects.all():
    #     if s.key.find('.jpg') != -1:
    #         summaries.append(
    #             {'key':s.key.replace(recipe_root,''),
    #              'last_modified': s.last_modified,
    #             }
    #         )
    


    return redirect(url_for('brewculator')) 

### NOT BEING USED ###
# Delete file endpoint
@app.route('/media_delete', methods=['POST'])
def media_delete():


    # Get user'recipe_description_images/'+User+'/recipes/'+recipe_folder+file.filename
    User = current_user.username
    file = request.form['key']
    
    s3_key='recipe_description_images/'+User+'/recipes/'+file
    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket('thegratefulbrauer')
    my_bucket.Object(s3_key).delete()   
    flash('successfully deleted: {}'.format(s3_key))

    return redirect(url_for('brewculator')) 




# Begin CRUD Views or more correctly, routes...
@app.route('/load')
def load():

    recipe = request.args.get('recipe', 0, type=str)

    try:

        ### Recipe Data ###

        # If id exists and this doesn't fail, we can load the recipe.
        Recipe = models.Recipe.query.filter_by(recipe = recipe).first()
        Recipe.id # this tests for AttributeError

    except AttributeError as error:
        print("this recipe doesn't exist so we can't load it.")

        recipe = "that recipe doesn't exist"

        return jsonify(recipe=recipe)

    # BB - user User to add filter
    user = models.User.query.filter_by(username = current_user.username).first()
    
    # Single row tables
    for table in ['System','Mash','Yeast','Water','Fermentation','Chemistry']:
        exec('{} = models.Recipe_{}.query.filter_by(recipe_id = Recipe.id, user_id = user.id).first()'.format(table, table))

    # Multiple row tables
    for table in ['Fermentables','Hops']:
        exec('{} = models.Recipe_{}.query.filter_by(recipe_id = Recipe.id, user_id = user.id).all()'.format(table, table))

    # Build data json dictionary based on models.


    # BB - This is serializing...maybe a better way...

    data = {'Recipe':{}} 

    recipe_dict = {}
    for r in recipe_columns:
        recipe_dict[r] = getattr(Recipe, r)
    
    exec("""
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
    """)

    return jsonify(data=data)

 

@app.route('/save')
def save():

    # Get user
    user = models.User.query.filter_by(username = current_user.username)[0]
    
    # Common to all (in db: gb_recipe_system)
    recipe = request.args.get('recipe', 0, type=str)
    style = request.args.get('style', 0, type=str)
    notes = request.args.get('notes', 0, type=str)

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
    Recipe = models.Recipe(recipe=recipe, style=style, notes=notes, user_id=user.id)
    
    if(len(models.Recipe.query.filter_by(recipe=Recipe.recipe).all()) == 0):
        print("this recipe doesn't exist so we are adding it.")

        db.session.add(Recipe)
        db.session.commit()
        # System

        system_string = "System = models.Recipe_System(user_id=user.id, recipe_id=Recipe.id,"
        for s in system_columns[1:]:
            system_string = system_string + " {}={},".format(s,s)

        system_string = system_string + ")";
        exec(system_string)

        # Fermentables
        num_of_ingredients = 5
        for i in range(0,num_of_ingredients):
            fermentables_string = "Fermentables{} = models.Recipe_Fermentables(user_id=user.id, recipe_id=Recipe.id,".format(i+1)
            for fermentables in fermentables_columns[1:]:
                fermentables_string = fermentables_string + " {}={}{},".format(fermentables,fermentables,i+1)
            fermentables_string = fermentables_string + ")";
            exec(fermentables_string)
        # Fermentables1 = models.Recipe_Fermentables(recipe_id=Recipe.id, ingredient=ingredient1, weight_lbs=weight_lbs1,)
        # Fermentables2 = models.Recipe_Fermentables(recipe_id=Recipe.id, ingredient=ingredient2, weight_lbs=weight_lbs2,)
        # Fermentables3 = models.Recipe_Fermentables(recipe_id=Recipe.id, ingredient=ingredient3, weight_lbs=weight_lbs3,)
        # Fermentables4 = models.Recipe_Fermentables(recipe_id=Recipe.id, ingredient=ingredient4, weight_lbs=weight_lbs4,)
        # Fermentables5 = models.Recipe_Fermentables(recipe_id=Recipe.id, ingredient=ingredient5, weight_lbs=weight_lbs5,)
        # Hops
        num_of_ingredients = 3
        for i in range(0,num_of_ingredients):
            hops_string = "Hops{} = models.Recipe_Hops(user_id=user.id, recipe_id=Recipe.id,".format(i+1)
            for hops in hops_columns[1:]:
                hops_string = hops_string + " {}={}{},".format(hops,hops,i+1)
            hops_string = hops_string + ")"
            exec(hops_string)
        # Hops1 = models.Recipe_Hops(recipe_id=Recipe.id, hop=hop1, weight_oz=weight_oz1, boil_time_min=boil_time_min1,)
        # Hops2 = models.Recipe_Hops(recipe_id=Recipe.id, hop=hop2, weight_oz=weight_oz2, boil_time_min=boil_time_min2,)
        # Hops3 = models.Recipe_Hops(recipe_id=Recipe.id, hop=hop3, weight_oz=weight_oz3, boil_time_min=boil_time_min3,)

        # Mash
        mash_string = "Mash = models.Recipe_Mash(user_id=user.id, recipe_id=Recipe.id,"
        for m in mash_columns[1:]:
            mash_string = mash_string + " {}={},".format(m,m)

        mash_string = mash_string + ")"; exec(mash_string)
        
        # Yeast
        yeast_string = "Yeast = models.Recipe_Yeast(user_id=user.id, recipe_id=Recipe.id,"
        for y in yeast_columns[1:]:
            yeast_string = yeast_string + " {}={},".format(y,y)

        yeast_string = yeast_string + ")"; exec(yeast_string)

        # Water
        water_string = "Water = models.Recipe_Water(user_id=user.id, recipe_id=Recipe.id,"
        for w in water_columns[1:]:
            water_string = water_string + " {}={},".format(w,w)

        water_string = water_string + ")"; exec(water_string)

        # Fermentation
        fermentation_string = "Fermentation = models.Recipe_Fermentation(user_id=user.id, recipe_id=Recipe.id,"
        for fermentation in fermentation_columns[1:]:
            fermentation_string = fermentation_string + " {}={},".format(fermentation,fermentation)

        fermentation_string = fermentation_string + ")"; exec(fermentation_string)

        # Chemistry
        chemistry_string = "Chemistry = models.Recipe_Chemistry(user_id=user.id, recipe_id=Recipe.id,"
        for c in chemistry_columns[1:]:
            chemistry_string = chemistry_string + " {}={},".format(c,c)

        chemistry_string = chemistry_string + ")"; exec(chemistry_string)

        exec("Fermentables = [Fermentables1, Fermentables2, Fermentables3, Fermentables4, Fermentables5]")
        exec("Hops = [Hops1, Hops2, Hops3]")
        exec("db.session.add_all(Fermentables + Hops + [Mash, Water, Fermentation, Yeast, Chemistry, System])")
        exec("db.session.commit()")

    else:
        recipe = "that recipe already exists"
    
    # Get updated list of recipes 
    Recipes = [recipe_name.recipe for recipe_name in models.Recipe.query.filter_by(user_id = user.id).all()]

    return jsonify(recipe=recipe, Recipes=Recipes)


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

    # Get updated list of recipes 
    user = models.User.query.filter_by(username = current_user.username)[0]
    Recipes = [recipe_name.recipe for recipe_name in models.Recipe.query.filter_by(user_id = user.id).all()]
        
    return jsonify(recipe=recipe, Recipes=Recipes)


@app.route('/brewculator')
@login_required
def brewculator():

    # Get user    
    user = models.User.query.filter_by(username = current_user.username)[0]


    ### NOT BEING USED ### -- this is the code to link to AWS
    # recipe_root = 'recipe_description_images/'+user.username+'/recipes/'

    # # load S3 images for current user
    # # Let's use Amazon S3: cleint and resource have different actions and abilities
    # s3_client = boto3.client('s3')
    # s3_resource = boto3.resource('s3')
    
    # s3_resource = boto3.resource('s3')
    # bucket = s3_resource.Bucket('thegratefulbrauer')
    # objs = list(bucket.objects.filter(Prefix=recipe_root))

    # # This will be the default value unless other objects are found
    # summaries = [{'key': 'None','last_modified':'None'}]

    # if(len(objs)>1):
    #     objects = s3_client.list_objects_v2(Bucket='thegratefulbrauer', StartAfter=recipe_root)    
    #     summaries = []
    #     for s in objects['Contents']:
    #         if (s['Key'].find('.jpg') != -1 or s['Key'].find('.jpeg') != -1 or s['Key'].find('.JPG') != -1 or s['Key'].find('.PNG') != -1 or s['Key'].find('.png') != -1) and s['Key'].find(recipe_root) != -1:
    #             summaries.append(
    #                 {'key':s['Key'].replace(recipe_root,''),
    #                  'last_modified': s['LastModified']
    #                 }
    #             )

    # else:
    #     my_bucket = s3_resource.Bucket('thegratefulbrauer')
    #     my_bucket.put_object(Bucket='thegratefulbrauer', Body='', Key=recipe_root)






            
    # Get fermentables (not recipe values but constants)
    Recipes = models.Recipe.query.filter_by(user_id = user.id).all()
    Styles = models.Styles.query.order_by('styles').all()
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
    fcolumns = [[j for j in i] for i in fcolumns] # Python3 has zips as generators so I have to convert


    # Dynamic Control for Hops Inputs
    num_of_inputs = 3
    hcolumns = [zip(hops_columns,[i]*(len(hops_columns)+1)) for i in range(1,num_of_inputs+1)]
    hcolumns = [[j for j in i] for i in hcolumns] # Python3 has zips as generators so I have to convert

    return render_template('/brewculator/brewculator.html',
                           User = user.username,     # Files=summaries, --> from AWS
                           Data = json.dumps(data),
                           Recipes=Recipes,
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
    # manager.run()
    app.run(host='0.0.0.0', port=port)
    # !import code; code.interact(local=vars()) #Note this down as well

