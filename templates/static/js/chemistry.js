function get_chemistry_info(){

    init_Ca = parseFloat($("input[name='init_Ca']")[0].value)
    init_Mg = parseFloat($("input[name='init_Mg']")[0].value)
    init_Na = parseFloat($("input[name='init_Na']")[0].value)
    init_Cl = parseFloat($("input[name='init_Cl']")[0].value)
    init_SO4 = parseFloat($("input[name='init_SO4']")[0].value)
    init_HCO3_or_CaCO3 = parseFloat($("input[name='init_HCO3_CaCO3']")[0].value)

    // Distilled Percentages
    mash_distilled_percent = parseFloat($("input[name='mash_distilled_percent']")[0].value)
    sparge_distilled_percent = parseFloat($("input[name='sparge_distilled_percent']")[0].value)

    // Special Adjustments
    acidulated_malt_percent = parseFloat($("input[name='acidulated_malt_percent']")[0].value)
    lactic_acid_percent = parseFloat($("input[name='lactic_acid_percent']")[0].value)
    acidulated_malt_oz = parseFloat($("input[name='acidulated_malt_oz']")[0].value)
    lactic_acid_ml = parseFloat($("input[name='lactic_acid_ml']")[0].value)

    // Mash pH_down
    mash_ph_down_gypsum_CaSO4 = parseFloat($("input[name='mash_ph_down_gypsum_CaSO4']")[0].value)
    mash_ph_down_cal_chl_CaCl2 = parseFloat($("input[name='mash_ph_down_cal_chl_CaCl2']")[0].value)
    mash_ph_down_epsom_salt_MgSO4 = parseFloat($("input[name='mash_ph_down_epsom_salt_MgSO4']")[0].value)

    // Mash pH_up
    mash_ph_up_slaked_lime_CaOH2 = parseFloat($("input[name='mash_ph_up_slaked_lime_CaOH2']")[0].value)
    mash_ph_up_baking_soda_NaHCO3 = parseFloat($("input[name='mash_ph_up_baking_soda_NaHCO3']")[0].value)
    mash_ph_up_chalk_CaCO3 = parseFloat($("input[name='mash_ph_up_chalk_CaCO3']")[0].value)

    // Sparge pH_down
    sparge_ph_down_gypsum_CaSO4 = parseFloat($("input[name='sparge_ph_down_gypsum_CaSO4']")[0].value)
    sparge_ph_down_cal_chl_CaCl2 = parseFloat($("input[name='sparge_ph_down_cal_chl_CaCl2']")[0].value)
    sparge_ph_down_epsom_salt_MgSO4 = parseFloat($("input[name='sparge_ph_down_epsom_salt_MgSO4']")[0].value)

    // Sparge pH_up
    sparge_ph_up_slaked_lime_CaOH2 = parseFloat($("input[name='sparge_ph_up_slaked_lime_CaOH2']")[0].value)
    sparge_ph_up_baking_soda_NaHCO3 = parseFloat($("input[name='sparge_ph_up_baking_soda_NaHCO3']")[0].value)
    sparge_ph_up_chalk_CaCO3 = parseFloat($("input[name='sparge_ph_up_chalk_CaCO3']")[0].value)


    get_mash_info()
    // We have these variables after calling get_mash_info:
    // total_grains = calc_percent_of_total()
    // mash_volume = total*(mash_thickness/4) // Convert to [Gal] for mash_thickness
    // infusion_temp = (0.2/mash_thickness)*(sacc_rest_temp-init_grain_temp)+sacc_rest_temp
    // mash_out_volume = ( (170 - sacc_rest_temp)*(0.2*total_grains+mash_volume) ) / (212 - 170)

    get_water_info()
    // We have these variables after calling get_water_info:
    // total_boil_time
    // evap_rate
    // shrinkage
    // mash_tun_dead_space
    // lauter_tun_dead_space
    // kettle_dead_space
    // fermentation_tank_loss
    // grain_abs_factor
    // PBV - Pre-Boil Volume
    // EL - Equipment Loss
    // VFR - Volume From Runnings
    // SV - Sparge Volume
    // SVPMO - Sparge Volume Post Mash Out
    // TW - Total Water Volume


}

