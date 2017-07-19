//
//$(document).ready(function() {
//    initMap();
//});
//
//var map; // define a map as a global variable for use of different functions
//var directionsDisplay;
//var directionsService = new google.maps.DirectionsService();
//
//function initMap() {
////	Function to pull in the map.
//	map = new google.maps.Map(document.getElementById('map'), {
//        center: new google.maps.LatLng(53.3498053, -6.260309699999993),
//        zoom: 12,
//        mapTypeId: google.maps.MapTypeId.ROADMAP
//    }); //closing map creation
//
////	  Add traffic layer to the map.
//	  var trafficLayer = new google.maps.TrafficLayer();
//	  trafficLayer.setMap(map);
//
////	  Add Public transit layer to the map.
//	  var transitLayer = new google.maps.TransitLayer();
//	  transitLayer.setMap(map);
//
////	Function to pull in the json from the url.
//    $.getJSON("http://127.0.0.1:8000/dublinbuspredict/sampleQuery", null, function(d) {
//        console.log(d.data[0])
//        var data = d.data;
//        var points = new Array;
//        var marker, i;
//        var infowindow = new google.maps.InfoWindow();
//        var bounds = new google.maps.LatLngBounds();
//        for (i = 0; i < data.length; i++) {
//                var myLatLng = new google.maps.LatLng(data[i][3], data[i][4])
//                marker = new google.maps.Marker({
//                position: new google.maps.LatLng(data[i][3], data[i][4]),
//                map: map
//            });
//         points.push(marker.getPosition());
//         bounds.extend(marker.position);
//
//        google.maps.event.addListener(marker, 'click', (function(marker, i){
//        	return function() {
//        		infowindow.setContent(data[i][1] + "<br>" + data[i][2]);
//        		infowindow.open(map,marker);
//        	}
//        })(marker, i));
//        }
//
//      //Initialize the Path Array
//      var path = new google.maps.MVCArray();
//
//      //Initialize the Direction Service
//      var service = new google.maps.DirectionsService();
//
//      //Set the Path Stroke Color
//      var poly = new google.maps.Polyline({ map: map, strokeColor: '#4986E7' });
//
//      //Loop and Draw Path Route between the Points on MAP
//      for (var i = 0; i < points.length; i++) {
//          if ((i + 1) < points.length) {
//              var src = points[i];
//              var des = points[i + 1];
//              path.push(src);
//              poly.setPath(path);
//              service.route({
//                  origin: src,
//                  destination: des,
//                  travelMode: google.maps.DirectionsTravelMode.TRANSIT
//              })
//          }
//          }
//    });
//
//}
//

// Toggle function for route div on map.html
$(document).ready(function(){
	$("#showDetails").click(function(){
		$("#toggleDetailsRes").toggle(1000);
	});
});

// Toggle function for route div on map.html
$(document).ready(function(){
	$("#RouteMap").click(function(){
		$("#toggleRouteMap").toggle(1000);
	});
});

// Map and Marker related functions for map.html
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

