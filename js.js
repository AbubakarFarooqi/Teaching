var w = 'succuss'

function suc(){
    console.log('over here you can see the code')
}


function nav() {
    document.getElementById('sim').addEventListener('click', function() {
        window.open('https://geo-fs.com', '_blank'); // opens in a new tab
    });

    document.getElementById('map').addEventListener('click', function(){
        window.open('https://www.google.com/maps/place/George+Bush+Intercontinental+Airport/@29.9865406,-95.3519559,15z/data=!3m1!4b1!4m6!3m5!1s0x8640b423d94355c7:0x9cc6b4fcc8c0c231!8m2!3d29.9931058!4d-95.3416255!16zL20vMDEzNnN0?entry=ttu&g_ep=EgoyMDI1MDgxMy4wIKXMDSoASAFQAw%3D%3D')
    });

    document.getElementById('radar').addEventListener('click', function(){
        window.open('https://www.airnavradar.com/@38.90743,39.79755,z4?rightSidebar=flightFeed')
    });
}

function test(){
    console.log(w)
}

// Call the function so it runs
nav();
test();