var map = L.mapbox.map('map').setView([-12.03034, -77.06630], 6);

var osm = L.tileLayer('http://tile.openstreetmap.org/{z}/{x}/{y}.png');
var goglesatelite = L.tileLayer('https://khms0.google.com/kh/v=145&src=app&x={x}&y={y}&z={z}');
var goglemap = L.tileLayer('https://mts0.google.com/vt/hl=es&src=app&x={x}&y={y}&z={z}');

L.control.layers({
    'Distritos': L.mapbox.tileLayer('examples.map-9ijuk24y').addTo(map),
    'Mapbox': L.mapbox.tileLayer('ruben.map-tlseskm0'),
    'Open Street Map': osm,
    'Google Satelite': goglesatelite,
    'Google Map': goglemap

}).addTo(map);
