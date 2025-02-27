from app.persistence.repository import InMemoryRepository

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_amenity(self, amenity_data):
        name = amenity_data.get('name')
        if not name or len(name) > 50:
            raise ValueError("Amenity name is required and must be less than or equal to 50 characters.")

        new_amenity = {'name': name}
        return self.amenity_repo.create(new_amenity)

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get_by_id(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        name = amenity_data.get('name')
        if not name or len(name) > 50:
            raise ValueError("Amenity name is required and must be less than or equal to 50 characters.")

        updated_amenity = self.amenity_repo.update(amenity_id, {'name': name})
        if not updated_amenity:
            raise ValueError(f"No amenity found with ID {amenity_id}.")
        return updated_amenity

    def delete_amenity(self, amenity_id):
        return self.amenity_repo.delete(amenity_id)

