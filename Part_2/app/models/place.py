#!/usr/bin/python3

from app.models.base_model import BaseModel
from .user import User


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities

    @property
    def title(self):
        return self.title

    @title.setter
    def title(self, value):
        if value is None or not isinstance(value, str):
            raise TypeError('title must be a non-empty string')
        if not value or len(value) > 100:
            raise ValueError('title must 100 characters or less')
        self.title = value

    @property
    def description(self):
        return self.description

    @description.setter
    def description(self, value):
        if value is None or not isinstance(value, str):
            raise TypeError('description must be a non-empty string')
        self.description = value

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, value):
        if value is None or not isinstance(value, float):
            raise TypeError('price must be a float')
        if value < 0:
            raise ValueError('price must be a positive float')
        self.price = value

    @property
    def latitude(self):
        return self.latitude

    @latitude.setter
    def latitude(self, value):
        if value is None or not isinstance(value, float):
            raise TypeError('latitude must be a float')
        if value < -90 or value > 90:
            raise ValueError('latitude must be between -90 and 90')
        self.latitude = value

    @property
    def longitude(self):
        return self.longitude

    @longitude.setter
    def longitude(self, value):
        if value is None or not isinstance(value, float):
            raise TypeError('longitude must be a float')
        if value < -180 or value > 180:
            raise ValueError('longitude must be between -180 and 180')
        self.longitude = value

    @property
    def owner(self):
        return self.owner

    @owner.setter
    def owner(self, owner):
        if owner is None or not isinstance(owner, User):
            raise TypeError('owner must be an User')
        self.owner = owner

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
