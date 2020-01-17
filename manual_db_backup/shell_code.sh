
# connection to postgres can be made from a shell command heroku has. Goto heroku.com and look under postgres settings.

\copy gb_recipe_master FROM '/home/bbearce/Documents/thegratefulbrauer/manual_db_backup/recipe_master.csv' DELIMITERS ',' CSV QUOTE E'\'' HEADER;

\copy gb_recipe_chemistry FROM '/home/bbearce/Documents/thegratefulbrauer/manual_db_backup/recipe_chemistry.csv' DELIMITERS ',' CSV QUOTE E'\'' HEADER;
\copy gb_recipe_fermentables FROM '/home/bbearce/Documents/thegratefulbrauer/manual_db_backup/recipe_fermentables.csv' DELIMITERS ',' CSV QUOTE E'\'' HEADER;
\copy gb_recipe_fermentation FROM '/home/bbearce/Documents/thegratefulbrauer/manual_db_backup/recipe_fermentation.csv' DELIMITERS ',' CSV QUOTE E'\'' HEADER;
\copy gb_recipe_hops FROM '/home/bbearce/Documents/thegratefulbrauer/manual_db_backup/recipe_hops.csv' DELIMITERS ',' CSV QUOTE E'\'' HEADER;
\copy gb_recipe_mash FROM '/home/bbearce/Documents/thegratefulbrauer/manual_db_backup/recipe_mash.csv' DELIMITERS ',' CSV QUOTE E'\'' HEADER;
\copy gb_recipe_system FROM '/home/bbearce/Documents/thegratefulbrauer/manual_db_backup/recipe_system.csv' DELIMITERS ',' CSV QUOTE E'\'' HEADER;
\copy gb_recipe_water FROM '/home/bbearce/Documents/thegratefulbrauer/manual_db_backup/recipe_water.csv' DELIMITERS ',' CSV QUOTE E'\'' HEADER;
\copy gb_recipe_yeast FROM '/home/bbearce/Documents/thegratefulbrauer/manual_db_backup/recipe_yeast.csv' DELIMITERS ',' CSV QUOTE E'\'' HEADER;

