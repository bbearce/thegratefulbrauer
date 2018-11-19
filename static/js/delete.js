$(function() {
  $('#delete').bind('click', 
    function() {
      $.getJSON($SCRIPT_ROOT + '/delete', 

                {
                 // Recipe; send in recipe to delete
                 recipe: $('select[id="recipe_delete"]').val()

                 //OLD
                 //recipe: $('input[name="recipe"]').val(),

                },
                // Upon recieving the data
                function(data) {

                if (data['recipe'] == "that recipe does not exist") {
                    $("#messages").text("That recipe doesn't exist")
                } else { 
                  Recipes = data['Recipes']
                  var recipe_load_select_input = document.getElementById("recipe_load");
                  var recipe_delete_select_input = document.getElementById("recipe_delete");

                  option_count = recipe_load_select_input.length
                  //Clear all current selections
                  for (i = 0; i < option_count; i++) {
                      recipe_load_select_input.options[0].remove()
                      recipe_delete_select_input.options[0].remove()
                  }
                  //Add all recipes that are currently in database after adding the new one
                  for (i = 0; i < Recipes.length; i++) {
                      var recipe = document.createElement("option");
                      recipe.text = Recipes[i];
                      recipe_delete_select_input.options.add(recipe, 0)   
                      //Weird thing where I have to create the recipe option again or 
                      //the code only works for the second select
                      var recipe = document.createElement("option");
                      recipe.text = Recipes[i];  
                      recipe_load_select_input.options.add(recipe, 0)
                  } 
                  //Send User Message
                  alert("You just deleted "+data['recipe'])
                }

                
                }
      );

    return false;
    }
  );
});