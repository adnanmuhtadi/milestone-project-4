// Take from https://developers.google.com/maps/documentation/javascript/adding-a-google-map#maps_add_map-javascript
// Initialize and add the map
function initMap() {
  // The location of Manchester
  const Manchester = { lat: 53.480, lng: -2.235 };
  // The map, centered at Manchester
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 15,
    center: Manchester,
  });
  // The marker, positioned at Manchester
  const marker = new google.maps.Marker({
    position: Manchester,
    map: map,
  });
}