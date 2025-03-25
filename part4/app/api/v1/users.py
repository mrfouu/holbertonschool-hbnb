from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.services import facade
from flask import jsonify
import json

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
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new user"""
        
        user_data = api.payload
    
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400
        
        try:
            new_user = facade.create_user(user_data)
            new_user.validate()
        except (TypeError, ValueError) as e:
            return {'error': str(e)}, 400

        return {
                'id': new_user.id,
                'first_name': new_user.first_name,
                'last_name': new_user.last_name,
                'email': new_user.email
            }, 201
        
    @api.response(200, 'List of users retrieved successfully')
    @jwt_required()
    def get(self):
        """Retrieve a list of all users"""
        users = facade.get_all_users()
        return {'users': [user.to_dict() for user in users]}, 200


@api.route('/<user_id>')
class UserResource(Resource):
    @jwt_required()
    @api.response(200, 'User details retrieved successfully', model=user_response_model)
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        
        user = facade.get_user_by_id(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        
        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }, 200
        
    @jwt_required()
    @api.expect(user_model, validate=True)
    @api.response(200, 'User details updated successfully')
    @api.response(400, 'Invalid input data')
    @api.response(404, 'User not found')
    def put(self, user_id):
        """Update user details by ID"""
        
        current_user = get_jwt_identity()

        user_data = api.payload
        
        user = facade.get_user_by_id(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        
        if not current_user.get('is_admin') and current_user.get('id') != user.id:
            return {'error': 'Admin privileges required'}, 403
        
        updated_user = facade.update_user(user_id, user_data)
        updated_user.validate()
        
        return {
            'id': updated_user.id,
            'first_name': updated_user.first_name,
            'last_name': updated_user.last_name,
            'email': updated_user.email
        }, 200