//
//var jqxhr = $.getJSON("example.json", function() {
//  alert("success");
//})
//.success(function() { alert("second success"); })
//.error(function() { alert("error"); })
//.complete(function() { alert("complete"); });
//
function loadRoutes(){
    console.log('HEReeeeeeeeeeeeeee!')
    var counter = 0
    var a = $.getJSON("http://127.0.0.1:8000/dublinbuspredict/loadRoutesForMap", null, function(d) {
        $.each(d['list_routes'], function(i, p) {
            $('#dropdown-list-4').append($('<li></li>').val(p).html('<a onclick=getStops2("' + p + '")>' + p + '</a>'));
        })
    });
    var b = $.getJSON("http://127.0.0.1:8000/dublinbuspredict/divs", null, function(d) {
        console.log('Second call!');
        console.log('Results:', d);
//        if (d.length == 15){
//                console.log(p);
//        }
//        else{
////        $.each(d['info_buses'], function(i, p) {
////            console.log(p);
////            console.log(d['journey_times'])
////        })
//            var theDiv = document.getElementById("info-divs");
//            if (d['info_buses'].length == 2){
//                console.log(d['info_buses'][0])
//                var content = document.createTextNode("<div class='row my-individual-result' id='toggleDetailsRes'><div class='col-sm-2 text-center'><h5>" + (d['info_buses'][0]['predicted_arrival_time'])
//                    + "</h5></div><div class='col-sm-2 text-center'><h5>" + (d['info_buses'][1]['predicted_arrival_time']) + "</h5></div><div class='col-sm-2 text-center'><h5>" + (d['journey_time'][0]) +
//                    "</h5></div><div class='col-sm-2 text-center'><h5>Display Price</h5></div><div class='col-sm-4 text-center'><h4 id='RouteMap'>More Information</h4></div></div><div " +
//                    "class='row my-individual-result' id='toggleRouteMap'><div class='col-sm-12 text-center'><h5>Display Route table and information</h5></div></div>")
//                theDiv.appendChild(content);
//            }
//            else if (d['info_buses'].length == 4){
//                console.log(d['info_buses'][0])
//                console.log(d['journey_times'][0])
//                var content = document.createTextNode("<div class='row my-individual-result' id='toggleDetailsRes'><div class='col-sm-2 text-center'><h5>" + (d['info_buses'][0]['predicted_arrival_time'])
//                    + "</h5></div><div class='col-sm-2 text-center'><h5>" + (d['info_buses'][1]['predicted_arrival_time']) + "</h5></div><div class='col-sm-2 text-center'><h5>" + (d['journey_times'][0]) +
//                    "</h5></div><div class='col-sm-2 text-center'><h5>Display Price</h5></div><div class='col-sm-4 text-center'><h4 id='RouteMap'>More Information</h4></div></div><div " +
//                    "class='row my-individual-result' id='toggleRouteMap'><div class='col-sm-12 text-center'><h5>Display Route table and information</h5></div></div>")
//                theDiv.appendChild(content);
//                var content = document.createTextNode("<div class='row my-individual-result' id='toggleDetailsRes'><div class='col-sm-2 text-center'><h5>" + (d['info_buses'][2]['predicted_arrival_time'])
//                    + "</h5></div><div class='col-sm-2 text-center'><h5>" + (d['info_buses'][3]['predicted_arrival_time']) + "</h5></div><div class='col-sm-2 text-center'><h5>" + (d['journey_times'][1]) +
//                    "</h5></div><div class='col-sm-2 text-center'><h5>Display Price</h5></div><div class='col-sm-4 text-center'><h4 id='RouteMap'>More Information</h4></div></div><div " +
//                    "class='row my-individual-result' id='toggleRouteMap'><div class='col-sm-12 text-center'><h5>Display Route table and information</h5></div></div>")
//                theDiv.appendChild(content);
//            }
//            else if (d['info_buses'].length == 6){}
//        }
    });
}

//function loadDivs(){
//    $.getJSON("http://127.0.0.1:8000/dublinbuspredict/divs", null, function(d){
//        console.log('DIVS!')
//        console.log(d)
//    });
//}

function searchFunctionRoute2() {
    var input, filter, ul, li, a, i;
    input = document.getElementById("search-box-4");
    filter = input.value.toUpperCase();
    ul = document.getElementById("dropdown-list-4");
    li = ul.getElementsByTagName("li");
    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("a")[0];
        if (a.innerHTML.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}

function getStops2(route) {
    document.getElementById("search-box-4").value = route;
    console.log(route);
    $.getJSON("http://127.0.0.1:8000/dublinbuspredict/pilotRoutes", {"route":route}, function(d) {
        console.log(d)
        document.getElementById("dropdown-list-5").innerHTML = "";
        document.getElementById("search-box-5").value = "";
        document.getElementById("search-box-6").value = "";
    $.each(d['stops'], function(i, p) {
        $('#dropdown-list-5').append($('<li></li>').val(p).html('<a onclick=getStopsDest2(' + p + ')>' + route + ' - ' + p + '</a>'));
    });
    });
}

function searchFunctionSRC2() {
    var input, filter, ul, li, a, i;
    input = document.getElementById("search-box-5");
    filter = input.value.toUpperCase();
    ul = document.getElementById("dropdown-list-5");
    li = ul.getElementsByTagName("li");
    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("a")[0];
        if (a.innerHTML.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}

function getStopsDest2(source) {
    document.getElementById("search-box-5").value = source;
    console.log('Source:', source);
    route = document.getElementById("search-box-4").value;
    console.log ('Route:', route)
    $.getJSON("http://127.0.0.1:8000/dublinbuspredict/pilotDest", {"route":route, "source":source}, function(d) {
        console.log(d)
        document.getElementById("dropdown-list-6").innerHTML = "";
        document.getElementById("search-box-6").value = "";
    $.each(d['stops'], function(i, p) {
        $('#dropdown-list-6').append($('<li></li>').val(p).html('<a onclick=getStopsDestExtra2(' + p + ')>' + route + ' - ' + p + '</a>'));
    });
    });
}

function getStopsDestExtra2(stop){
    document.getElementById("search-box-6").value = stop;
}

function searchFunctionDest2() {
    var input, filter, ul, li, a, i;
    input = document.getElementById("search-box-6");
    filter = input.value.toUpperCase();
    ul = document.getElementById("dropdown-list-6");
    li = ul.getElementsByTagName("li");
    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("a")[0];
        if (a.innerHTML.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}
