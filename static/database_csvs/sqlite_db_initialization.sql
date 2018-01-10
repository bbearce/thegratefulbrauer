sqlite> .separator ,
sqlite> .import <path>/data.csv <table>

# load thegratefulbrauer db tables
sqlite> .separator
sqlite> .import /Users/bbearce/Documents/thegratefulbrauer/static/database_csvs/fermentables.csv fermentables
sqlite> .import /Users/bbearce/Documents/thegratefulbrauer/static/database_csvs/hops.csv hops
sqlite> .import /Users/bbearce/Documents/thegratefulbrauer/static/database_csvs/styles.csv styles
sqlite> .import /Users/bbearce/Documents/thegratefulbrauer/static/database_csvs/yeast.csv yeast
sqlite> .import /Users/bbearce/Documents/thegratefulbrauer/static/database_csvs/gravity_correction_chart.csv gravity_correction_chart