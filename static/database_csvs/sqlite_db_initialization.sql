# sqlite

sqlite> .separator ,
sqlite> .import <path>/data.csv <table>

# load thegratefulbrauer db tables
sqlite> .separator
sqlite> .import /Users/bbearce/Documents/thegratefulbrauer/static/database_csvs/fermentables.csv fermentables
sqlite> .import /Users/bbearce/Documents/thegratefulbrauer/static/database_csvs/hops.csv hops
sqlite> .import /Users/bbearce/Documents/thegratefulbrauer/static/database_csvs/styles.csv styles
sqlite> .import /Users/bbearce/Documents/thegratefulbrauer/static/database_csvs/yeast.csv yeast
sqlite> .import /Users/bbearce/Documents/thegratefulbrauer/static/database_csvs/gravity_correction_chart.csv gravity_correction_chart



# postgres
\copy gb_constants_fermentables FROM '/Users/bbearce/Documents/Code/Heroku/Python_Brew_App/static/db_constants/fermentables distilled_values.csv' DELIMITER ',' CSV;
\copy gb_constants_hops FROM '/Users/bbearce/Documents/Code/Heroku/Python_Brew_App/static/db_constants/hops.csv' DELIMITER ',' CSV;
\copy gb_constants_styles FROM '/Users/bbearce/Documents/Code/Heroku/Python_Brew_App/static/db_constants/styles.csv' DELIMITER ',' CSV;
\copy gb_constants_yeast FROM '/Users/bbearce/Documents/Code/Heroku/Python_Brew_App/static/db_constants/yeast.csv' DELIMITER ',' CSV;
\copy gb_constants_gravity_correction_chart FROM '/Users/bbearce/Documents/Code/Heroku/Python_Brew_App/static/db_constants/gravity_correction_chart.csv' DELIMITER ',' CSV;
\copy gb_constants_utilization_table FROM '/Users/bbearce/Documents/Code/Heroku/Python_Brew_App/static/db_constants/utilization_table.csv' DELIMITER ',' CSV