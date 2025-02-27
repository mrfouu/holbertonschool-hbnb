from app.persistence.repository import InMemoryRepository


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # Placeholder method for creating a user
    def create_user(self, user_data):
        # Logic will be implemented in later tasks
        pass

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_email(email)

    def get_all_users(self):
        return self.user_repo.get_all()

    def update_user(self, user_id, user_data):
        # Logic will be implemented in later tasks
        pass

    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        # Logic will be implemented in later tasks
        return self.place_repo.get_places(place_id)

    def get_all_places(self):
        # Logic will be implemented in later tasks
        return self.place_repo.get_all_places()

    def create_place(self, place_data):
        # Placeholder for logic to create a place-l "é "
        return self.place_repo.create_place(place_data)


    def update_place(self, place_id, place_data):
        # Placeholder for logic to update a place
        return self.place_repo.update_place(place_id, place_data)

    #amenities
    def create_amenity(self, amenity_data):
        # Placeholder for logic to create an amenity
        pass

    def get_amenity(self, amenity_id):
        # Placeholder for logic to retrieve an amenity by ID
        pass

    def get_all_amenities(self):
        # Placeholder for logic to retrieve all amenities
        pass

    def update_amenity(self, amenity_id, amenity_data):
        # Placeholder for logic to update an amenity
        pass

    def create_review(self, review_data):
        review = self.review_repo.add(review_data)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        return self.review_repo.get_by_place(place_id)

    def update_review(self, review_id, review_data):
        review = self.review_repo.update(review_id, review_data)

        if 'rating' in review_data:
            review.rating = review_data['rating']
        if 'text' in review_data:
            review.text = review_data['text']
        if 'user_id' in review_data:
            review.user_id = review_data['user_id']
        if 'place_id' in review_data:
            review.place_id = review_data['place_id']

    def delete_review(self, review_id):
        review = self.review_repo.delete(review_id)

        if review:
            self.review_repo.delete(review_id)
            return {message: 'Review deleted successfully'}, 200
        else:
            return {message: 'Review not found'}, 404
