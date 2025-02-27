#!/usr/bin/python3

from .base_model import BaseModel
from .place import Place
import uuid
from datetime import datetime
import re


class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        self.firstname = first_name
        self.lastname = last_name
        self.email = email
        self.is_admin = is_admin

    @property
    def first_name(self):
        return self.first_name

    @first_name.setter
    def first_name(self, value):
        if value is None or not isinstance(value, str):
            raise TypeError('first_name must be a non-empty string')
        if not value or len(value) > 50:
            raise ValueError(
                'first_name must be non-empty and 50 characters or less')
        self.first_name = value

    @property
    def last_name(self):
        return self.last_name

    @last_name.setter
    def last_name(self, value):
        if value is None or not isinstance(value, str):
            raise TypeError('last_name must be a non-empty string')
        if not value or len(value) > 50:
            raise ValueError(
                'last_name must be non-empty and 50 characters or less')
        self.last_name = value

    @property
    def email(self):
        return self.email

    @email.setter
    def email(self, value):
        if value is None or not isinstance(value, str):
            raise TypeError('email must be a non-empty string')
        if not re.fullmatch(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$',
                            self.email):
            raise ValueError('please enter a valid email address')
        self.email = value

    @property
    def is_admin(self):
        return self.is_admin

    @is_admin.setter
    def is_admin(self, value):
        if not isinstance(value, bool):
            raise TypeError('user must be an admin')
        self.is_admin = value

    def add_place(self, place):
        """Add a place to the user's list of places"""
        if not isinstance(place, Place):
            raise TypeError('place must be an instance of the Place class')
        self.places.append(place)