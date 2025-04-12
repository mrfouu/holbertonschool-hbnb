console.log('✅ Fichier JS chargé correctement');
document.addEventListener('DOMContentLoaded', async () => {
    const reviewForm = document.getElementById('review-form');
  
    function getPlaceIdFromURL() {
      const params = new URLSearchParams(window.location.search);
      return params.get('id');
    }
  
    function getCookie(name) {
      const value = `; ${document.cookie}`;
      const parts = value.split(`; ${name}=`);
  
      if (parts.length === 2) return parts.pop().split(';').shift();
      return null;
    }
  
    async function submitReview(token, placeId, reviewText, rating) {
      try {
        const response = await fetch(`http://localhost:5000/api/v1/reviews/${placeId}`, {
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
          reviewForm.reset();
  
          // ✅ Redirection vers la page du lieu après soumission
          window.location.href = `place.html?id=${placeId}`;
        } else {
          const data = await response.json();
          alert(`Failed to submit review: ${data.message || 'Unknown error'}`);
        }
      } catch (error) {
        console.error('Error submitting review:', error);
        alert('An error occurred while submitting the review. Please try again.');
      }
    }
  
    const token = getCookie('token');
    const placeId = getPlaceIdFromURL();
  
    if (!token || !placeId) {
      alert('Missing token or place ID. Please make sure you are logged in and have selected a place.');
      window.location.href = 'index.html';
      return;
    }
  
    reviewForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      console.log('Form submitted');
      const reviewText = document.getElementById('review').value;
      const rating = document.getElementById('rating').value;
      await submitReview(token, placeId, reviewText, rating);
    });
  });
  