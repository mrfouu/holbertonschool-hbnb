  const currentPage = window.location.pathname;
  console.log('📄 Page actuelle :', currentPage);

  document.addEventListener('DOMContentLoaded', async () => {

    const loginLink = document.getElementById('login-link');
    const placesList = document.getElementById('places-list');
    const priceFilter = document.getElementById('price-filter');
    const placeDetailsSection = document.getElementById('place-details');
    const reviewsSection = document.getElementById('reviews');
    const addReviewSection = document.getElementById('add-review');
    const reviewForm = document.getElementById('review-form');

    let placesData = [];

    function getCookie(name) {
      const value = `; ${document.cookie}`;
      const parts = value.split(`; ${name}=`);
      if (parts.length === 2) return parts.pop().split(';').shift();
    }

    function checkAuthentication(forceRedirect = false) {
      const token = getCookie('token');
    
      if (!token) {
        if (forceRedirect) {
          window.location.href = 'login.html';
        }
        return null;
      }
    
      return fetch('http://localhost:5000/api/v1/auth/protected', {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      })
        .then(response => {
          if (!response.ok) {
            document.cookie = 'token=; Max-Age=0; path=/';
            if (forceRedirect) {
              window.location.href = 'login.html';
            }
            return null;
          }
    
          if (loginLink) {
            loginLink.textContent = 'My Account';
            loginLink.href = 'profile.html';
          }
    
          if (addReviewSection) {
            addReviewSection.style.display = 'block';
          }
    
          return token;
        })
        .catch(error => {
          console.error('Erreur de vérification du token :', error);
          if (forceRedirect) window.location.href = 'login.html';
          return null;
        });
    }
    
    

    function getPlaceIdFromURL() {
      const params = new URLSearchParams(window.location.search);
      return params.get('id');
    }

    function displayPlaces(places) {
      if (!placesList) return;
      placesList.innerHTML = '';

      places.forEach(place => {
        const placeCard = document.createElement('article');
        placeCard.className = 'place-card';

        const titleElement = document.createElement('h2');
        titleElement.textContent = place.title;

        const priceElement = document.createElement('p');
        priceElement.textContent = `Price per night: $${place.price}`;

        const descriptionElement = document.createElement('p');
        descriptionElement.textContent = place.description;

        const detailsButton = document.createElement('button');
        detailsButton.className = 'details-button';
        detailsButton.textContent = 'View Details';
        
        const basePath = window.location.pathname.replace(/index\.html$/, '');
        detailsButton.addEventListener('click', () => {
          location.href = `${basePath}place.html?id=${place.id}`;
        });
        

        placeCard.appendChild(titleElement);
        placeCard.appendChild(priceElement);
        placeCard.appendChild(descriptionElement);
        placeCard.appendChild(detailsButton);

        placesList.appendChild(placeCard);
      });
    }

    async function fetchPlaces(token) {
      try {
        const response = await fetch('http://localhost:5000/api/v1/places/', {
          headers: token ? { 'Authorization': `Bearer ${token}` } : {}
        });

        if (!response.ok) throw new Error(`Error fetching places: ${response.statusText}`);

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

    function filterPlacesByPrice(maxPrice) {
      if (maxPrice === 'all') {
        displayPlaces(placesData);
      } else {
        const filteredPlaces = placesData.filter(place => place.price <= parseInt(maxPrice));
        displayPlaces(filteredPlaces);
      }
    }

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
        if (placeDetailsSection) placeDetailsSection.textContent = 'Unable to fetch place details.';
      }
    }

    function displayPlaceDetails(place) {
      if (!placeDetailsSection || !reviewsSection) return;

      placeDetailsSection.textContent = '';
      reviewsSection.textContent = '';

      const titleElement = document.createElement('h1');
      titleElement.textContent = place.title;

      const hostElement = document.createElement('p');
      hostElement.innerHTML = `<strong>Host:</strong> ${place.owner_id}`;

      const priceElement = document.createElement('p');
      priceElement.innerHTML = `<strong>Price per night:</strong> $${place.price}`;

      const descriptionElement = document.createElement('p');
      descriptionElement.innerHTML = `<strong>Description:</strong> ${place.description}`;

      const amenitiesElement = document.createElement('p');
      amenitiesElement.innerHTML = `<strong>Amenities:</strong> ${place.amenities.join(', ') || 'No amenities listed'}`;

      placeDetailsSection.appendChild(titleElement);
      placeDetailsSection.appendChild(hostElement);
      placeDetailsSection.appendChild(priceElement);
      placeDetailsSection.appendChild(descriptionElement);
      placeDetailsSection.appendChild(amenitiesElement);

      const reviewsTitle = document.createElement('h2');
      reviewsTitle.textContent = 'Reviews';
      reviewsSection.appendChild(reviewsTitle);

      if (place.reviews && place.reviews.length > 0) {
        place.reviews.forEach(review => {
          const reviewCard = document.createElement('article');
          reviewCard.className = 'review-card';

          const reviewerElement = document.createElement('p');
          reviewerElement.innerHTML = `<strong>${review.user}:</strong>`;

          const commentElement = document.createElement('p');
          commentElement.textContent = review.comment;

          const ratingElement = document.createElement('p');
          ratingElement.textContent = `Rating: ${'★'.repeat(review.rating)}${'☆'.repeat(5 - review.rating)}`;

          reviewCard.appendChild(reviewerElement);
          reviewCard.appendChild(commentElement);
          reviewCard.appendChild(ratingElement);

          reviewsSection.appendChild(reviewCard);
        });
      } else {
        const noReviewsElement = document.createElement('p');
        noReviewsElement.textContent = 'No reviews yet.';
        reviewsSection.appendChild(noReviewsElement);
      }
    }

    async function submitReview(token, placeId, reviewText, rating) {
      try {
        const response = await fetch(`http://localhost:5000/api/v1/places/${placeId}/reviews/`, {
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

    const token = await checkAuthentication();


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

    if (reviewForm && currentPage.includes('_add_review.html')) {
      const tokenForReview = await checkAuthentication(true);
      reviewForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const reviewText = document.getElementById('review').value;
        const rating = document.getElementById('rating').value;
        await submitReview(tokenForReview, placeId, reviewText, rating);
      });
    } else {
      checkAuthentication();
    }  
  });
