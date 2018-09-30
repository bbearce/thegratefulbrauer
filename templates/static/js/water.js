function get_water_info(){
   
    total_boil_time = parseInt($("input[name='total_boil_time']")[0].value)
    evap_rate = parseFloat($("input[name='evap_rate']")[0].value)
    shrinkage = parseFloat($("input[name='shrinkage']")[0].value)
    
    mash_tun_dead_space = parseFloat($("input[name='mash_tun_dead_space']")[0].value)
    lauter_tun_dead_space = parseFloat($("input[name='lauter_tun_dead_space']")[0].value)
    kettle_dead_space = parseFloat($("input[name='kettle_dead_space']")[0].value)
    fermentation_tank_loss = parseFloat($("input[name='fermentation_tank_loss']")[0].value)
    grain_abs_factor = parseFloat($("input[name='grain_abs_factor']")[0].value)

    // From System
    batch_size = parseFloat($('input[name="batch_size"').val()) //Gal

    get_mash_info()
    // We have these variables after calling get_mash_info
    // total_grains = calc_percent_of_total()
    // mash_volume = total*(mash_thickness/4) // Convert to [Gal] for mash_thickness
    // infusion_temp = (0.2/mash_thickness)*(sacc_rest_temp-init_grain_temp)+sacc_rest_temp
    // mash_out_volume = ( (170 - sacc_rest_temp)*(0.2*total_grains+mash_volume) ) / (212 - 170)

    // [1] Pre-Boil Volume

    PBV = ( (batch_size + kettle_dead_space + fermentation_tank_loss)/(1 - shrinkage/100) ) / 
          (1 - ((evap_rate/100)*(total_boil_time/60)))

    // [2] Volume From Runnings

    EL = mash_tun_dead_space + lauter_tun_dead_space // Equipment Loss

    VFR = mash_volume - (total_grains*grain_abs_factor) - EL

    // [3] Sparge Volume

    SV = PBV - VFR

    // [4] Sparge Volume Post Mash Out

    SVPMO = SV - mash_out_volume

    // [5] Total Water Needed

    TW = PBV + (total_grains*grain_abs_factor) + EL


}

function make_water_chart (){

    // Remove previous chart
    var elem = document.getElementById("waterChart");
    elem.remove();
    var elem = document.getElementsByClassName("chartjs-size-monitor");
    if(elem.length != 0){
        elem[0].remove();
    }else{console.log('Note from water: initial water chart')}

    var canvas = document.createElement('canvas');
    canvas.id = 'waterChart'
    var div = document.getElementsByClassName("waterChartDiv")
    div[0].appendChild(canvas)

    var ctx = document.getElementById("waterChart")
    var myWaterChart = new Chart(ctx,{
      "type":"doughnut",
      "data":{"labels":["Mash Vol","Sparge Vol","Mash Out Vol"],
              "datasets":[{"label":"My First Dataset","data":[mash_volume,SV,mash_out_volume],
                           "backgroundColor":["rgb(255, 99, 132)",
                                              "rgb(54, 162, 235)",
                                              "rgb(255, 205, 86)"]}]
             }
    });


}



function refresh_water(){
    
    get_water_info()

    $("#mash_volume_water_duplicate").text(mash_volume)
    $("#mash_out_vol_duplicate").text(mash_out_volume)
    $("#sparge_vol").text(SVPMO)

    make_water_chart()

}


// Initialize water values
refresh_water()

//// Watch for dependencies

// Things to watch from water
water_array = document.getElementsByClassName('water_input')
for (var i=0, max=water_array.length; i < max; i++) {
    // Do something with the element here
    water_array[i].addEventListener("input", function() {
    refresh_water()

    });

}

// Things to watch from fermentables
weightsArray = document.getElementsByClassName('fermentables_weight')
for (var i=0, max=5; i < max; i++) {

    fermentables = document.getElementsByName('ingredient'+String(i+1))
    fermentables[0].addEventListener("input", function() {
    refresh_water()

    });

    weightsArray[i].addEventListener("input", function() {
    refresh_water()

    });

}

// Things to watch from mash
mash_array = document.getElementsByClassName('mash_input')
for (var i=0, max=mash_array.length; i < max; i++) {
    // Do something with the element here
    mash_array[i].addEventListener("input", function() {
    refresh_water()

    });

}

// Things to watch from system
system_array = document.getElementsByClassName('system_input')
for (var i=0, max=system_array.length; i < max; i++) {
    // Do something with the element here
    system_array[i].addEventListener("input", function() {
    refresh_water()

    });

}




