from __main__ import app
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

# Site tables
class Role(db.Model):
    __tablename__ = 'gb_site_role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'gb_site_users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('gb_site_role.id'))

    def __repr__(self):
        return '<User %r>' % self.username


# Constants tables
class Fermentables(db.Model):
    __tablename__ = 'gb_constants_fermentables'
    id = db.Column(db.Integer, primary_key=True)
    ingredients = db.Column(db.String(64), unique=True)
    degree_linter = db.Column(db.String(5))
    value = db.Column(db.Float)
    ppg = db.Column(db.Float)
    srm = db.Column(db.Float)
    ez_water_code = db.Column(db.Integer)
    distilled_water_ph = db.Column(db.Float)
    flavor_profile = db.Column(db.Text)
    dp = db.Column(db.Integer)
    is_grain = db.Column(db.Integer)

    def __repr__(self):
        return '<Role %r>' % self.ingredients

class Hops(db.Model):
    __tablename__ = 'gb_constants_hops'
    id = db.Column(db.Integer, primary_key=True)
    hops = db.Column(db.String(64), unique=True)
    value = db.Column(db.Float)
    alphaLow = db.Column(db.Float)
    alphaHigh = db.Column(db.Float)
    alphaAcid = db.Column(db.Float)
    berry = db.Column(db.Float)
    citrus = db.Column(db.Float)
    tart = db.Column(db.Float)
    flowery = db.Column(db.Float)
    earthy = db.Column(db.Float)
    pine = db.Column(db.Float)
    spicy = db.Column(db.Float)
    bitter = db.Column(db.Float)
    flavorProfile = db.Column(db.Text)
    possibleSubstitutions = db.Column(db.Text)
    origin = db.Column(db.String(64))
    storage = db.Column(db.String(64))
    additionalInformation_History = db.Column(db.Text)

    def __repr__(self):
        return '<Role %r>' % self.hops

class Yeast(db.Model):
    __tablename__ = 'gb_constants_yeast'
    id = db.Column(db.Integer, primary_key=True)
    yeastStrain = db.Column(db.String(64), unique=True)
    value = db.Column(db.Float)
    attenuation = db.Column(db.Float)
    temperatureRangeLow = db.Column(db.Integer)
    temperatureRangeHigh = db.Column(db.Integer)
    flocculation = db.Column(db.String(64))
    alcoholTolerancePercentLow = db.Column(db.Float)
    alcoholTolerancePercentHigh = db.Column(db.Float)
    flavorCharacteristics = db.Column(db.Text)
    recommendedStyles = db.Column(db.Text)
    brewery = db.Column(db.String(64))

    def __repr__(self):
        return '<Role %r>' % self.yeastStrain

class Styles(db.Model):
    __tablename__ = 'gb_constants_styles'
    id = db.Column(db.Integer, primary_key=True)
    generalStyle = db.Column(db.String(64))
    styles = db.Column(db.String(64))
    OGRangeLow = db.Column(db.Float)
    OGRangeHigh = db.Column(db.Float)
    FGRangeLow = db.Column(db.Float)
    FGRangeHigh = db.Column(db.Float)
    bitterLow = db.Column(db.Float)
    bitterHigh = db.Column(db.Float)
    SRMRangeLow = db.Column(db.Float)
    SRMRangeHigh = db.Column(db.Float)

    def __repr__(self):
        return '<Role %r>' % self.styles

class utilization_table(db.Model):
    __tablename__ = 'gb_constants_utilization_table'
    id = db.Column(db.Integer, primary_key=True)
    boil_time = db.Column(db.Integer)
    whole_hop = db.Column(db.Float)
    pellet_hop = db.Column(db.Float)

class gravity_correction_chart(db.Model):
    __tablename__ = 'gb_constants_gravity_correction_chart'
    id = db.Column(db.Integer, primary_key=True)
    temperature_F = db.Column(db.Integer)
    temperature_C = db.Column(db.Integer)
    add_SG = db.Column(db.Float)

    def __repr__(self):
        return '<Temperature %r>' % self.temperature_C



# Recipe tables

class Recipe(db.Model):
    __tablename__ = 'gb_recipe_master'
    # Columns
    id = db.Column(db.Integer, primary_key=True)
    recipe = db.Column(db.String(64))
    style = db.Column(db.String(64))
    # Relationships
    fermentables = db.relationship('Recipe_Fermentables', backref='gb_recipe_master', cascade="all, delete-orphan" , lazy='dynamic')
    hops = db.relationship('Recipe_Hops', backref='gb_recipe_master', cascade="all, delete-orphan" , lazy='dynamic')
    mash = db.relationship('Recipe_Mash', backref='gb_recipe_master', cascade="all, delete-orphan" , lazy='dynamic')
    water = db.relationship('Recipe_Water', backref='gb_recipe_master', cascade="all, delete-orphan" , lazy='dynamic')
    fermentation = db.relationship('Recipe_Fermentation', backref='gb_recipe_master', cascade="all, delete-orphan" , lazy='dynamic')
    yeast = db.relationship('Recipe_Yeast', backref='gb_recipe_master', cascade="all, delete-orphan" , lazy='dynamic')
    chemistry = db.relationship('Recipe_Chemistry', backref='gb_recipe_master', cascade="all, delete-orphan" , lazy='dynamic')
    system = db.relationship('Recipe_System', backref='gb_recipe_master', cascade="all, delete-orphan" , lazy='dynamic')

    def __repr__(self):
        return '<Recipe: %r>' % self.recipe

