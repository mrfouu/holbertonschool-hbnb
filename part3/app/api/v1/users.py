from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import get_jwt_identity
from app.services import facade

api = Namespace('users', description='User related operations')

user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='Password for the user')
})

user_response_model = api.model('UserResponse', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the user'),
    'last_name': fields.String(description='Last name of the user'),
    'email': fields.String(description='Email of the user'),
})


@api.route('/')
class UserList(Resource):
    @api.expect(user_model)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new user"""
        user_data = api.payload
        try:
            # Extract password for hashing
            password = user_data.pop('password')
            new_user = facade.create_user(user_data, password)
            new_user.validate()
        except (TypeError, ValueError) as e:
            return {'error': str(e)}, 400

            new_user = facade.create_user(user_data)
            return {
                'id': new_user.id,
                'first_name': new_user.first_name,
                'last_name': new_user.last_name,
                'email': new_user.email
            }, 201
        except ValueError as e:
            return {'error': str(e)}, 400

    @api.response(200, 'List of users retrieved successfully')
    def get(self):
        """Retrieve a list of all users"""
        users = facade.get_all_users()
        return {'users': [user.to_dict() for user in users]}, 200


@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully', model=user_response_model)
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        try:
            updated_user = facade.update_user(user_id, user_data, password)
            updated_user.validate()
        except (TypeError, ValueError) as e:
            return {'error': str(e)}, 400

        if not updated_user:
            return {'error': 'User not found'}, 404

        return {
            'id': updated_user.id,
            'first_name': updated_user.first_name,
            'last_name': updated_user.last_name,
            'email': updated_user.email
        }, 200
