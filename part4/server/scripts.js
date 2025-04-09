document.addEventListener('DOMContentLoaded', () => {
  const loginLink = document.getElementById('login-link');
  const placesList = document.getElementById('places-list');
  const priceFilter = document.getElementById('price-filter');
  const placeDetailsSection = document.getElementById('place-details');
  const reviewsSection = document.getElementById('reviews');
  const addReviewSection = document.getElementById('add-review');
  const reviewForm = document.getElementById('review-form');

  let placesData = [];

  // Utilitaire pour récupérer un cookie
  function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
  }

  // Vérifie si l'utilisateur est authentifié
  function checkAuthentication(redirectIfNotAuth = false) {
    const token = getCookie('token');

    if (!token && redirectIfNotAuth) {
      window.location.href = 'index.html';
    }

    if (!token && loginLink) loginLink.style.display = 'block';
    if (token && loginLink) {
      loginLink.textContent = 'My Account';
      loginLink.href = 'profile.html';
    }

    if (token && addReviewSection) addReviewSection.style.display = 'block';
    if (!token && addReviewSection) addReviewSection.style.display = 'none';

    return token;
  }

  // Récupérer l'ID du lieu depuis l'URL
  function getPlaceIdFromURL() {
    const params = new URLSearchParams(window.location.search);
    return params.get('id');
  }

  // Affiche la liste des places
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
        <button class="details-button" onclick="location.href='place.html?id=${place.id}'">View Details</button>
      `;

      placesList.appendChild(placeCard);
    });
  }

  // Fetch de la liste des places
  async function fetchPlaces(token) {
    try {
      const response = await fetch('http://localhost:5000/api/v1/places', {
        headers: token ? { 'Authorization': `Bearer ${token}` } : {}
      });

      if (!response.ok) throw new Error(`Error fetching places: ${response.statusText}`);

      const data = await response.json();
      placesData = data.places; // ✅ Correction ici
      displayPlaces(placesData);
    } catch (error) {
      console.error(error);
      if (placesList) placesList.innerHTML = '<p>Unable to fetch places. Please try again later.</p>';
    }
  }

  // Filtre de prix
  function filterPlacesByPrice(maxPrice) {
    if (maxPrice === 'all') {
      displayPlaces(placesData);
    } else {
      const filteredPlaces = placesData.filter(place => place.price <= parseInt(maxPrice)); // ✅ Correction ici
      displayPlaces(filteredPlaces);
    }
  }

  // Fetch des détails d'un lieu
  async function fetchPlaceDetails(token, placeId) {
    try {
      const response = await fetch(`http://localhost:5000/api/v1/places/${placeId}`, {
        headers: token ? { 'Authorization': `Bearer ${token}` } : {}
      });

      if (!response.ok) throw new Error(`Error fetching place details: ${response.statusText}`);

      const place = await response.json();
      displayPlaceDetails(place);
    } catch (error) {
      console.error(error);
      if (placeDetailsSection) placeDetailsSection.innerHTML = '<p>Unable to fetch place details.</p>';
    }
  }

  // Affichage des détails d'un lieu
  function displayPlaceDetails(place) {
    if (!placeDetailsSection || !reviewsSection) return;

    placeDetailsSection.innerHTML = `
      <h1>${place.title}</h1>
      <p><strong>Host:</strong> ${place.owner_id}</p>
      <p><strong>Price per night:</strong> $${place.price}</p>
      <p><strong>Description:</strong> ${place.description}</p>
      <p><strong>Amenities:</strong> ${place.amenities.join(', ') || 'No amenities listed'}</p>
    `;

    reviewsSection.innerHTML = `<h2>Reviews</h2>`;
    if (place.reviews && place.reviews.length > 0) {
      place.reviews.forEach(review => {
        const reviewCard = document.createElement('article');
        reviewCard.className = 'review-card';

        reviewCard.innerHTML = `
          <p><strong>${review.user}:</strong></p>
          <p>${review.comment}</p>
          <p>Rating: ${'★'.repeat(review.rating)}${'☆'.repeat(5 - review.rating)}</p>
        `;

        reviewsSection.appendChild(reviewCard);
      });
    } else {
      reviewsSection.innerHTML += `<p>No reviews yet.</p>`;
    }
  }

  // Soumission d'un avis (Add Review Page)
  async function submitReview(token, placeId, reviewText, rating) {
    try {
      const response = await fetch(`http://localhost:5000/api/v1/places/${placeId}/reviews`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
          comment: reviewText,
          rating: parseInt(rating)
        })
      });

      if (response.ok) {
        alert('Review submitted successfully!');
        if (reviewForm) reviewForm.reset();
      } else {
        const data = await response.json();
        alert(`Failed to submit review: ${data.message || 'Unknown error'}`);
      }
    } catch (error) {
      console.error('Error submitting review:', error);
      alert('An error occurred while submitting the review. Please try again.');
    }
  }

  // Initialisation globale
  const token = checkAuthentication();

  if (placesList) {
    fetchPlaces(token);
  }

  if (priceFilter) {
    priceFilter.addEventListener('change', (event) => {
      filterPlacesByPrice(event.target.value);
    });
  }

  const placeId = getPlaceIdFromURL();

  if (placeDetailsSection && placeId) {
    fetchPlaceDetails(token, placeId);
  }

  if (reviewForm && placeId) {
    const tokenForReview = checkAuthentication(true); // Force redirect if not authenticated
    reviewForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      const reviewText = document.getElementById('review-text').value;
      const rating = document.getElementById('rating').value;
      await submitReview(tokenForReview, placeId, reviewText, rating);
    });
  }
});
