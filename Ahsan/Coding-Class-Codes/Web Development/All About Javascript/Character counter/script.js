const modal = document.getElementById("modal")
const remSpan = document.getElementById("rem")
const totalSpan = document.getElementById("total")
const input = document.getElementById("input")

const limit = 20

input.setAttribute("maxLength",limit)

input.addEventListener('input',function(){
    let length = input.value.length 
    let remaining = limit - length

    remSpan.innerHTML = `Remaining Limit: ${remaining} Characters`
    totalSpan.innerHTML = `Current Characters: ${length} Characters`
})