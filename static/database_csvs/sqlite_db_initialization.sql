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
\copy fermentables FROM '/Users/bbearce/Documents/thegratefulbrauer/static/database_csvs/fermentables.csv' DELIMITER ',' CSV
\copy hops FROM '/Users/bbearce/Documents/thegratefulbrauer/static/database_csvs/hops.csv' DELIMITER ',' CSV
\copy styles FROM '/Users/bbearce/Documents/thegratefulbrauer/static/database_csvs/styles.csv' DELIMITER ',' CSV
\copy yeast FROM '/Users/bbearce/Documents/thegratefulbrauer/static/database_csvs/yeast.csv' DELIMITER ',' CSV
\copy gravity_correction_chart FROM '/Users/bbearce/Documents/thegratefulbrauer/static/database_csvs/gravity_correction_chart.csv' DELIMITER ',' CSV
