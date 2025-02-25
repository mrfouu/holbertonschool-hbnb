#!/usr/bin/python3

from app.models.base_model import BaseModel
from app.models.place import Place
import uuid
from datetime import datetime
import re


class Review(BaseModel):
    def __init__(self, place_id, user_id, text):
        self.place_id = place_id
        self.user_id = user_id
        self.text = text
        self.rating = rating

    @property
    def place_id(self):
        return self.place_id

    @place_id.setter
    def place_id(self, value):
        if value is None or not isinstance(value, str):
            raise TypeError('place_id must be a non-empty string')
        self.place_id = value

    @property
    def user_id(self):
        return self.user_id

    @user_id.setter
    def user_id(self, value):
        if value is None or not isinstance(value, str):
            raise TypeError('user_id must be a non-empty string')
        self.user_id = value

    @property
    def text(self):
        return self.text

    @text.setter
    def text(self, value):
        if value is None or not isinstance(value, str):
            raise TypeError('text must be a non-empty string')
        self.text = value

    @property
    def rating(self):
        return self.rating

    @rating.setter
    def rating(self, value):
        if value is None or not isinstance(value, int):
            raise TypeError('rating must be an integer')
        if value < 0 or value > 5:
            raise ValueError('rating must be between 0 and 5')
        self.rating = value
