from app.models.base_model import BaseModel
from app import db
import uuid

class Review(BaseModel):

    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String, nullable=True)
    place_id = db.Column(db.Integer, db.ForeignKey('places.id'), nullable=False)  # Clé étrangère vers Place
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)  # Clé étrangère vers User

    # Relations
    user = db.relationship('User', backref='reviews')  # Relation avec User
    place = db.relationship('Place', backref='reviews')  # Relation avec Place

    @property
    def place_id(self):
        return self._place_id

    @place_id.setter
    def place_id(self, value):
        if value is None or not isinstance(value, str):
            raise TypeError('place_id must be a non-empty string')
        self._place_id = value

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        if value is None or not isinstance(value, str):
            raise TypeError('user_id must be a non-empty string')
        self._user_id = value

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if value is None or not isinstance(value, str):
            raise TypeError('text must be a non-empty string')
        self._text = value

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
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
