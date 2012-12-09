{%for road in ROADS %}
  var points = new google.maps.MVCArray();
{% for coord in road.coords %}
  points.push(new google.maps.LatLng({{coord.lat}}, {{coord.lng}}));
{% endfor %}
createPolyline(map, points);
{% endfor %}
              }*/

/*function formSubmit(){
 *   var f = getElementById("coord_form");
 *     alert(f.["start lng"]);
 *       }*/



function displayMarkers(map) {
  {% for coord in COORDS %}
    createMarker(map, new google.maps.LatLng({{coord.lat}},{{coord.lng}}),"" + {{coord.id}})
  {% endfor %}
}

