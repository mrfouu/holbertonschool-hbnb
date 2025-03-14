from app.models.base_model import BaseModel
from app import db
import uuid


class Amenity(BaseModel):
    __tablename__ = 'amenities'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(50), nullable=False)

    def validate(self):
        if not self.name: 
            raise ValueError("Amenity name must not be empty")
        elif len(self.name) > 50:
            raise ValueError("Amenity name must be <= 50 characters..")
