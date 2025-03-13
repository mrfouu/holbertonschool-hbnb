#!/usr/bin/python3

from .base_model import BaseModel
import re
from app import db, bcrypt  # Importer l'instance Bcrypt initialisée


class User(BaseModel):
    __tablename__ = 'users'

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if value is None or not isinstance(value, str):
            raise TypeError('first_name must be a non-empty string')
        if not value or len(value) > 50:
            raise ValueError(
                'first_name must be non-empty and 50 characters or less')
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if value is None or not isinstance(value, str):
            raise TypeError('last_name must be a non-empty string')
        if not value or len(value) > 50:
            raise ValueError(
                'last_name must be non-empty and 50 characters or less')
        self._last_name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if value is None or not isinstance(value, str):
            raise TypeError('email must be a non-empty string')
        if not re.fullmatch(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
                            value):
            raise ValueError('please enter a valid email address')
        self._email = value

    @property
    def is_admin(self):
        return self._is_admin

    @is_admin.setter
    def is_admin(self, value):
        if not isinstance(value, bool):
            raise TypeError('user must be an admin')
        self._is_admin = value

    def hash_password(self, password):
        """Hache le mot de passe avant de le stocker."""
        self._password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Vérifie si le mot de passe en clair correspond au hachage."""
        if not self._password:
            raise ValueError('Password is not set')
        if not password:
            raise ValueError('Password is empty')
        return bcrypt.check_password_hash(self._password, password)

    def to_dict(self):
        """Convertit l'utilisateur en dictionnaire sans inclure le mot de passe."""
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'is_admin': self.is_admin,
        }

    def validate(self):
        if self._first_name is None or not isinstance(self._first_name, str):
            raise TypeError('first_name must be a non-empty string')
        if not self._first_name or len(self._first_name) > 50:
            raise ValueError(
                'first_name must be non-empty and 50 characters or less')

        if self._last_name is None or not isinstance(self._last_name, str):
            raise TypeError('last_name must be a non-empty string')
        if not self._last_name or len(self._last_name) > 50:
            raise ValueError(
                'last_name must be non-empty and 50 characters or less')
            
        if self._email is None or not isinstance(self._email, str):
            raise TypeError('email must be a non-empty string')
        if not re.fullmatch(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
                            self._email):
            raise ValueError('please enter a valid email address')
        
        if not isinstance(self._is_admin, bool):
            raise TypeError('user must be an admin')
