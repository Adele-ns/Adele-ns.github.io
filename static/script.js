// static/script.js
$(document).ready(function () {
    // Coordonnées géographiques de Paris
    var parisCoordinates = [48.8566, 2.3522];

    // Initialiser la carte Leaflet centrée sur [0, 0] (au centre du monde)
    var map = L.map('map-container').setView([0, 0], 2);

    // Ajouter une couche de tuiles (OpenStreetMap)
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/s{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // Ajouter un marqueur à Paris
    L.marker(parisCoordinates).addTo(map).bindPopup('Made in France');
});

