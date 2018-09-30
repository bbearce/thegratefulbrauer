function get_mash_info(){
   
    init_grain_temp = parseInt($("input[name='init_grain_temp']")[0].value)
    sacc_rest_temp = parseInt($("input[name='sacc_rest_temp']")[0].value)
    mash_duration = parseInt($("input[name='mash_duration']")[0].value)
    mash_thickness = parseFloat($("input[name='mash_thickness']")[0].value)

    total_grains = calc_percent_of_total()

    mash_volume = total_grains*(mash_thickness/4) // Convert to [Gal] for mash_thickness

    infusion_temp = (0.2/mash_thickness)*(sacc_rest_temp-init_grain_temp)+sacc_rest_temp


    // Mash Out Volume
    mash_protein_rest_temp = 168
    mash_volume_qts = mash_volume*4
    mash_out_volume = ((0.2*total_grains)+(mash_volume_qts))*(((mash_protein_rest_temp-sacc_rest_temp)/(210-mash_protein_rest_temp))/4)

}

function make_mash_chart() {

    // Remove previous chart
    var elem = document.getElementById("mashChart");
    elem.remove();
    var elem = document.getElementsByClassName("chartjs-size-monitor");
    if(elem.length != 0){
        elem[0].remove();
    }else{console.log('Note from mash: initial mash chart')}

    var canvas = document.createElement('canvas');
    canvas.id = 'mashChart'
    var div = document.getElementsByClassName("mashChartDiv")
    div[0].appendChild(canvas)


    // Mash scatter line data
    grain_temp = init_grain_temp; grain_temp_duration = 5
    sacc_rest = sacc_rest_temp; sacc_rest_duration = mash_duration
    mash_out = mash_protein_rest_temp; mash_out_duration = 30
    boil_temp = 212; boil_temp_duration = parseInt($("input[name='total_boil_time']")[0].value)

    total_time = grain_temp_duration + sacc_rest_duration + mash_out_duration + boil_temp_duration

    mash_data = []
    for (i = 0; i <= total_time; i=i+1) {
        if(i <= grain_temp_duration){//pre-mash in
            temp = grain_temp
        }else if(i <= grain_temp_duration + sacc_rest_duration){
            temp = sacc_rest
        }else if(i <=  grain_temp_duration + sacc_rest_duration + mash_out_duration){
            temp = mash_out  
        }else if(i <= grain_temp_duration + sacc_rest_duration + mash_out_duration + boil_temp_duration){
            temp = boil_temp
        }
        mash_data.push({x:i, y:temp})
    }
    mash_data.push({x:grain_temp_duration+0.5,y:(grain_temp+sacc_rest)/2})
    mash_data.push({x:grain_temp_duration+sacc_rest_duration+0.5,y:(sacc_rest+mash_out)/2})
    mash_data.push({x:grain_temp_duration+sacc_rest_duration+mash_out_duration+0.5,y:(mash_out+boil_temp)/2})

    // Mash In Infusion
    infusion_temp = infusion_temp; infusion_temp_duration = 5
    infusion_data = []
    for (i = 0; i <= infusion_temp_duration; i=i+1) {
        infusion_data.push({x:i, y:infusion_temp})
    }
    infusion_data.push({x:infusion_temp_duration+0.5,y:(infusion_temp+sacc_rest)/2})//

    // Mash Out Infusion
    mash_out_infusion_temp = 212; mash_out_infusion_temp_duration = 5
    mash_out_infusion_data = []
    for (i = 0; i <= infusion_temp_duration; i=i+1) {
        mash_out_infusion_data.push({x:i+sacc_rest_duration, y:mash_out_infusion_temp})
    }
    mash_out_infusion_data.push({x:infusion_temp_duration+sacc_rest_duration+0.5, y:(mash_out_infusion_temp+mash_out)/2})


    var ctx = document.getElementById('mashChart').getContext('2d');
    var scatterChart = new Chart(ctx, {type: 'scatter', 
       data: {
          datasets: [
             {
             label: "Mash Temp",
             borderColor:'rgba(200,200,200,1)',
             backgroundColor:'rgba(200,200,200,0.5)',
             data: mash_data
             },
            {
             label: "Infusion Temp",
             borderColor:'rgba(100,100,250,1)',
             backgroundColor:'rgba(100,100,250,0.5)',
             data: infusion_data
             },
            {
             label: "Mash Out Infusion Temp",
             borderColor:'rgba(250,100,100,1)',
             backgroundColor:'rgba(250,100,100,0.5)',
             data: mash_out_infusion_data
             }
          ]
       },
       options: {
          responsive: true
       }

    });


}

function refresh_mash(){
    
    get_mash_info()

    $("#mash_volume").text(mash_volume)
    $("#infusion_temp").text(infusion_temp)
    $("#mash_out_vol").text(mash_out_volume)

    make_mash_chart()
}

// Initialize mash values
refresh_mash()

//// Watch for dependencies

// Things to watch from mash
mash_array = document.getElementsByClassName('mash_input')
for (var i=0, max=mash_array.length; i < max; i++) {
    // Do something with the element here
    mash_array[i].addEventListener("input", function() {
    refresh_mash()

    });

}

// Things to watch from fermentables
weightsArray = document.getElementsByClassName('fermentables_weight')
for (var i=0, max=5; i < max; i++) {

    fermentables = document.getElementsByName('ingredient'+String(i+1))
    fermentables[0].addEventListener("input", function() {
    refresh_mash()

    });

    weightsArray[i].addEventListener("input", function() {
    refresh_mash()

    });

}
