from app.models.base_model import BaseModel
from app import db, bcrypt


class Amenity(BaseModel):
    __tablename__ = 'amenities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String, nullable=True)

    def validate(self):
        if not self.name: 
            raise ValueError("Amenity name must not be empty")
        elif len(self.name) > 50:
            raise ValueError("Amenity name must be <= 50 characters..")
