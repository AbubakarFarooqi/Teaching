const citySelect = document.getElementById("cities")
const findWeatherButton = document.getElementById("button")
const cityCountrySpan = document.getElementById("cityName")
const tempCelSpan = document.getElementById("temp_cels_number")
const tempFahSpan = document.getElementById("temp_fahr_number")
const windSpeedSpan = document.getElementById("wind_speed_number")

findWeatherButton.addEventListener('click',async ()=>{
    let city = citySelect.value
    let apiUrl = `https://api.weatherapi.com/v1/current.json?key=0f9f65342419461e869235451260607&q=${city}`

    let response = await fetch(apiUrl) // whenever working with api you have to do await

    if (!response.ok){
        alert("Api failed")
    }

    let data = await response.json()

    let country = data.location.country
    let temp_c = data.current.temp_c
    let temp_f = data.current.temp_f
    let wind_kph = data.current.wind_kph

    cityCountrySpan.innerHTML = `${city}, ${country}`
    tempCelSpan.innerHTML = `${temp_c}`
    tempFahSpan.innerHTML = `${temp_f}`
    windSpeedSpan.innerHTML = `${wind_kph}`
})