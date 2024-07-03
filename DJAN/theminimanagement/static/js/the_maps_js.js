var map = L.map('map').setView([-44.9612115, 168.5256356], 10);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

function getCoordinates(address, callback) {
    fetch(`https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(address)}`)
        .then(response => response.json())
        .then(data => {
            if (data && data.length > 0) {
                callback(data[0].lat, data[0].lon);
            } else {
                console.error('No coordinates found for address:', address);
            }
        })
        .catch(error => console.error('Error fetching coordinates:', error));
}

var locations = [
    {
        address: "164 McDonnell Road, Arrowtown 9351",
        infoPage: "job1.html"
    },
    {
        address: "166 Centennial Avenue, Arrowtown 9371",
        infoPage: "job2.html"
    },
    {
        address: "Joe Oconnell Drive, Frankton, Queenstown 9371",
        infoPage: "job3.html"
    }
];

locations.forEach(location => {
    getCoordinates(location.address, (lat, lon) => {
        L.marker([lat, lon]).addTo(map)
          .bindPopup(`<b>${location.address}</b><br><a href="${location.infoPage}" target="_blank">More info</a>`)
          .openPopup();
        });
});