$(document).ready(function() {
    initMap();
});

var map; // define a map as a global variable for use of different functions 
var directionsDisplay;
var directionsService = new google.maps.DirectionsService();

function initMap() {
//	Function to pull in the map. 
	map = new google.maps.Map(document.getElementById('map'), {
        center: new google.maps.LatLng(53.3498053, -6.260309699999993),
        zoom: 12,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    }); //closing map creation 
	
//	  Add traffic layer to the map.
	  var trafficLayer = new google.maps.TrafficLayer();
	  trafficLayer.setMap(map);
	  
//	  Add Public transit layer to the map. 
	  var transitLayer = new google.maps.TransitLayer();
	  transitLayer.setMap(map);

//	Function to pull in the json from the url. 
    $.getJSON("http://127.0.0.1:8000/dublinbuspredict/sampleQuery", null, function(d) {
        console.log(d.data[0])
        var data = d.data;  
        var points = new Array;
        var marker, i;
        var infowindow = new google.maps.InfoWindow();
        var bounds = new google.maps.LatLngBounds();
        for (i = 0; i < data.length; i++) {  
                var myLatLng = new google.maps.LatLng(data[i][3], data[i][4])
                marker = new google.maps.Marker({
                position: new google.maps.LatLng(data[i][3], data[i][4]),
                map: map
            });
         points.push(marker.getPosition());
         bounds.extend(marker.position);
             
        google.maps.event.addListener(marker, 'click', (function(marker, i){
        	return function() {
        		infowindow.setContent(data[i][1] + "<br>" + data[i][2]);
        		infowindow.open(map,marker);
        	}
        })(marker, i));
        }
        
      //Initialize the Path Array
      var path = new google.maps.MVCArray();
    
      //Initialize the Direction Service
      var service = new google.maps.DirectionsService();

      //Set the Path Stroke Color
      var poly = new google.maps.Polyline({ map: map, strokeColor: '#4986E7' });
      
      //Loop and Draw Path Route between the Points on MAP
      for (var i = 0; i < points.length; i++) {
          if ((i + 1) < points.length) {
              var src = points[i];
              var des = points[i + 1];
              path.push(src);
              poly.setPath(path);
              service.route({
                  origin: src,
                  destination: des,
                  travelMode: google.maps.DirectionsTravelMode.TRANSIT
              })
          }
          }
    });

}

function loadFirstMenu(){
$.getJSON("http://127.0.0.1:8000/dublinbuspredict/pilotRoutes", {"route":route}, function(d) {
        console.log(d)
        document.getElementById("dropdown-list-2").innerHTML = "";
        document.getElementById("search-box-2").value = "";
        document.getElementById("search-box-3").value = "";
    $.each(d['stops'], function(i, p) {
        $('#dropdown-list-2').append($('<li></li>').val(p).html('<a onclick=getStopsDest(' + p + ')>' + route + ' - ' + p + '</a>'));
    });
}
