$(function() {
  $('#delete').bind('click', 
    function() {
      $.getJSON($SCRIPT_ROOT + '/delete', 

                {
                 // Recipe; send in recipe to delete
                 recipe: $('input[name="recipe"]').val(),

                },
                // Upon recieving the data
                function(data) {

                if (data['recipe'] == "that recipe does not exist") {
                    $("#messages").text("That recipe doesn't exist")
                } else { 
                    $("#messages").text("You deleted "+data['recipe'])
                }

                
                }
      );

    return false;
    }
  );
});