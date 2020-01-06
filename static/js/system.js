
// Change photo
var change_style_image = function(){

    var current_style = $('select[name="style"]').val()
    document.getElementById('style-img').src = "../static/img/beer_style_photos/" + current_style + '.jpg'
    console.log("../static/img/beer_style_photos/" + current_style)

}


// Initial run of function when page loads
change_style_image()


// Grab currently selected style
$('select[name="style"]')[0].addEventListener("change", function() {
    
    change_style_image()    

});





