const search = document.getElementById("search")
const searchBtn = document.getElementById("searchBtn")
const searchedMoviesDiv = document.getElementById("searched_movies")

search.addEventListener("keydown",async (event)=>{
    if (event.key == "Enter"){
        await searchMovie()
    }
})
searchBtn.addEventListener('click', searchMovie)


async function searchMovie(){
    let apiURL = `https://www.omdbapi.com/?apikey=c550fb3a&s=${search.value}&type=movie`
    let response = await fetch(apiURL)

    if (!response.ok){
        alert("API Failed")
    }

    let data = await response.json()
    if (data.Response == 'False'){
        alert("Movie Not Found")
    }
    // const total = parseInt(data.totalResults)

    // console.log(total)

    for (let i=0; i<data.Search.length;i++){
        const movieInfoDiv = document.createElement('div')
        movieInfoDiv.classList.add('movie-info')
        const imgTag = document.createElement('img')
        let img = data.Search[i].Poster
        imgTag.setAttribute("src",img)
        const movieDetailsDiv = document.createElement('div')
        movieDetailsDiv.classList.add('movie-details')
        const titleSpan = document.createElement('span')
        const releaseDateSpan = document.createElement('span')
        titleSpan.classList.add('movie-info-span')
        releaseDateSpan.classList.add('movie-info-span')

        let title = data.Search[i].Title
        let release = data.Search[i].Year

        titleSpan.innerHTML = `Title: ${title}`
        releaseDateSpan.innerHTML = `Release Date: ${release}`

        movieInfoDiv.appendChild(imgTag)
        movieInfoDiv.appendChild(movieDetailsDiv)

        movieDetailsDiv.appendChild(titleSpan)
        movieDetailsDiv.appendChild(releaseDateSpan)

        searchedMoviesDiv.appendChild(movieInfoDiv)



    }

    
    
}