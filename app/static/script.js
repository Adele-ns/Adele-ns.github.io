// static/script.js
$(document).ready(function () {
    // Coordonnées géographiques de Paris
    var parisCoordinates = [48.8, 2.3];

    // Initialiser la carte Leaflet centrée sur [0, 0] (au centre du monde)
    var map = L.map('map-container').setView([0, 0], 2);

    // Ajouter une couche de tuiles (OpenStreetMap)
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

    // Ajouter un marqueur à Paris
    L.marker(parisCoordinates).addTo(map)
        .bindPopup('Made in France');
});

