document.getElementById("ai220").addEventListener("click", function(){
    const div = document.getElementById("div_a220");
    const airbusPlane = document.getElementById("a220");
    if (div.style.display === "none" || div.style.display === "") {
        div.style.display = "block";
        const currentheight = parseInt(window.getComputedStyle(airbusPlane).height,10);
        airbusPlane.style.height = (currentheight + 120) + "px";
    } else {
        div.style.display = "none";
        const currentheight = parseInt(window.getComputedStyle(airbusPlane).height,10);
        airbusPlane.style.height = (currentheight - 120) + "px";
    }
    

});