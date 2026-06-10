// const searchBarInput = document.getElementById("searchBarInput")

// searchBarInput.addEventListener("focus",function (){
//     const searchBarMagGlassFirst = document.getElementById("searchBarMagGlassFirst")
//         searchBarMagGlassFirst.style.display = "flex"
// })


// searchBarInput.addEventListener("blur",function (){
//     const searchBarMagGlassFirst = document.getElementById("searchBarMagGlassFirst")
//         searchBarMagGlassFirst.style.display = "none"
// })


// TOPICS SCROLL

const topicsParent = document.getElementById("topicsParent")
const rightBtn = document.getElementById("rightTopicButton")

const amountOfScroll = 200

rightBtn.addEventListener('click',function () {
  console.log("It's clicked")
    topicsParent.scrollBy({left:amountOfScroll,behavior:"smooth"})
});

