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
        # Logic will be implemented in later tasks
        user = User(**user_data)
        user = self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def get_all_users(self):
        return self.user_repo.get_all()

    def update_user(self, user_id, user_data):
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

        self.user_repo.update(user, user_data)
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
        place = self.place_repo.add(place_data)
        return place


    def update_place(self, place_id, place_data):
        # Placeholder for logic to update a place
        place = self.place_repo.get(place_id)
        if not place:
            return None
        if 'name' in place_data:
            place.name = place_data['name']
        if 'description' in place_data:
            place.description = place_data['description']
        if 'owner_id' in place_data:
            place.owner_id = place_data['owner_id']
        if 'address' in place_data:
            place.address = place_data['address']
        if 'city' in place_data:
            place.city = place_data['city']
        return self.place_repo.update(place_id, place_data)

    #amenities
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        name = amenity_data.get('name')
        if not name or len(name) > 50:
            raise ValueError("Amenity name is required and must be less than or equal to 50 characters.")

        new_amenity = {'name': name}
        return self.amenity_repo.add(new_amenity)

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.amenity_repo.get(amenity_id)
        if not amenity:
            raise ValueError(f"No amenity found with ID {amenity_id}.")

        name = amenity_data.get('name')
        if not name or len(name) > 50:
            raise ValueError("Amenity name is required and must be less than or equal to 50 characters.")

        amenity.name = name
        return self.amenity_repo.update(amenity_id, amenity)

    def create_review(self, review_data):
        review = Review(**review_data)
        review = self.review_repo.add(review_data)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        return self.review_repo.get_by_attribute('place_id', place_id)

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

        return self.review_repo.update(review_id, review)
