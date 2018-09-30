function get_yeast_info(){
   
   
    yeast_name = $("select[name='yeast_name']")[0].value
    init_cells = $("input[name='init_cells']")[0].value
    
    // iterate over all yeast and find user chosen yeast
    yeast_properties = []   
    for (var i = 0; i < Data['Constants']['gb_constants_yeast'].length; i++){
      // look for the entry with a matching `code` value
      if (Data['Constants']['gb_constants_yeast'][i].yeastStrain == yeast_name){
         yeast_properties = Data['Constants']['gb_constants_yeast'][i]
        // obj[i].name is the matched result
      }
    }

}

function calculate_yeast_output(){

    // Retrieve needed inputs
    OG = parseFloat($('#OG').text())
    attenuation = yeast_properties.attenuation
    // From System
    batch_size = parseFloat($('input[name="batch_size"').val()) //Gal
    liter_batch_size = batch_size*3.785 // batch_size*[liters/gallon]

    // Final Gravity
    FG = OG - (attenuation/100)*(OG - 1)

    // Alcohol By Volume
    ABV = (1.05/0.79)*((OG-FG)/FG)*100

    // Degree Plato calculation
    degree_plato = (OG - 1)*1000 / 4 


    // Recommended Cell Count calculation

    RCC = (1.16*10**9 * degree_plato * liter_batch_size) // [billions]

}

function make_yeast_chart() {

    // Remove previous chart
    var elem = document.getElementById("yeastChart");
    elem.remove();
    var elem = document.getElementsByClassName("chartjs-size-monitor");
    if(elem.length != 0){
        elem[0].remove();
    }else{console.log('Note from yeast: initial yeast chart')}

    var canvas = document.createElement('canvas');
    canvas.id = 'yeastChart'
    var div = document.getElementsByClassName("yeastChartDiv")
    div[0].appendChild(canvas)

    var ctx = document.getElementById('yeastChart').getContext('2d');
    var myBarChart = new Chart(ctx,{
        "type":"bar",
        "data":{"labels":["Predicted","Low","High","Barley Wine High"],
        "datasets":[{
            "label":"ABV",
            "data":[ABV,3,10,17],
            "fill":false,
            "backgroundColor":["rgba(255, 159, 64, 0.5)","rgba(201, 203, 207, 0.2)","rgba(201, 203, 207, 0.2)","rgba(201, 203, 207, 0.2)"],
            "borderColor":["rgb(255, 159, 64)","rgb(201, 203, 207)","rgb(201, 203, 207)","rgba(201, 203, 207)"],
            "borderWidth":1}]
         },
        "options":{"scales":{"yAxes":[{"ticks":{"beginAtZero":true}}]}}});

}

function refresh_yeast() {

    get_yeast_info()
    calculate_yeast_output()

    $('#abv').text(ABV)
    $('#OG').text(OG)
    $('#fg').text(FG)

    $('#Yeast').text(yeast_name)
    $('#Attenuation').text(yeast_properties.attenuation)
    $('#Pitch_Rate_Recommended').text(RCC/10**9)

    make_yeast_chart()

}

// Display Yeast calculations right away
refresh_yeast()

// Things to watch from yeast
$("select[name='yeast_name']")[0].addEventListener("input", function(){
    refresh_yeast()
})



// Things to watch from fermentables
for (var i=0, max=5; i < max; i++) {

    fermentables = document.getElementsByName('ingredient'+String(i+1))
    fermentables[0].addEventListener("input", function() {
    refresh_yeast()

    });

    weightsArray[i].addEventListener("input", function() {
    refresh_yeast()

    });


}

// Things to watch from system
system_array = document.getElementsByClassName('system_input')
for (var i=0, max=system_array.length; i < max; i++) {
    // Do something with the element here
    system_array[i].addEventListener("input", function() {
    refresh_yeast()

    });

}


