const nameInput = document.getElementById('name')
const nameValidationSpan = document.getElementById('name_validation')
const passwordInput = document.getElementById('password')
const passwordValidationSpan = document.getElementById('password_validation')
const emailInput = document.getElementById('email')
const emailValidationSpan = document.getElementById('email_validation')
const regex =  /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{3,}$/
const submitButton = document.getElementById('button')


let isNameValid = false
let isPasswordValid = false
let isEmailValid = false


submitButton.disabled = true

function updateButton(){
  if (isEmailValid && isPasswordValid && isEmailValid){
    submitButton.disabled = false
    submitButton.style
  }
  else{
    submitButton.disabled = true

  }
}


function nameValidator(str){
    if (str.length === 0) {
        isNameValid = false
        nameValidationSpan.innerHTML = "Name cannot be empty"
        updateButton()
        return
    }

    for (var i = 0; i < str.length; i++) {
        var code = str.charCodeAt(i);

        if (!(code >= 65 && code <= 90) && !(code >= 97 && code <= 122)) {
            isNameValid = false
            nameValidationSpan.innerHTML = "Name can only contain alphabets" ;
            updateButton()
            return
        }
    }
    isNameValid = true
    updateButton()
    nameValidationSpan.innerHTML = ""
}

nameInput.addEventListener('input', function (){
    nameValidator(nameInput.value)
})

function passwordValidator(str){
    if (str.length === 0) {
        isPasswordValid = false
        passwordValidationSpan.innerHTML = "Password cannot be empty"
        updateButton()
        return
    }

    if (str.length < 8) {
        isPasswordValid = false
        passwordValidationSpan.innerHTML = "Password is too short (8 characters minimum)"
        updateButton()
        return
    }
    isPasswordValid = true
    updateButton()
    passwordValidationSpan.innerHTML = ""
}

passwordInput.addEventListener('input', function (){
    passwordValidator(passwordInput.value)
})

function emailValidator(str){
    if (str.length === 0) {
        isEmailValid = false
        emailValidationSpan.innerHTML = "Email cannot be empty"
        updateButton()
        return
    }

    if (!regex.test(str)) {
        isEmailValid = false
        emailValidationSpan.innerHTML = "Enter a valid email"
        updateButton()
        return
    }
    isEmailValid = true
    updateButton()
    emailValidationSpan.innerHTML = ""
}

emailInput.addEventListener('input', function (){
    emailValidator(emailInput.value)
})


