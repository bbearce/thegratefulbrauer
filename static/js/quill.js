var quill = new Quill('#editor-container', {
    modules: {
      toolbar: [
        ['bold', 'italic'],
        ['link', 'blockquote', 'code-block', 'image'],
        [{ list: 'ordered' }, { list: 'bullet' }]
      ]
    },
    placeholder: 'Compose an epic...',
    theme: 'snow'
  });
  
var form = document.querySelector('form');

form.onsubmit = function() {
  // Populate hidden form on submit
  var about = document.querySelector('input[name=about]');
  about.value = JSON.stringify(quill.getContents());
  
  // To set the contents
  // quill.setContents([{"insert":"Testing new content!\n"}])

  // What we want to save
  // var saved_string = JSON.stringify(quill.getContents()['ops'])

  // To load
  // var loaded_string = JSON.parse(saved_string)
  // quill.setContents(loaded_string)

  console.log("Submitted", $(form).serialize());

  console.log("\n\n\n");

  console.log("Submitted", $(form).serializeArray());
  
  // No back end to actually submit to!
  alert('Open the console to see the submit data!')
  return false;
};
