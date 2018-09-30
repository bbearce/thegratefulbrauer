function get_fermentation_info(){
    days1 = parseInt($("input[name='days1']")[0].value)
    days2 = parseInt($("input[name='days2']")[0].value)
    days3 = parseInt($("input[name='days3']")[0].value)
    days4 = parseInt($("input[name='days4']")[0].value)
    days5 = parseInt($("input[name='days5']")[0].value)

    temp1 = parseInt($("input[name='temp1']")[0].value)    
    temp2 = parseInt($("input[name='temp2']")[0].value)    
    temp3 = parseInt($("input[name='temp3']")[0].value)    
    temp4 = parseInt($("input[name='temp4']")[0].value)    
    temp5 = parseInt($("input[name='temp5']")[0].value)    


}

function make_fermentation_graph() {
    
    // Remove previous chart
    var elem = document.getElementById("fermentationChart");
    elem.remove();
    var elem = document.getElementsByClassName("chartjs-size-monitor");
    if(elem.length != 0){
        elem[0].remove();
    }else{console.log('Note from fermentation: initial fermentation chart')}

    var canvas = document.createElement('canvas');
    canvas.id = 'fermentationChart'
    var div = document.getElementsByClassName("fermentationChartDiv")
    div[0].appendChild(canvas)

    // Mash scatter line data
    time1 = days1; temp1 = temp1;
    time2 = days2; temp2 = temp2;
    time3 = days3; temp3 = temp3;
    time4 = days4; temp4 = temp4;
    time5 = days5; temp5 = temp5;

    total_time = time1+time2+time3+time4+time5

    fermentation_data = []
    for (i = 0; i <= total_time; i=i+1) {
        if (i <= time1){
            temp = temp1
        }else if(i <= time1+time2){
            temp = temp2
        }else if(i <= time1+time2+time3){
            temp = temp3
        }else if(i <= time1+time2+time3+time4){
            temp = temp4
        }else if(i <= time1+time2+time3+time4+time5){
            temp = temp5
        }
        fermentation_data.push({x:i,y:temp})
    }

    var ctx = document.getElementById('fermentationChart').getContext('2d');
    var scatterChart = new Chart(ctx, {type: 'scatter', 
       data: {
          datasets: [
             {
             label: "Fermentation Schedule",
             borderColor:'rgba(200,200,200,1)',
             backgroundColor:'rgba(200,200,200,0.5)',
             data: fermentation_data
             }
          ]
       },
       options: {
          responsive: true
       }

    });

}

function refresh_fermentation() {
    get_fermentation_info()
    make_fermentation_graph()

}

// Display Fermentation calculations right away
refresh_fermentation()

// Things to watch from fermentation
fermentation_array = document.getElementsByClassName('fermentation_input')
for (var i=0, max=fermentation_array.length; i < max; i++) {
    // Do something with the element here
    fermentation_array[i].addEventListener("input", function() {
    refresh_fermentation()

    });

}


