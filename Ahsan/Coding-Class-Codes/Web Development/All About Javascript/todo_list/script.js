onPageLoad()
var tasks = []
var current_task_id = 1
const form = document.getElementById("form")

form.addEventListener("submit",function (e){
    e.preventDefault()

    const name = document.getElementById("NameofTask").value
    const description = document.getElementById("DescriptionofTask").value
    const stDate = document.getElementById("StartofTask").value
    const endDate = document.getElementById("EndofTask").value

    const id = getNewId()

    tasks.push (
        {
            "id":id,
            "name":name,
            "description":description,
            "startDate":stDate,
            "endDate":endDate
        }
    )
    localStorage.setItem("tasks",JSON.stringify(tasks))
    addTask(id,name,description,stDate,endDate)
})


function getNewId(){
    newId = current_task_id + 1
    current_task_id = newId
    return newId
}

function onPageLoad(){
    tasks = JSON.parse(localStorage.getItem("tasks"))
    for(const task of tasks){
        addTask(task.name,task.description,task.stDate,task.endDate)
    }
}

function addTask(id,name,description,stDate,endDate){
    console.log("sdffgwgdbhbgh")
    const tr = document.createElement("tr")
    tr.id = id
    tr.innerHTML = `
    <td>${name}</td>
    <td>${description}</td>
    <td>${stDate}</td>
    <td>${endDate}</td>
    <td><button class="update-button">Update</button></td>
    <td><button class="delete-button">Delete</button></td>
    `

    const table = document.getElementById("table")

    table.appendChild(tr)
}