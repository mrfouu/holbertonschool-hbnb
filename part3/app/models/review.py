#!/usr/bin/python3

from app.models.base_model import BaseModel
from app import db, bcrypt


class Review(BaseModel):
    def __init__(self, place_id, user_id, text, rating):
        """
        Initialize a new Review instance.
        
        Args:
            place_id (str): The ID of the place being reviewed.
            user_id (str): The ID of the user writing the review.
            text (str): The text content of the review.
            rating (int): The rating of the review.
        """

    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String, nullable=True)
    place_id = db.Column(db.Integer, db.ForeignKey('places.id'), nullable=False)

    @property
    def place_id(self):
        """
        Get the place_id of the review.
        
        Returns:
            str: The ID of the place being reviewed.
        """
        return self._place_id

    @place_id.setter
    def place_id(self, value):
        """
        Set the place_id of the review.
        
        Args:
            value (str): The new place_id.
        
        Raises:
            TypeError: If value is not a non-empty string.
        """
        if value is None or not isinstance(value, str):
            raise TypeError('place_id must be a non-empty string')
        self._place_id= value

    @property
    def user_id(self):
        """
        Get the user_id of the review.
        
        Returns:
            str: The ID of the user writing the review.
        """
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        """
        Set the user_id of the review.
        
        Args:
            value (str): The new user_id.
        
        Raises:
            TypeError: If value is not a non-empty string.
        """
        if value is None or not isinstance(value, str):
            raise TypeError('user_id must be a non-empty string')
        self._user_id = value

    @property
    def text(self):
        """
        Get the text content of the review.
        
        Returns:
            str: The text content of the review.
        """
        return self._text

    @text.setter
    def text(self, value):
        """
        Set the text content of the review.
        
        Args:
            value (str): The new text content.
        
        Raises:
            TypeError: If value is not a non-empty string.
        """
        if value is None or not isinstance(value, str):
            raise TypeError('text must be a non-empty string')
        self._text = value

    @property
    def rating(self):
        """
        Get the rating of the review.
        
        Returns:
            int: The rating of the review.
        """
        return self._rating

    @rating.setter
    def rating(self, value):
        """
        Set the rating of the review.
        
        Args:
            value (int): The new rating.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not between 0 and 5.
        """
        if value is None or not isinstance(value, int):
            raise TypeError('rating must be an integer')
        if value < 0 or value > 5:
            raise ValueError('rating must be between 0 and 5')
        self._rating = value
        
    def validate(self):
        
        if self._rating is None or not isinstance(self._rating, int):
            raise TypeError('rating must be an integer')
        if self._rating < 0 or self._rating > 5:
            raise ValueError('rating must be between 0 and 5')
        
        if self._text == "" or not isinstance(self._text, str):
            raise TypeError('text must be a non-empty string')
        
        if self._user_id == "" or not isinstance(self._user_id, str):
            raise TypeError('user_id must be a non-empty string')
        
        if self._place_id == "" or not isinstance(self._place_id, str):
            raise TypeError('place_id must be a non-empty string')
        
        return