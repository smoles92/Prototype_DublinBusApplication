function searchFunctionRoute() {
    var input, filter, ul, li, a, i;
    input = document.getElementById("search-box-1");
    filter = input.value.toUpperCase();
    ul = document.getElementById("dropdown-list-1");
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

function getStops(route) {
    document.getElementById("search-box-1").value = route;
    console.log(route);
    $.getJSON("http://127.0.0.1:8000/dublinbuspredict/pilotRoutes", {"route":route}, function(d) {
        console.log(d)
        document.getElementById("dropdown-list-2").innerHTML = "";
        document.getElementById("search-box-2").value = "";
        document.getElementById("search-box-3").value = "";
    $.each(d['stops'], function(i, p) {
        $('#dropdown-list-2').append($('<li></li>').val(p).html('<a onclick=getStopsDest(' + p + ')>' + route + ' - ' + p + '</a>'));
    });
//        for (i = 0; i < d['stops'].length; i++) {
//            console.log(d['stops'][i]);
//        }
    });
}

function searchFunctionSRC() {
    var input, filter, ul, li, a, i;
    input = document.getElementById("search-box-2");
    filter = input.value.toUpperCase();
    ul = document.getElementById("dropdown-list-2");
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

function getStopsDest(source) {
    document.getElementById("search-box-2").value = source;
    console.log('Source:', source);
    route = document.getElementById("search-box-1").value;
    console.log ('Route:', route)
    $.getJSON("http://127.0.0.1:8000/dublinbuspredict/pilotDest", {"route":route, "source":source}, function(d) {
        console.log(d)
        document.getElementById("dropdown-list-3").innerHTML = "";
        document.getElementById("search-box-3").value = "";
    $.each(d['stops'], function(i, p) {
        $('#dropdown-list-3').append($('<li></li>').val(p).html('<a onclick=getStopsDestExtra(' + p + ')>' + route + ' - ' + p + '</a>'));
    });
    });
}

function getStopsDestExtra(stop){
    document.getElementById("search-box-3").value = stop;
}

function searchFunctionDest() {
    var input, filter, ul, li, a, i;
    input = document.getElementById("search-box-3");
    filter = input.value.toUpperCase();
    ul = document.getElementById("dropdown-list-3");
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

//function passToMap() {
//    route = document.getElementById("search-box-1").value;
//    source = document.getElementById("search-box-2").value;
//    destination = route = document.getElementById("search-box-3").value;
//    console.log('Route:', route)
//    console.log('Source:', source)
//    console.log('Destination:', destination)
//}
