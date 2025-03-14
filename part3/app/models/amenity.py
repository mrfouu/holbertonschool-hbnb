from app.models.base_model import BaseModel
from app import db
import uuid

# Table d'association pour la relation Many-to-Many
place_amenity = db.Table('place_amenity',
    db.Column('place_id', db.Integer, db.ForeignKey('places.id'), primary_key=True),
    db.Column('amenity_id', db.Integer, db.ForeignKey('amenities.id'), primary_key=True)
)

class Amenity(BaseModel):
    __tablename__ = 'amenities'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(50), nullable=False)

    # Relation Many-to-Many avec Place
    places = db.relationship('Place', secondary=place_amenity, backref='amenities', lazy=True)

    def validate(self):
        if not self.name:
            raise ValueError("Amenity name must not be empty")
        elif len(self.name) > 50:
            raise ValueError("Amenity name must be <= 50 characters")