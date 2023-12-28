// static/script.js
$(document).ready(function () {
    // Initialiser la carte Leaflet
    var map = L.map('map-container').setView([0, 0], 2);

    // Ajouter une couche de tuiles (OpenStreetMap)
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // Exemple : Ajouter un marqueur au centre de la carte
    L.marker([0, 0]).addTo(map).bindPopup('Centre de la carte');

    // Ajoutez votre propre logique pour la carte ici
});

