#!/usr/bin/python3

from app.models.base_model import BaseModel
from .user import User
from app import db, bcrypt

class Place(BaseModel):
    __tablename__ = 'places'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String, nullable=True)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)  # Clé étrangère vers User

    # Relations
    reviews = db.relationship('Review', backref='place', lazy=True)  # One-to-Many avec Review
    amenities = db.relationship('Amenity', secondary='place_amenity', backref='places', lazy=True)  # Many-to-Many avec Amenity

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if value is None or not isinstance(value, str):
            raise TypeError('title must be a non-empty string')
        if not value or len(value) > 100:
            raise ValueError('title must be 100 characters or less')
        self._title = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if value is None or not isinstance(value, str):
            raise TypeError('description must be a non-empty string')
        self._description = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value is None or not isinstance(value, float):
            raise TypeError('price must be a float')
        if value < 0:
            raise ValueError('price must be a positive float')
        self._price = value

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if value is None or not isinstance(value, float):
            raise TypeError('latitude must be a float')
        if value < -90.0 or value > 90.0:
            raise ValueError('latitude must be between -90 and 90')
        self._latitude = value

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if value is None or not isinstance(value, float):
            raise TypeError('longitude must be a float')
        if value < -180.0 or value > 180.0:
            raise ValueError('longitude must be between -180 and 180')
        self._longitude = value

    @property
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        if owner_id is None or not isinstance(owner_id, User):
            raise TypeError('owner must be an User')
        self._owner_id = owner_id

    def add_review(self, review):
        """Add a review to the place."""
        self._reviews.append(review)
        self.save()

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self._amenities.append(amenity)
        self.save()

    def validate(self):
        if self._latitude is None or not isinstance(self._latitude, float):
            raise TypeError('latitude must be a float')
        if self._latitude < -90.0 or self._latitude > 90.0:
            raise ValueError('latitude must be between -90 and 90')

        if self._longitude is None or not isinstance(self._longitude, float):
            raise TypeError('longitude must be a float')
        if self._longitude < -180.0 or self._longitude > 180.0:
            raise ValueError('longitude must be between -180 and 180')

        if self._owner_id == "" or not isinstance(self._owner_id, str):
            raise TypeError('owner must be a string')

        if self._price is None or not isinstance(self._price, float):
            raise TypeError('price must be a float')
        if self._price < 0:
            raise ValueError('price must be a positive float')

        if self._description is None or not isinstance(self._description, str):
            raise TypeError('description must be a non-empty string')

        if self._title is None or not isinstance(self._title, str):
            raise TypeError('title must be a non-empty string')
        if not self._title or len(self._title) > 100:
            raise ValueError('title must be 100 characters or less')