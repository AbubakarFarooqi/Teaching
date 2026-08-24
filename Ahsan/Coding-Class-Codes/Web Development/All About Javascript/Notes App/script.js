const textArea = document.getElementById("textarea")
const addButton = document.getElementById("add_button")
const notes = document.getElementById("notes")
const body = document.getElementById("body")

let allNotes = []
let notesIds = 1



function OnPageLoad(){
    const arr = localStorage.getItem('notes');
    if (arr){
        allNotes = JSON.parse(arr)
    }

    for (i=0; i<allNotes.length; i++ ){
        DisplayNote(allNotes[i])
    }
}

function DisplayNote(notesText){
    let noteDiv = document.createElement("div")
    noteDiv.classList.add("note")

    noteDiv.setAttribute("id", notesIds)
    notesIds++

    let noteDetailsDiv = document.createElement("div")
    noteDetailsDiv.classList.add("note-details")
    noteDetailsDiv.innerHTML = notesText
    noteDetailsDiv.style.whiteSpace = "pre-wrap"

    let customizeButtonsDiv = document.createElement("div")
    customizeButtonsDiv.classList.add("customize-buttons")

    let editButton = document.createElement("button")
    editButton.classList.add("edit-button")
    editButton.innerHTML = "Edit"

    editButton.addEventListener("click", () => {

        let modalDialog = document.createElement("dialog")
        modalDialog.classList.add("modal")

        let editNote = document.createElement("textarea")
        editNote.classList.add("edit-note")
        editNote.setAttribute("placeholder", "Type your note here")

        let saveButtonDiv = document.createElement("div")
        saveButtonDiv.classList.add("save-button-div")

        let saveButton = document.createElement("button")
        saveButton.classList.add("save-button")
        saveButton.innerHTML = "Save"

        saveButton.addEventListener("click", () => {

            noteDetailsDiv.innerHTML = editNote.value
            noteDetailsDiv.style.whiteSpace = "pre-wrap"

            modalDialog.style.display = "none"
            modalDialog.close()
            idx =  allNotes.findIndex(n => n == notesText)
            if (idx != -1){
                allNotes[idx] = editNote.value
            }
            localStorage.setItem("notes", JSON.stringify(allNotes))

        })

        modalDialog.appendChild(editNote)
        modalDialog.appendChild(saveButtonDiv)
        saveButtonDiv.appendChild(saveButton)

        body.appendChild(modalDialog)

        modalDialog.style.display = "flex"
        modalDialog.showModal()

        

    })

    let deleteButton = document.createElement("button")
    deleteButton.classList.add("delete-button")
    deleteButton.innerHTML = "Delete"

    deleteButton.addEventListener("click", () => {
        noteDiv.remove()
        allNotes = allNotes.filter(n => n !== noteDetailsDiv.innerHTML)
        localStorage.setItem("notes", JSON.stringify(allNotes))

    })

    customizeButtonsDiv.appendChild(editButton)
    customizeButtonsDiv.appendChild(deleteButton)

    noteDiv.appendChild(noteDetailsDiv)
    noteDiv.appendChild(customizeButtonsDiv)

    notes.appendChild(noteDiv)
}


addButton.addEventListener("click", () => {

    let notesText = textArea.value

    if (notesText.trim() == "") {
        alert("Write something to add a note.")
        return
    }

    // Add the actual note text to the array
    allNotes.push(notesText)

    DisplayNote(notesText)

    // Save notes to localStorage
    localStorage.setItem("notes", JSON.stringify(allNotes))

    

    textArea.value = ""
})

OnPageLoad()