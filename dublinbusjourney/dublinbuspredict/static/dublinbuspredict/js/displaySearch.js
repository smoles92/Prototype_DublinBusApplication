 $(document).ready(function() {
    initMap();
});

var map; // define a map as a global variable for use of different functions 

function initMap() {
	map = new google.maps.Map(document.getElementById('map'), {
        center: new google.maps.LatLng(53.3498053, -6.260309699999993),
        zoom: 12,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    }); //closing map creation 
	

    $.getJSON("http://127.0.0.1:8000/dublinbuspredict/sampleQuery", null, function(d) {
        var data = d.data;   
        var points = new Array();
        var marker, i;
        
        for (i = 0; i < data.length; i++) {  
            marker = new google.maps.Marker({
                position: new google.maps.LatLng(data[i][3], data[i][4]),
                map: map
            });
        }
    })

}
