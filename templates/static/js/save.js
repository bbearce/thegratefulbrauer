$(function() {
$('#save').bind('click', 
  function() {
    $.getJSON($SCRIPT_ROOT + '/save', 

              {
               // Recipe
               recipe: $('input[name="recipe"]').val(),
               style: $('select[name="style"]').val(),

               // System Table
               batch_size: $('input[name="batch_size"]').val(),
               extraction_efficiency: $('input[name="extraction_efficiency"]').val(),

               // Fermentables Table
               ingredient1: $('select[name="ingredient1"]').val(),
               weight_lbs1: $('input[name="weight_lbs1"]').val(),
               percent_of_total1: $('input[name="percent_of_total1"]').val(),
               
               ingredient2: $('select[name="ingredient2"]').val(),
               weight_lbs2: $('input[name="weight_lbs2"]').val(),
               percent_of_total2: $('input[name="percent_of_total2"]').val(),
               
               ingredient3: $('select[name="ingredient3"]').val(),
               weight_lbs3: $('input[name="weight_lbs3"]').val(),
               percent_of_total3: $('input[name="percent_of_total3"]').val(),
               
               ingredient4: $('select[name="ingredient4"]').val(),
               weight_lbs4: $('input[name="weight_lbs4"]').val(),
               percent_of_total4: $('input[name="percent_of_total4"]').val(),

               ingredient5: $('select[name="ingredient5"]').val(),
               weight_lbs5: $('input[name="weight_lbs5"]').val(),
               percent_of_total5: $('input[name="percent_of_total5"]').val(),


               // Hops Table
               hop1: $('select[name="hop1"]').val(),
               weight_oz1: $('input[name="weight_oz1"]').val(),
               boil_time_min1: $('input[name="boil_time_min1"]').val(),

               hop2: $('select[name="hop2"]').val(),
               weight_oz2: $('input[name="weight_oz2"]').val(),
               boil_time_min2: $('input[name="boil_time_min2"]').val(),

               hop3: $('select[name="hop3"]').val(),
               weight_oz3: $('input[name="weight_oz3"]').val(),
               boil_time_min3: $('input[name="boil_time_min3"]').val(),

               // Mash Table
               init_grain_temp: $('input[name="init_grain_temp"]').val(),
               sacc_rest_temp: $('input[name="sacc_rest_temp"]').val(),
               mash_duration: $('input[name="mash_duration"]').val(),
               mash_thickness: $('input[name="mash_thickness"]').val(),
               
               // Yeast Table
               yeast_name: $('select[name="yeast_name"]').val(),
               init_cells: $('input[name="init_cells"]').val(),

               // Water Table
               total_boil_time: $('input[name="total_boil_time"]').val(),
               evap_rate: $('input[name="evap_rate"]').val(),
               shrinkage: $('input[name="shrinkage"]').val(),
               mash_tun_dead_space: $('input[name="mash_tun_dead_space"]').val(),
               lauter_tun_dead_space: $('input[name="lauter_tun_dead_space"]').val(),
               kettle_dead_space: $('input[name="kettle_dead_space"]').val(),
               fermentation_tank_loss: $('input[name="fermentation_tank_loss"]').val(),
               grain_abs_factor: $('input[name="grain_abs_factor"]').val(),

               // Fermentation Table
               days1: $('input[name="days1"]').val(),
               temp1: $('input[name="temp1"]').val(),
               days2: $('input[name="days2"]').val(),
               temp2: $('input[name="temp2"]').val(),
               days3: $('input[name="days3"]').val(),
               temp3: $('input[name="temp3"]').val(),
               days4: $('input[name="days4"]').val(),
               temp4: $('input[name="temp4"]').val(),
               days5: $('input[name="days5"]').val(),
               temp5: $('input[name="temp5"]').val(),

               // Chemistry
               init_Ca: $('input[name="init_Ca"]').val(),
               init_Mg: $('input[name="init_Mg"]').val(),
               init_Na: $('input[name="init_Na"]').val(),
               init_Cl: $('input[name="init_Cl"]').val(),
               init_SO4: $('input[name="init_SO4"]').val(),
               init_HCO3_CaCO3: $('input[name="init_HCO3_CaCO3"]').val(),
               actual_ph: $('input[name="actual_ph"]').val(),
               effective_alkalinity: $('input[name="effective_alkalinity"]').val(),
               residual_alkalinity: $('input[name="residual_alkalinity"]').val(),
               ph_down_gypsum_CaSO4: $('input[name="ph_down_gypsum_CaSO4"]').val(),
               ph_down_cal_chl_CaCl2: $('input[name="ph_down_cal_chl_CaCl2"]').val(),
               ph_down_epsom_salt_MgSO4: $('input[name="ph_down_epsom_salt_MgSO4"]').val(),
               ph_up_slaked_lime_CaOH2: $('input[name="ph_up_slaked_lime_CaOH2"]').val(),
               ph_up_baking_soda_NaHCO3: $('input[name="ph_up_baking_soda_NaHCO3"]').val(),
               ph_up_chalk_CaCO3: $('input[name="ph_up_chalk_CaCO3"]').val(),



              },

              function(data) {

              if (data['recipe'] == "that recipe already exists") {
                  $("#messages").text("That recipe already exists, please try another name")
              } else { 
                  $("#messages").text("You just saved "+data['recipe'])
              }

              }
    );

  return false;
  }
);
});