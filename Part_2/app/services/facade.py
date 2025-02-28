from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # Placeholder method for creating a user
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        # Logic will be implemented in later tasks
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_email('email', email)
        return self.user_repo.get_by_attribute('email', email)

    def get_all_users(self):
        return self.user_repo.get_all()

    def update_user(self, user_id, user_data):
        user = self.user_repo.get(user_id)
        if not user:
            return None
        for key, value in user_data.items():
            if hasattr(user, key):
                setattr(user, key, value)
        # Logic will be implemented in later tasks
        user = self.user_repo.get(user_id)
        if not user:
            return None
        if 'first_name' in user_data:
            user.first_name = user_data['first_name']
        if 'last_name' in user_data:
            user.last_name = user_data['last_name']
        if 'email' in user_data:
            user.email = user_data['email']

        self.user_repo.update(user_id, user_data)
        return user

    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        # Logic will be implemented in later tasks
        return self.place_repo.get(place_id)

    def get_all_places(self):
        # Logic will be implemented in later tasks
        return self.place_repo.get_all()

    def create_place(self, place_data):
        # Placeholder for logic to create a place-l "é "
        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def update_place(self, place_id, place_data):
        # Placeholder for logic to update a place
        place = self.place_repo.get(place_id)
        if place:
            if 'title' in place_data:
                place.title = place_data['title']
            if 'description' in place_data:
                place.description = place_data['description']
            if 'price' in place_data:
                place.price = place_data['price']
            if 'latitude' in place_data:
                place.latitude = place_data['latitude']
            if 'longitude' in place_data:
                place.longitude = place_data['longitude']
            if 'owner_id' in place_data:
                place.owner_id = place_data['owner_id']
            if 'amenities' in place_data:
                place.amenities = place_data['amenities']
            self.place_repo.update(place_id, place_data)
        return place

    # amenities
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.amenity_repo.get(amenity_id)
        if amenity:
            if 'name' in amenity_data:
                amenity.name = amenity_data['name']
            self.amenity_repo.update(amenity_id, amenity_data)
        return amenity

    def create_review(self, review_data):
        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        return [
            review for review in self.review_repo.get_all()
            if review.place_id == place_id]


    def update_review(self, review_id, review_data):
        review = self.review_repo.get(review_id)
        if not review:
            return None

        if 'rating' in review_data:
            review.rating = review_data['rating']
        if 'text' in review_data:
            review.text = review_data['text']
        if 'user_id' in review_data:
            review.user_id = review_data['user_id']
        if 'place_id' in review_data:
            review.place_id = review_data['place_id']

        self.review_repo.update(review_id, review_data)
        return review
