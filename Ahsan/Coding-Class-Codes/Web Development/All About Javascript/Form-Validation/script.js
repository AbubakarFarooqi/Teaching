const nameInput = document.getElementById('name')
const nameValidationSpan = document.getElementById('name_validation')

function nameValidator(str){
    if (str.length === 0) {
    nameValidationSpan.innerHTML = "Name cannot be empty" ;
    return
  }

  for (var i = 0; i < str.length; i++) {
    var code = str.charCodeAt(i);
    
    // Check if code is NOT in A-Z and NOT in a-z
    if (!(code >= 65 && code <= 90) && !(code >= 97 && code <= 122)) {
      nameValidationSpan.innerHTML = "Name can only contain alphabets" ; 
      return
    }
  }

  nameValidationSpan.innerHTML = ''
}

nameInput.addEventListener('input',function (){
  nameValidator(nameInput.value)
})