$(function() {
  $('#load').bind('click', 
    function() {
      $.getJSON($SCRIPT_ROOT + '/load', 

                {
                 // Recipe; send in recipe to delete
                 recipe: $('input[name="recipe"]').val(),

                },
                // Upon recieving the data
                function(data) {
                 x = data
                

                }
      );

    return false;
    }
  );
});