function calculate_ph_and_resulting_water_profile(){

    // Calculate Post Mash Additions
    mash_Ca = init_Ca + (
              mash_ph_up_chalk_CaCO3*105.89 + 
              mash_ph_down_gypsum_CaSO4*60 + 
              mash_ph_down_cal_chl_CaCl2*72 + 
              mash_ph_up_slaked_lime_CaOH2*143)/((mash_volume == 0) ? 1 : mash_volume)
    mash_Mg = init_Mg + (
              mash_ph_down_epsom_salt_MgSO4*24.6)/((mash_volume == 0) ? 1 : mash_volume)
        
    mash_Na = init_Na + (
              mash_ph_up_baking_soda_NaHCO3*72.3)/((mash_volume == 0) ? 1 : mash_volume)
    mash_Cl = init_Cl + (
              mash_ph_down_cal_chl_CaCl2*127.47)/((mash_volume == 0) ? 1 : mash_volume)
    mash_SO4 = init_SO4 + (
               mash_ph_down_gypsum_CaSO4*147.4 + 
               mash_ph_down_epsom_salt_MgSO4*103)/((mash_volume == 0) ? 1 : mash_volume)

    // Calculate Distilled Mash pH by fermentable
    for (var i = 0; i<fermentables_properties.length;i++) {
        fermentables_properties[i]['distilled_water_ph'] = ((fermentables_properties[i]['ez_water_code'] == 10) ? 5.22-0.00504*fermentables_properties[i]['srm'] : fermentables_properties[i]['distilled_water_ph'])
    }

    // Calculate Effective Alkalinity

    // There is this radio button for Bicarbonate versus Alkalinity
    // We can't see how it works in the sheet.

    //ratio = 50/61
    ratio = 1

    if (mash_volume == 0){
        effective_alkalinity = 0
    } else {
        effective_alkalinity = (init_HCO3_or_CaCO3*ratio + 
            (
                (mash_ph_up_chalk_CaCO3*130) +
                (mash_ph_up_baking_soda_NaHCO3*157) -
                (176.1*lactic_acid_percent/100*lactic_acid_ml*2) -
                (4160.4*acidulated_malt_percent/100*acidulated_malt_oz)*2.5 +
                (mash_ph_up_slaked_lime_CaOH2)*357
            )/((mash_volume == 0) ? 1 : mash_volume)
        )
    }

    // Calculate Residual Alkalinity

    if (mash_volume == 0){
        residual_alkalinity = 0
    } else {
        residual_alkalinity = effective_alkalinity - ((mash_Ca/1.4)+(mash_Mg/1.7))
    }


    // Calculate Estimated Room-Temp Mash pH

    if (mash_volume == 0){
        estimated_ph = 0
    } else {

        sum_of_product = 0
        for (var i = 0; i<fermentables_properties.length;i++) {
            sum_of_product = sum_of_product + (fermentables_properties[i]['distilled_water_ph'] * fermentable_weights[i])
        }

        normalize_by_total_grains = sum_of_product / (total_grains == 0 ? 1 : total_grains)


        estimated_ph = normalize_by_total_grains +(0.1085*mash_volume/(total_grains == 0 ? 1 : total_grains)+0.013)*residual_alkalinity/50
    }

    // Calculate Post Sparge Additions

    mash_sparge_Ca = (1 - (mash_volume*mash_distilled_percent+SVPMO*sparge_distilled_percent/(mash_volume+SVPMO)))*init_Ca + 
                     (
                          (mash_ph_up_chalk_CaCO3 + sparge_ph_up_chalk_CaCO3)*105.89 +
                          (mash_ph_down_gypsum_CaSO4+ sparge_ph_down_gypsum_CaSO4)*60 +
                          (mash_ph_down_cal_chl_CaCl2 + sparge_ph_down_cal_chl_CaCl2)*72 +
                          (mash_ph_up_slaked_lime_CaOH2 + sparge_ph_up_slaked_lime_CaOH2)*143
                     )/(mash_volume + SVPMO)
    mash_sparge_Mg = (1 - (mash_volume*mash_distilled_percent+SVPMO*sparge_distilled_percent/(mash_volume+SVPMO)))*init_Mg + 
                     (
                          (mash_ph_down_epsom_salt_MgSO4+sparge_ph_down_epsom_salt_MgSO4)*24.6
                     )/(mash_volume + SVPMO)

    mash_sparge_Na = (1 - (mash_volume*mash_distilled_percent+SVPMO*sparge_distilled_percent/(mash_volume+SVPMO)))*init_Na + 
                     (
                          (mash_ph_up_baking_soda_NaHCO3+sparge_ph_up_baking_soda_NaHCO3)*72.3 

                     )/(mash_volume + SVPMO)

    mash_sparge_Cl = (1 - (mash_volume*mash_distilled_percent+SVPMO*sparge_distilled_percent/(mash_volume+SVPMO)))*init_Cl + 
                     (
                          (mash_ph_down_cal_chl_CaCl2+sparge_ph_down_cal_chl_CaCl2)*127.47

                     )/(mash_volume + SVPMO)
    mash_sparge_SO4 = (1 - (mash_volume*mash_distilled_percent+SVPMO*sparge_distilled_percent/(mash_volume+SVPMO)))*init_SO4 + 
                     (
                          (mash_ph_down_gypsum_CaSO4+sparge_ph_down_gypsum_CaSO4)*147.4 + 
                          (mash_ph_down_epsom_salt_MgSO4+sparge_ph_down_epsom_salt_MgSO4)*103

                     )/(mash_volume + SVPMO)

    // Cl/SO4 ratios
    mash_Cl_SO4 = mash_Cl / mash_SO4
    mash_sparge_Cl_SO4 = mash_sparge_Cl / mash_sparge_SO4


}

