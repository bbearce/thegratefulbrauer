# sqlite

sqlite> .separator ,
sqlite> .import <path>/data.csv <table>

# load thegratefulbrauer db tables
sqlite> .separator
sqlite> .import /Users/bbearce/Documents/Code/Heroku/thegratefulbrauer/static/database_csvs/fermentables.csv gb_constants_fermentables
sqlite> .import /Users/bbearce/Documents/Code/Heroku/thegratefulbrauer/static/database_csvs/hops.csv gb_constants_hops
sqlite> .import /Users/bbearce/Documents/Code/Heroku/thegratefulbrauer/static/database_csvs/styles.csv gb_constants_styles
sqlite> .import /Users/bbearce/Documents/Code/Heroku/thegratefulbrauer/static/database_csvs/yeast.csv gb_constants_yeast
sqlite> .import /Users/bbearce/Documents/Code/Heroku/thegratefulbrauer/static/database_csvs/gravity_correction_chart.csv gb_constants_gravity_correction_chart



# postgres
\copy gb_constants_fermentables FROM '/Users/bbearce/Documents/Code/Heroku/thegratefulbrauer/static/database_csvs/fermentables.csv' DELIMITER ',' CSV
\copy gb_constants_hops FROM '/Users/bbearce/Documents/Code/Heroku/thegratefulbrauer/static/database_csvs/hops.csv' DELIMITER ',' CSV
\copy gb_constants_styles FROM '/Users/bbearce/Documents/Code/Heroku/thegratefulbrauer/static/database_csvs/styles.csv' DELIMITER ',' CSV
\copy gb_constants_yeast FROM '/Users/bbearce/Documents/Code/Heroku/thegratefulbrauer/static/database_csvs/yeast.csv' DELIMITER ',' CSV
\copy gb_constants_gravity_correction_chart FROM '/Users/bbearce/Documents/Code/Heroku/thegratefulbrauer/static/database_csvs/gravity_correction_chart.csv' DELIMITER ',' CSV
\copy gb_utilization_table FROM '/Users/bbearce/Documents/Code/Heroku/thegratefulbrauer/static/database_csvs/utilization_table.csv' DELIMITER ',' CSV


# in postico app
copy gb_constants_fermentables FROM '/Users/bbearce/Documents/Code/Heroku/thegratefulbrauer/static/database_csvs/fermentables.csv' DELIMITER ',' CSV;
copy gb_constants_hops FROM '/Users/bbearce/Documents/Code/Heroku/thegratefulbrauer/static/database_csvs/hops.csv' DELIMITER ',' CSV;
copy gb_constants_styles FROM '/Users/bbearce/Documents/Code/Heroku/thegratefulbrauer/static/database_csvs/styles.csv' DELIMITER ',' CSV;
copy gb_constants_yeast FROM '/Users/bbearce/Documents/Code/Heroku/thegratefulbrauer/static/database_csvs/yeast.csv' DELIMITER ',' CSV;
copy gb_constants_gravity_correction_chart FROM '/Users/bbearce/Documents/Code/Heroku/thegratefulbrauer/static/database_csvs/gravity_correction_chart.csv' DELIMITER ',' CSV;
copy gb_constants_utilization_table FROM '/Users/bbearce/Documents/Code/Heroku/thegratefulbrauer/static/database_csvs/utilization_table.csv' DELIMITER ',' CSV


select * from gb_recipe_mash limit 100;

select * from gb_constants_utilization_table limit 100;
select * from gb_constants_hops limit 100;
select * from gb_constants_styles limit 100;
select * from gb_constants_hops limit 100;
select * from gb_constants_yeast limit 100;
delete from gb_constants_yeast;

select * from gb_constants_fermentables limit 100;

select * from gb_recipe_mash limit 100;
select * from gb_recipe_yeast limit 100;