class Recipe_System(db.Model):
    __tablename__ = 'gb_recipe_system'
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('gb_recipe_master.id', ondelete='CASCADE'), nullable=False)
    batch_size = db.Column(db.Float)
    extraction_efficiency = db.Column(db.Float)

    def __repr__(self):
        return '<System for recipe_id: %r>' % self.recipe_id

class Recipe_Fermentables(db.Model):
    __tablename__ = 'gb_recipe_fermentables'
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('gb_recipe_master.id', ondelete='CASCADE'), nullable=False)
    ingredient = db.Column(db.String(64))
    weight_lbs = db.Column(db.Float)

    def __repr__(self):
        return '<Fermentable: %r>' % self.ingredient

class Recipe_Hops(db.Model):
    __tablename__ = 'gb_recipe_hops'
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('gb_recipe_master.id', ondelete='CASCADE'), nullable=False)
    hop = db.Column(db.String(64))
    weight_oz = db.Column(db.Float)
    boil_time_min = db.Column(db.Integer)
    

    def __repr__(self):
        return '<Hop: %r>' % self.hop

class Recipe_Mash(db.Model):
    __tablename__ = 'gb_recipe_mash'
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('gb_recipe_master.id', ondelete='CASCADE'), nullable=False)
    init_grain_temp = db.Column(db.Float)
    sacc_rest_temp = db.Column(db.Float)
    mash_duration = db.Column(db.Integer)
    mash_thickness = db.Column(db.Float)

    def __repr__(self):
        return '<Mash for recipe_id: %r>' % self.recipe_id

class Recipe_Yeast(db.Model):
    __tablename__ = 'gb_recipe_yeast'
    id = db.Column(db.Integer, primary_key=True)    
    recipe_id = db.Column(db.Integer, db.ForeignKey('gb_recipe_master.id', ondelete='CASCADE'), nullable=False)
    yeast_name = db.Column(db.String(64))
    init_cells = db.Column(db.Float)

    def __repr__(self):
        return '<Yeast: %r>' % self.yeast_name

class Recipe_Water(db.Model):
    __tablename__ = 'gb_recipe_water'
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('gb_recipe_master.id', ondelete='CASCADE'), nullable=False)
    total_boil_time = db.Column(db.Float)
    evap_rate = db.Column(db.Float)
    shrinkage = db.Column(db.Float)
    mash_tun_dead_space = db.Column(db.Float)
    lauter_tun_dead_space = db.Column(db.Float)
    kettle_dead_space = db.Column(db.Float)
    fermentation_tank_loss = db.Column(db.Float)
    grain_abs_factor = db.Column(db.Float)
    


    def __repr__(self):
        return '<Water for recipe_id: %r>' % self.recipe_id

class Recipe_Fermentation(db.Model):
    __tablename__ = 'gb_recipe_fermentation'
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('gb_recipe_master.id', ondelete='CASCADE'), nullable=False)
    days1 = db.Column(db.Integer)
    temp1 = db.Column(db.Integer)
    days2 = db.Column(db.Integer)
    temp2 = db.Column(db.Integer)
    days3 = db.Column(db.Integer)
    temp3 = db.Column(db.Integer)
    days4 = db.Column(db.Integer)
    temp4 = db.Column(db.Integer)
    days5 = db.Column(db.Integer)
    temp5 = db.Column(db.Integer)


    def __repr__(self):
        return '<Fermentation for recipe_id: %r>' % self.recipe_id


class Recipe_Chemistry(db.Model):
    __tablename__ = 'gb_recipe_chemistry'
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('gb_recipe_master.id', ondelete='CASCADE'), nullable=False)
    init_Ca = db.Column(db.Float)
    init_Mg = db.Column(db.Float)
    init_Na = db.Column(db.Float)
    init_Cl = db.Column(db.Float)
    init_SO4 = db.Column(db.Float)
    init_HCO3_CaCO3 = db.Column(db.Float)
    actual_ph = db.Column(db.Float)
    effective_alkalinity = db.Column(db.Float)
    residual_alkalinity = db.Column(db.Float)
    ph_down_gypsum_CaSO4 = db.Column(db.Float)
    ph_down_cal_chl_CaCl2 = db.Column(db.Float)
    ph_down_epsom_salt_MgSO4 = db.Column(db.Float)
    ph_up_slaked_lime_CaOH2 = db.Column(db.Float)
    ph_up_baking_soda_NaHCO3 = db.Column(db.Float)
    ph_up_chalk_CaCO3 = db.Column(db.Float)

    def __repr__(self):
        return '<Chemistry for recipe_id: %r>' % self.recipe_id





