let is24HourMode = true
const hoursSpan = document.getElementById("hours")
const minutesSpan = document.getElementById("minutes")
const secondsSpan = document.getElementById("seconds")


document.getElementById("toggle_btn").addEventListener('click',function (){
    is24HourMode = !is24HourMode
    console.log(is24HourMode)
})

function updateClock(){
    const currentTime = new Date() 
    let hours = currentTime.getHours()
    let minutes = currentTime.getMinutes()
    let seconds = currentTime.getSeconds()

    if (is24HourMode == true){
        hoursSpan.textContent = hours
        minutesSpan.textContent = minutes
        secondsSpan.textContent = seconds
    }
    else{
        hours = hours % 12
        hoursSpan.textContent = hours
        minutesSpan.textContent = minutes
        secondsSpan.textContent = seconds
    }
}

updateClock()
setInterval(updateClock,1000)