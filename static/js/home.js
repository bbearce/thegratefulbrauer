// function convert_md_to_html(){
//     console.log('ran convert_md_to_html()')
//     // Get markdown to convert
//     var notes = document.getElementById('notes').value

//     var converter = new showdown.Converter({'tables':true}); // local option for enabling tables in MD.
//     var html = converter.makeHtml(notes);
    
//     var output_html = document.getElementById('output-html')
//     output_html.innerHTML = html

//     // Adjust what is shown
//     if (document.getElementById('notes').style.display === 'none') {
//         document.getElementById('notes').style.display = 'block'
//         document.getElementById('output-html').style.display = 'none'

//     } else {
//         document.getElementById('notes').style.display = 'none'
//         document.getElementById('output-html').style.display = 'block'
        
//     }
// }

// function toggle_image_upload() {

//     var upload_image_position = document.getElementsByClassName('fl-fl')[0]

//     if (upload_image_position.style.right === '100px') {
//         upload_image_position.style.right = "-7000px"
//     } else {
//         upload_image_position.style.right = "100px"
//     }
        
// }



