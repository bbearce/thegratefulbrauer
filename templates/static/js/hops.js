
function get_hop_info(){
    // Go get the drop down indgredients 
    hops = []
    for (var i = 0; i < 3; i++) {
        hops.push($('select[name="hop'+(i+1).toString()+'"]').val())
    }

    hops_properties = []
    for (i in hops) {//

        var hop = hops[i]

        // iterate over each element in the array
        
        for (var i = 0; i < Data['Constants']['gb_constants_hops'].length; i++){
          // look for the entry with a matching `code` value
          if (Data['Constants']['gb_constants_hops'][i].hops == hop){
             hops_properties.push({hop_name:hop,
                                   alphaAcid:Data['Constants']['gb_constants_hops'][i]['alphaAcid'],
                                   berry:Data['Constants']['gb_constants_hops'][i]['berry'],
                                   citrus:Data['Constants']['gb_constants_hops'][i]['citrus'],
                                   tart:Data['Constants']['gb_constants_hops'][i]['tart'],
                                   flowery:Data['Constants']['gb_constants_hops'][i]['flowery'],
                                   earthy:Data['Constants']['gb_constants_hops'][i]['earthy'],
                                   pine:Data['Constants']['gb_constants_hops'][i]['pine'],
                                   spicy:Data['Constants']['gb_constants_hops'][i]['spicy'],
                                   bitter:Data['Constants']['gb_constants_hops'][i]['bitter']
                                 })

            // obj[i].name is the matched result
          }
        }
    }//
}

function calc_ibu(){

  og = calc_og()

  // retrieve utilization for each hop

  // [1] boil_times first 
  hop_weights = []
  boil_times = []
  utilizations= []
  for (var i = 0; i < 3; i++) {
      boil_times.push(parseInt($('input[name="boil_time_min'+(i+1).toString()+'"]').val()))
      hop_weights.push(parseFloat($('input[name="weight_oz'+(i+1).toString()+'"]').val()))
      
      // Go look for that boil time in utilization_table
      for (var j = 0; j < Data['Constants']['gb_constants_ut'].length; j++){
        // look for the entry with a matching `code` value
        if (Data['Constants']['gb_constants_ut'][j].boil_time == boil_times[i]){
           utilizations.push(Data['Constants']['gb_constants_ut'][j].pellet_hop)

          }
      }



  }

  // [2] Cgravity second

  if (og < 1.050) {Cgravity = 1} else {Cgravity = 1 + (og-1.050)/0.2}

  // [3] Get batch size

  batch_size = parseFloat($('input[name="batch_size"').val()) //Gal

  // [4] Calculate IBUs
  ibus = []
  for (var i = 0; i < 3; i++) {
    
    ibu = ( (hop_weights[i])*(utilizations[i]/100)*(hops_properties[i]['alphaAcid']/100)*7489 ) / ( (batch_size)*(Cgravity) )

    ibus.push(ibu)
  }

  return ibus[0]+ibus[1]+ibus[2]

}

function make_hops_chart() {

    // Remove previous chart
    var elem = document.getElementById("hopsChart");
    elem.remove();
    var elem = document.getElementsByClassName("chartjs-size-monitor");
    if(elem.length != 0){
        elem[0].remove();
    }else{console.log('Note from hops: initial hop chart')}
    

    var canvas = document.createElement('canvas');
    canvas.id = 'hopsChart'
    var div = document.getElementsByClassName("hopsChartDiv")
    div[0].appendChild(canvas)

    // Chart Code
    var ctx = document.getElementById('hopsChart').getContext('2d');
    var myRadarChart = new Chart(ctx, {
    type: 'radar',
    data: {
    labels: ['Berry', 'Citrus', 'Tart', 'Flowery', 'Earthy', 'Pine', 'Spicy', 'Bitter'],
    datasets: [
        {data: [hops_properties[0]['berry'],
                hops_properties[0]['citrus'],
                hops_properties[0]['tart'],
                hops_properties[0]['flowery'],
                hops_properties[0]['earthy'],
                hops_properties[0]['pine'],
                hops_properties[0]['spicy'],
                hops_properties[0]['bitter']],
         label: hops_properties[0]['hop_name'],
         backgroundColor: 'rgba(100, 0, 0, 0.3)'},

        {data: [hops_properties[1]['berry'],
                hops_properties[1]['citrus'],
                hops_properties[1]['tart'],
                hops_properties[1]['flowery'],
                hops_properties[1]['earthy'],
                hops_properties[1]['pine'],
                hops_properties[1]['spicy'],
                hops_properties[1]['bitter']],
         label: hops_properties[1]['hop_name'],
         backgroundColor: 'rgba(0, 100, 0, 0.3)'},

        {data: [hops_properties[2]['berry'],
                hops_properties[2]['citrus'],
                hops_properties[2]['tart'],
                hops_properties[2]['flowery'],
                hops_properties[2]['earthy'],
                hops_properties[2]['pine'],
                hops_properties[2]['spicy'],
                hops_properties[2]['bitter']],
         label: hops_properties[2]['hop_name'],
         backgroundColor: 'rgba(0, 0, 100, .3)'},


    ]
    },
    options: {
    scale: {
        // Hides the scale
        display: true
    }}

    });

}

function refresh_hops() {
  get_hop_info()
  $('#total_ibu').text(calc_ibu().toFixed(3)); //toFixed() is a rounding method 
  $('#ibu1').text(ibus[0])
  $('#alpha_acid1').text(hops_properties[0]['alphaAcid'])
  $('#utilization1').text(utilizations[0])
  $('#Hop1').text($("select[name='hop1']").val())
  $('#ibu2').text(ibus[1])
  $('#alpha_acid2').text(hops_properties[1]['alphaAcid'])
  $('#utilization2').text(utilizations[1])
  $('#Hop2').text($("select[name='hop2']").val())
  $('#ibu3').text(ibus[2])
  $('#alpha_acid3').text(hops_properties[2]['alphaAcid'])
  $('#utilization3').text(utilizations[2])
  $('#Hop3').text($("select[name='hop3']").val())

  make_hops_chart()
}

// Display Chart right off the bat
refresh_hops()

//// Watch hops for dependencies

// Things to watch from hops
for (var i=0, max=3; i < max; i++) {

    Hops = document.getElementsByName('hop'+String(i+1))
    Hops[0].addEventListener("input", function(){
        refresh_hops()
    })

    Weights = document.getElementsByName('weight_oz'+String(i+1))
    Weights[0].addEventListener("input", function(){
        refresh_hops()
    })

    Boil_Times = document.getElementsByName('boil_time_min'+String(i+1))
    Boil_Times[0].addEventListener("input", function(){
        refresh_hops()
    })
}

// Things to watch from fermentables
for (var i=0, max=5; i < max; i++) {

    fermentables = document.getElementsByName('ingredient'+String(i+1))
    fermentables[0].addEventListener("input", function() {
    refresh_hops()

    });

    weightsArray[i].addEventListener("input", function() {
    refresh_hops()

    });


}

// Things to watch from system
system_array = document.getElementsByClassName('system_input')
for (var i=0, max=system_array.length; i < max; i++) {
    // Do something with the element here
    system_array[i].addEventListener("input", function() {
    refresh_hops()

    });

}

