import pandas as pd, psycopg2 as pg, os

psql = pd.io.sql


# BB - need to use the venv3.6

# get connected to the database
connection = pg.connect("host='ec2-23-21-229-48.compute-1.amazonaws.com' dbname=d4hvr3omam72o1 user=xjedptgsjqocwi password='25dfb7913372da245831b379d76ddb39eaf18eac98eade1b9542bc3ff0936dc4'")

 
gb_recipe_master = psql.read_sql_query("SELECT * FROM public.gb_recipe_master", connection)
gb_recipe_chemistry = psql.read_sql_query("SELECT * FROM public.gb_recipe_chemistry", connection)
gb_recipe_fermentables = psql.read_sql_query("SELECT * FROM public.gb_recipe_fermentables", connection)
gb_recipe_fermentation = psql.read_sql_query("SELECT * FROM public.gb_recipe_fermentation", connection)
gb_recipe_hops = psql.read_sql_query("SELECT * FROM public.gb_recipe_hops", connection)
gb_recipe_mash = psql.read_sql_query("SELECT * FROM public.gb_recipe_mash", connection)
gb_recipe_system = psql.read_sql_query("SELECT * FROM public.gb_recipe_system", connection)
gb_recipe_water = psql.read_sql_query("SELECT * FROM public.gb_recipe_water", connection)
gb_recipe_yeast = psql.read_sql_query("SELECT * FROM public.gb_recipe_yeast", connection)

tables = {
    'gb_recipe_master' : gb_recipe_master,
    'gb_recipe_chemistry' : gb_recipe_chemistry,
    'gb_recipe_fermentables' : gb_recipe_fermentables,
    'gb_recipe_fermentation' : gb_recipe_fermentation,
    'gb_recipe_hops' : gb_recipe_hops,
    'gb_recipe_mash' : gb_recipe_mash,
    'gb_recipe_system' : gb_recipe_system,
    'gb_recipe_water' : gb_recipe_water,
    'gb_recipe_yeast' : gb_recipe_yeast
}

date = '03_29_2020'
os.mkdir('manual_db_backup/{}'.format(date))


for table in tables.keys():
    tables[table].to_csv('manual_db_backup/{}/{}.csv'.format(date, table), index=None)

# print(dataframe)


