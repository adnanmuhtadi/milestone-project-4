// Take from https://developers.google.com/maps/documentation/javascript/adding-a-google-map#maps_add_map-javascript
// Initialize and add the map
function initMap() {
  // The location of Uluru
  const uluru = { lat: 37.946, lng: -121.719 };
  // The map, centered at Uluru
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 13,
    center: uluru,
  });
  // The marker, positioned at Uluru
  const marker = new google.maps.Marker({
    position: uluru,
    map: map,
  });
}