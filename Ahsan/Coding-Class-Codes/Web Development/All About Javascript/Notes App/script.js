const textArea = document.getElementById('textarea')
const addButton = document.getElementById('add_button')
const notesDiv = document.getElementById('notes')

addButton.addEventListener("click",()=>{
    let noteText = textArea.value
    if (noteText.trim() == ""){
        alert("Please write something!!!!")
        return
    }
})