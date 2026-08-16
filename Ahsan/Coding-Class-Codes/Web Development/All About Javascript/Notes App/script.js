const textArea = document.getElementById('textarea')
const addButton = document.getElementById('add_button')
const notesDiv = document.getElementById('notes')

addButton.addEventListener("click",()=>{
    let noteText = textArea.value
    if (noteText.trim() == ""){
        alert("Please write something!!!!")
        return
    }
    let noteDiv = document.createElement('div')
    noteDiv.classList.add('note')
    let noteDetailsDiv = document.createElement('div')
    noteDetailsDiv.classList.add('note-details')
    noteDetailsDiv.innerHTML = noteText
    noteDetailsDiv.style.whiteSpace = "pre-wrap"

    let customizeButtonsDiv = document.createElement('div')
    customizeButtonsDiv.classList.add('customize-buttons')

    let editButton = document.createElement('button')
    editButton.classList.add('edit-button')
    editButton.innerHTML = 'Edit'
    let deleteButton = document.createElement('button')
    deleteButton.innerHTML = 'Delete'
    deleteButton.classList.add('delete-button')

    customizeButtonsDiv.appendChild(editButton)
    customizeButtonsDiv.appendChild(deleteButton)

    noteDiv.appendChild(noteDetailsDiv)
    noteDiv.appendChild(customizeButtonsDiv)

    notesDiv.appendChild(noteDiv)
})