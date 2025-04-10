document.addEventListener('DOMContentLoaded', async () => {
  const placesList = document.getElementById('places-list');
  const priceFilter = document.getElementById('price-filter');
  let placesData = [];

  async function fetchPlaces(token) {
    try {
      const response = await fetch('http://localhost:5000/api/v1/places/', {
        headers: token ? { 'Authorization': `Bearer ${token}` } : {}
      });
      if (!response.ok) throw new Error('Error fetching places');
      const data = await response.json();
      placesData = data.places;
      displayPlaces(placesData);
    } catch (error) {
      console.error(error);
      if (placesList) {
        placesList.textContent = 'Unable to fetch places. Please try again later.';
      }
    }
  }

  function displayPlaces(places) {
    if (!placesList) return;
    placesList.innerHTML = '';

    places.forEach(place => {
      const placeCard = document.createElement('article');
      placeCard.className = 'place-card';

      placeCard.innerHTML = `
        <h2>${place.title}</h2>
        <p>Price per night: $${place.price}</p>
        <p>${place.description}</p>
        <button class="details-button">View Details</button>
      `;

      const detailsButton = placeCard.querySelector('.details-button');
      detailsButton.addEventListener('click', () => {
        location.href = `place.html?id=${place.id}`;
      });

      placesList.appendChild(placeCard);
    });
  }

  function filterPlacesByPrice(maxPrice) {
    const filtered = maxPrice === 'all' ? placesData : placesData.filter(p => p.price <= parseInt(maxPrice));
    displayPlaces(filtered);
  }

  const token = await getCookie('token');
  await fetchPlaces(token);

  if (priceFilter) {
    priceFilter.addEventListener('change', e => filterPlacesByPrice(e.target.value));
  }
});
function getPlaceIdFromURL() {
    const params = new URLSearchParams(window.location.search);
    return params.get('id');
  }
 function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
  }