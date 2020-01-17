import pandas as pd, psycopg2 as pg

psql = pd.io.sql


# BB - need to use the venv3.6

# get connected to the database
connection = pg.connect("host='ec2-23-21-229-48.compute-1.amazonaws.com' dbname=d4hvr3omam72o1 user=xjedptgsjqocwi password='25dfb7913372da245831b379d76ddb39eaf18eac98eade1b9542bc3ff0936dc4'")

 
dataframe = psql.read_sql_query("SELECT * FROM public.gb_recipe_master", connection)

print(dataframe)


