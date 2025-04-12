from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.services.facade import HBnBFacade

api = Namespace('places', description='Place operations')

facade = HBnBFacade()

# Models
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'amenities': fields.List(fields.String, required=True, description="List of amenities IDs")
})

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def post(self):
        """Register a new place"""
        current_user = get_jwt_identity()
        place_data = api.payload

        if not place_data:
            return {'message': 'Invalid input data'}, 400

        # Suppression de clés potentiellement présentes
        place_data.pop('owner_id', None)
        place_data.pop('user', None)

        # Récupération des amenities sous forme d'objets
        amenity_ids = place_data.pop('amenities', [])
        amenities = [facade.get_amenity(amenity_id) for amenity_id in amenity_ids if facade.get_amenity(amenity_id) is not None]
        place_data['amenities'] = amenities

        # Associer le propriétaire
        place_data['owner_id'] = current_user

        try:
            new_place = facade.create_place(place_data)
            new_place.validate()
        except (TypeError, ValueError) as e:
            return {'error': str(e)}, 400

        return self.serialize_place(new_place), 201

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        places = facade.get_all_places()
        return {'places': [self.serialize_place(place) for place in places]}, 200

    def serialize_place(self, place):
        return {
            "id": place.id,
            "title": place.title,
            "description": place.description,
            "price": place.price,
            "latitude": place.latitude,
            "longitude": place.longitude,
            "owner": {
                "id": place.user.id if place.user else None,
                "first_name": place.user.first_name if place.user else "",
                "last_name": place.user.last_name if place.user else ""
            },
            "amenities": [amenity.id for amenity in place.amenities]
            # Dans la vue liste, on n'inclut pas les reviews.
        }

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    @jwt_required()
    def get(self, place_id):
        """Get place details by ID"""
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404
        return self.serialize_place(place), 200

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    @api.response(403, 'Unauthorized action')
    @jwt_required()
    def put(self, place_id):
        """Update a place's information"""
        place_data = api.payload
        if not place_data:
            return {'error': 'Invalid input data'}, 400

        current_user = get_jwt_identity()  # current_user est une chaîne
        place = facade.get_place(place_id)
        if not place:
            return {'message': 'Place not found'}, 404

        # Pour accéder aux autres claims, on utilise get_jwt()
        claims = get_jwt()
        user_id = current_user  # already a string
        admin = claims.get('is_admin', False)

        if place.owner_id != user_id and not admin:
            return {'error': 'Unauthorized action'}, 403

        # Convertir les amenities
        amenity_ids = place_data.pop('amenities', [])
        amenities = [facade.get_amenity(amenity_id) for amenity_id in amenity_ids if facade.get_amenity(amenity_id) is not None]
        place_data['amenities'] = amenities

        updated_place = facade.update_place(place_id, place_data)
        return self.serialize_place(updated_place), 200

    def serialize_place(self, place):
        return {
            "id": place.id,
            "title": place.title,
            "description": place.description,
            "price": place.price,
            "latitude": place.latitude,
            "longitude": place.longitude,
            "owner": {
                "id": place.user.id if place.user else None,
                "first_name": place.user.first_name if place.user else "",
                "last_name": place.user.last_name if place.user else ""
            },
            "amenities": [amenity.id for amenity in place.amenities],
            "reviews": [
                {
                    "id": review.id,
                    "text": review.text,
                    "rating": review.rating,
                    "user_id": review.user_id,
                    "place_id": review.place_id
                } for review in place.reviews
            ]
        }
