document.addEventListener('DOMContentLoaded', async () => {
  const placeDetailsSection = document.getElementById('place-details');
  const reviewsSection = document.getElementById('reviews');
  const reviewForm = document.getElementById('review-form');

  async function fetchPlaceDetails(token, placeId) {
    try {
      const response = await fetch(`http://localhost:5000/api/v1/places/`, {
        headers: token ? { 'Authorization': `Bearer ${token}` } : {}
      });
      if (!response.ok) throw new Error('Error fetching place details');
      const place = await response.json();
      displayPlaceDetails(place);
    } catch (error) {
      console.error(error);
      if (placeDetailsSection) placeDetailsSection.textContent = 'Unable to fetch place details.';
    }
  }

  function displayPlaceDetails(place) {
    if (!placeDetailsSection || !reviewsSection) return;
  
    // Correction ici : je récupère proprement les noms ou ids des amenities
    const amenitiesList = Array.isArray(place.amenities)
      ? place.amenities.map(amenity => amenity.name || amenity.id).join(', ')
      : 'No amenities listed';
  
    placeDetailsSection.innerHTML = `
      <h1>${place.title}</h1>
      <p><strong>Host:</strong> ${place.owner_id}</p>
      <p><strong>Price per night:</strong> $${place.price}</p>
      <p><strong>Description:</strong> ${place.description}</p>
      <p><strong>Amenities:</strong> ${amenitiesList}</p>
    `;
  
    reviewsSection.innerHTML = '<h2>Reviews</h2>';
  
    if (place.reviews && place.reviews.length > 0) {
      place.reviews.forEach(review => {
        reviewsSection.innerHTML += `
          <article class="review-card">
            <p><strong>${review.user}:</strong></p>
            <p>${review.comment}</p>
            <p>Rating: ${'★'.repeat(review.rating)}${'☆'.repeat(5 - review.rating)}</p>
          </article>
        `;
      });
    } else {
      reviewsSection.innerHTML += '<p>No reviews yet.</p>';
    }
  }
  

  async function submitReview(token, placeId, reviewText, rating) {
    try {
      const response = await fetch(`http://localhost:5000/api/v1/reviews/`, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${token}`
  },
  credentials: 'include', // ✅ ajoute ceci pour les cookies / auth header
  mode: 'cors', // ✅ ajoute le mode CORS
  body: JSON.stringify({
    text: reviewText,
    rating: parseInt(rating),
    place_id: placeId,
    user_id: getUserIdFromToken(token)
  })
});

  
      if (response.ok) {
        alert('Review submitted successfully!');
        reviewForm.reset();
        await fetchPlaceDetails(token, placeId); // ✅ refresh reviews
      } else {
        const data = await response.json();
        alert(`Failed to submit review: ${data.message || 'Unknown error'}`);
      }
    } catch (error) {
      console.error('Error submitting review:', error);
      alert('An error occurred while submitting the review. Please try again.');
    }
  }
  

  function getPlaceIdFromURL() {
    const params = new URLSearchParams(window.location.search);
    return params.get('id');
  }

  function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
  }

  const token = await getCookie('token');
  const placeId = getPlaceIdFromURL();
  if (placeId) await fetchPlaceDetails(token, placeId);

  function getUserIdFromToken(token) {
    if (!token) return null;
    const payload = JSON.parse(atob(token.split('.')[1]));
    return payload.sub.id;
  }
  

  if (reviewForm && token && placeId) {
    reviewForm.addEventListener('submit', async event => {
      event.preventDefault();
      const reviewText = document.getElementById('review').value;
      const rating = document.getElementById('rating').value;
      await submitReview(token, placeId, reviewText, rating);
    });
  }
});
