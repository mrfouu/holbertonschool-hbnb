#!/usr/bin/python3

from app.models.base_model import BaseModel


class Review(BaseModel):
    def __init__(self, text, place, user, rating=None):
        """
        Initialize a new Review instance.
        
        Args:
            text (str): The text content of the review.
            place_id (str): The ID of the place being reviewed.
            user_id (str): The ID of the user writing the review.
            rating (int, optional): The rating of the review. Defaults to None.
        """
        self.text = text
        self.place = place
        self.user = user
        self.rating = rating

    @property
    def place_id(self):
        """
        Get the place_id of the review.
        
        Returns:
            str: The ID of the place being reviewed.
        """
        return self.place_id

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
        self.place_id = value

    @property
    def user_id(self):
        """
        Get the user_id of the review.
        
        Returns:
            str: The ID of the user writing the review.
        """
        return self.user_id

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
        self.user_id = value

    @property
    def text(self):
        """
        Get the text content of the review.
        
        Returns:
            str: The text content of the review.
        """
        return self .text

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
        self.text = value

    @property
    def rating(self):
        """
        Get the rating of the review.
        
        Returns:
            int: The rating of the review.
        """
        return self.rating

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
        self.rating = value