function refresh_chemistry(){
    get_chemistry_info()
    calculate_ph_and_resulting_water_profile()

    $("#mash_volume_for_chemistry").text(mash_volume)
    $("#sparge_volume_for_chemistry").text(SVPMO.toFixed(3))

    $("#estimated_ph").text(estimated_ph.toFixed(3))
    $("#effective_alkalinity").text(effective_alkalinity.toFixed(3))
    $("#residual_alkalinity").text(residual_alkalinity.toFixed(3))   

    $("#mash_Ca").text(mash_Ca.toFixed(3))
    $("#mash_Mg").text(mash_Mg.toFixed(3))
    $("#mash_Na").text(mash_Na.toFixed(3))
    $("#mash_Cl").text(mash_Cl.toFixed(3))
    $("#mash_SO4").text(mash_SO4.toFixed(3))

    $("#mash_sparge_Ca").text(mash_sparge_Ca.toFixed(3))
    $("#mash_sparge_Mg").text(mash_sparge_Mg.toFixed(3))
    $("#mash_sparge_Na").text(mash_sparge_Na.toFixed(3))
    $("#mash_sparge_Cl").text(mash_sparge_Cl.toFixed(3))
    $("#mash_sparge_SO4").text(mash_sparge_SO4.toFixed(3))
    
    $("#mash_Cl_SO4").text(mash_Cl_SO4.toFixed(3))
    $("#mash_sparge_Cl_SO4").text(mash_sparge_Cl_SO4.toFixed(3))

}

// Initialize chemistry values
refresh_chemistry()


//// Watch for dependencies

// Things to watchfor chemistry
chemistry_inputs = document.getElementsByClassName('chemistry_inputs')
for (var i=0, max=chemistry_inputs.length; i < max; i++) {

    chemistry_inputs[i].addEventListener("input", function() {
    refresh_chemistry()

    });

}

// Things to watch from fermentables
weightsArray = document.getElementsByClassName('fermentables_weight')
for (var i=0, max=5; i < max; i++) {

    fermentables = document.getElementsByName('ingredient'+String(i+1))
    fermentables[0].addEventListener("input", function() {
    refresh_chemistry()

    });

    weightsArray[i].addEventListener("input", function() {
    refresh_chemistry()

    });

}

// Things to watch from mash
mash_array = document.getElementsByClassName('mash_input')
for (var i=0, max=mash_array.length; i < max; i++) {
    // Do something with the element here
    mash_array[i].addEventListener("input", function() {
    refresh_chemistry()

    });

}

// Things to watch from system
system_array = document.getElementsByClassName('system_input')
for (var i=0, max=system_array.length; i < max; i++) {
    // Do something with the element here
    system_array[i].addEventListener("input", function() {
    refresh_chemistry()

    });

}
