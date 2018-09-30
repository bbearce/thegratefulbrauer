$(function() {
$('#load').bind('click', function() {

  // Go to load in python and pass in the recipe input value
  $.getJSON($SCRIPT_ROOT + '/load', {
    recipe: $('input[name="recipe"]').val(),

  // the load() function returns a json object with key value pairs
  }, function(data) {
    loaded_data = data

    if (data['recipe'] == "that recipe doesn't exist"){
    
    // If this recipe doesn't exist in the database then tell the user.

    $('#messages').text("That recipe doesn't exist")

    } else {
    // If this recipe exists in the database then tell the user and load it.

    $('#messages').text("You have loaded recipe "+loaded_data['data']['Recipe']['gb_recipe_master']['recipe'])

    // Recipe
    $('select[name="style"]').val(loaded_data['data']['Recipe']['gb_recipe_master']['style'])

    // System
    $('input[name="batch_size"]').val(loaded_data['data']['Recipe']['gb_recipe_system']['batch_size'])
    $('input[name="extraction_efficiency"]').val(loaded_data['data']['Recipe']['gb_recipe_system']['extraction_efficiency'])

    // Fermentables
    $('select[name="ingredient1"]').val(loaded_data['data']['Recipe']['gb_recipe_fermentables'][0]['ingredient'])
    $('input[name="weight_lbs1"]').val(loaded_data['data']['Recipe']['gb_recipe_fermentables'][0]['weight_lbs'])
    
    $('select[name="ingredient2"]').val(loaded_data['data']['Recipe']['gb_recipe_fermentables'][1]['ingredient'])
    $('input[name="weight_lbs2"]').val(loaded_data['data']['Recipe']['gb_recipe_fermentables'][1]['weight_lbs'])
    
    $('select[name="ingredient3"]').val(loaded_data['data']['Recipe']['gb_recipe_fermentables'][2]['ingredient'])
    $('input[name="weight_lbs3"]').val(loaded_data['data']['Recipe']['gb_recipe_fermentables'][2]['weight_lbs'])
    
    $('select[name="ingredient4"]').val(loaded_data['data']['Recipe']['gb_recipe_fermentables'][3]['ingredient'])
    $('input[name="weight_lbs4"]').val(loaded_data['data']['Recipe']['gb_recipe_fermentables'][3]['weight_lbs'])
    
    $('select[name="ingredient5"]').val(loaded_data['data']['Recipe']['gb_recipe_fermentables'][4]['ingredient'])
    $('input[name="weight_lbs5"]').val(loaded_data['data']['Recipe']['gb_recipe_fermentables'][4]['weight_lbs'])
    

    // Hops
    $('select[name="hop1"]').val(loaded_data['data']['Recipe']['gb_recipe_hops'][0]['hop'])
    $('input[name="weight_oz1"]').val(loaded_data['data']['Recipe']['gb_recipe_hops'][0]['weight_oz'])
    $('input[name="boil_time_min1"]').val(loaded_data['data']['Recipe']['gb_recipe_hops'][0]['boil_time_min'])
    $('input[name="alpha_acid_content1"]').val(loaded_data['data']['Recipe']['gb_recipe_hops'][0]['alpha_acid_content'])
    $('input[name="utilization1"]').val(loaded_data['data']['Recipe']['gb_recipe_hops'][0]['utilization'])
    $('input[name="ibu1"]').val(loaded_data['data']['Recipe']['gb_recipe_hops'][0]['ibu'])

    $('select[name="hop2"]').val(loaded_data['data']['Recipe']['gb_recipe_hops'][1]['hop'])
    $('input[name="weight_oz2"]').val(loaded_data['data']['Recipe']['gb_recipe_hops'][1]['weight_oz'])
    $('input[name="boil_time_min2"]').val(loaded_data['data']['Recipe']['gb_recipe_hops'][1]['boil_time_min'])
    $('input[name="alpha_acid_content2"]').val(loaded_data['data']['Recipe']['gb_recipe_hops'][1]['alpha_acid_content'])
    $('input[name="utilization2"]').val(loaded_data['data']['Recipe']['gb_recipe_hops'][1]['utilization'])
    $('input[name="ibu2"]').val(loaded_data['data']['Recipe']['gb_recipe_hops'][1]['ibu'])

    $('select[name="hop3"]').val(loaded_data['data']['Recipe']['gb_recipe_hops'][2]['hop'])
    $('input[name="weight_oz3"]').val(loaded_data['data']['Recipe']['gb_recipe_hops'][2]['weight_oz'])
    $('input[name="boil_time_min3"]').val(loaded_data['data']['Recipe']['gb_recipe_hops'][2]['boil_time_min'])
    $('input[name="alpha_acid_content3"]').val(loaded_data['data']['Recipe']['gb_recipe_hops'][2]['alpha_acid_content'])
    $('input[name="utilization3"]').val(loaded_data['data']['Recipe']['gb_recipe_hops'][2]['utilization'])
    $('input[name="ibu3"]').val(loaded_data['data']['Recipe']['gb_recipe_hops'][2]['ibu'])

    // Mash
    $('input[name="init_grain_temp"]').val(loaded_data['data']['Recipe']['gb_recipe_mash']['init_grain_temp'])
    $('input[name="infusion_temp"]').val(loaded_data['data']['Recipe']['gb_recipe_mash']['infusion_temp'])
    $('input[name="sacc_rest_temp"]').val(loaded_data['data']['Recipe']['gb_recipe_mash']['sacc_rest_temp'])
    $('input[name="mash_duration"]').val(loaded_data['data']['Recipe']['gb_recipe_mash']['mash_duration'])
    $('input[name="mash_volume"]').val(loaded_data['data']['Recipe']['gb_recipe_mash']['mash_volume'])
    $('input[name="mash_thickness"]').val(loaded_data['data']['Recipe']['gb_recipe_mash']['mash_thickness'])
    $('input[name="mash_out_vol"]').val(loaded_data['data']['Recipe']['gb_recipe_mash']['mash_out_vol'])

    // Yeast
    $('select[name="yeast_name"]').val(loaded_data['data']['Recipe']['gb_recipe_yeast']['yeast_name'])
    $('input[name="attenuation"]').val(loaded_data['data']['Recipe']['gb_recipe_yeast']['attenuation'])
    $('input[name="abv"]').val(loaded_data['data']['Recipe']['gb_recipe_yeast']['abv'])
    $('input[name="og"]').val(loaded_data['data']['Recipe']['gb_recipe_yeast']['og'])
    $('input[name="fg"]').val(loaded_data['data']['Recipe']['gb_recipe_yeast']['fg'])
    $('input[name="init_cells"]').val(loaded_data['data']['Recipe']['gb_recipe_yeast']['init_cells'])
    $('input[name="pitched_cells"]').val(loaded_data['data']['Recipe']['gb_recipe_yeast']['pitched_cells'])
    $('input[name="liters_for_starter"]').val(loaded_data['data']['Recipe']['gb_recipe_yeast']['liters_for_starter'])

    // Water
    $('input[name="total_boil_time"]').val(loaded_data['data']['Recipe']['gb_recipe_water']['total_boil_time'])
    $('input[name="evap_rate"]').val(loaded_data['data']['Recipe']['gb_recipe_water']['evap_rate'])
    $('input[name="shrinkage"]').val(loaded_data['data']['Recipe']['gb_recipe_water']['shrinkage'])
    $('input[name="mash_tun_dead_space"]').val(loaded_data['data']['Recipe']['gb_recipe_water']['mash_tun_dead_space'])
    $('input[name="lauter_tun_dead_space"]').val(loaded_data['data']['Recipe']['gb_recipe_water']['lauter_tun_dead_space'])
    $('input[name="kettle_dead_space"]').val(loaded_data['data']['Recipe']['gb_recipe_water']['kettle_dead_space'])
    $('input[name="fermentation_tank_loss"]').val(loaded_data['data']['Recipe']['gb_recipe_water']['fermentation_tank_loss'])
    $('input[name="grain_abs_factor"]').val(loaded_data['data']['Recipe']['gb_recipe_water']['grain_abs_factor'])
    
    // Fermentation
    $('input[name="days1"]').val(loaded_data['data']['Recipe']['gb_recipe_fermentation']['days1'])
    $('input[name="temp1"]').val(loaded_data['data']['Recipe']['gb_recipe_fermentation']['temp1'])
    $('input[name="days2"]').val(loaded_data['data']['Recipe']['gb_recipe_fermentation']['days2'])
    $('input[name="temp2"]').val(loaded_data['data']['Recipe']['gb_recipe_fermentation']['temp2'])
    $('input[name="days3"]').val(loaded_data['data']['Recipe']['gb_recipe_fermentation']['days3'])
    $('input[name="temp3"]').val(loaded_data['data']['Recipe']['gb_recipe_fermentation']['temp3'])
    $('input[name="days4"]').val(loaded_data['data']['Recipe']['gb_recipe_fermentation']['days4'])
    $('input[name="temp4"]').val(loaded_data['data']['Recipe']['gb_recipe_fermentation']['temp4'])
    $('input[name="days5"]').val(loaded_data['data']['Recipe']['gb_recipe_fermentation']['days5'])
    $('input[name="temp5"]').val(loaded_data['data']['Recipe']['gb_recipe_fermentation']['temp5'])

    // Chemistry
    $('input[name="init_Ca"]').val(loaded_data['data']['Recipe']['gb_recipe_chemistry']['init_Ca'])
    $('input[name="init_Mg"]').val(loaded_data['data']['Recipe']['gb_recipe_chemistry']['init_Mg'])
    $('input[name="init_Na"]').val(loaded_data['data']['Recipe']['gb_recipe_chemistry']['init_Na'])
    $('input[name="init_Cl"]').val(loaded_data['data']['Recipe']['gb_recipe_chemistry']['init_Cl'])
    $('input[name="init_SO4"]').val(loaded_data['data']['Recipe']['gb_recipe_chemistry']['init_SO4'])
    $('input[name="init_HCO3_CaCO3"]').val(loaded_data['data']['Recipe']['gb_recipe_chemistry']['init_HCO3_CaCO3'])
    $('input[name="actual_ph"]').val(loaded_data['data']['Recipe']['gb_recipe_chemistry']['actual_ph'])
    $('input[name="effective_alkalinity"]').val(loaded_data['data']['Recipe']['gb_recipe_chemistry']['effective_alkalinity'])
    $('input[name="residual_alkalinity"]').val(loaded_data['data']['Recipe']['gb_recipe_chemistry']['residual_alkalinity'])
    $('input[name="ph_down_gypsum_CaSO4"]').val(loaded_data['data']['Recipe']['gb_recipe_chemistry']['ph_down_gypsum_CaSO4'])
    $('input[name="ph_down_cal_chl_CaCl2"]').val(loaded_data['data']['Recipe']['gb_recipe_chemistry']['ph_down_cal_chl_CaCl2'])
    $('input[name="ph_down_epsom_salt_MgSO4"]').val(loaded_data['data']['Recipe']['gb_recipe_chemistry']['ph_down_epsom_salt_MgSO4'])
    $('input[name="ph_up_slaked_lime_CaOH2"]').val(loaded_data['data']['Recipe']['gb_recipe_chemistry']['ph_up_slaked_lime_CaOH2'])
    $('input[name="ph_up_baking_soda_NaHCO3"]').val(loaded_data['data']['Recipe']['gb_recipe_chemistry']['ph_up_baking_soda_NaHCO3'])
    $('input[name="ph_up_chalk_CaCO3"]').val(loaded_data['data']['Recipe']['gb_recipe_chemistry']['ph_up_chalk_CaCO3'])


    //// Rerun app calculations

    // Fermentables
    $('#OG').text(calc_og().toFixed(3)); //toFixed() is a rounding method
    make_chart();

    // Hops
    get_hop_info()
    $('#total_ibu').text(calc_ibu().toFixed(3)); //toFixed() is a rounding method 
    make_hops_chart()

    // Yeast

    // Mash

    // Water

    // Chemistry

    // Fermentation

    
    
    }


    

  });
  return false;
});
});