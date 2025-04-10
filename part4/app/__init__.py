from flask import Flask
from flask_restx import Api
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

jwt = JWTManager()
bcrypt = Bcrypt()
db = SQLAlchemy()

from app.api.v1.auth import api as auth_ns
from app.api.v1.users import api as users_ns
from app.api.v1.places import api as places_ns
from app.api.v1.reviews import api as reviews_ns
from app.api.v1.amenities import api as amenities_ns

def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.url_map.strict_slashes = False

    # Active Flask-CORS globalement pour toutes les routes
    CORS(app)

    authorizations = {
        'BearerAuth': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization',
            'description': 'Type in the *"Value"* input box below: **"Bearer <JWT>"**, where JWT is the token',
        }
    }

    api = Api(
        app,
        version='1.0',
        title='HBnB API',
        authorizations=authorizations,
        description='HBnB Application API',
        doc='/',
        security='BearerAuth'
    )

    # Ajout des namespaces
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(auth_ns, path='/api/v1/auth')
    api.add_namespace(places_ns, path='/api/v1/places')
    api.add_namespace(reviews_ns, path='/api/v1/reviews')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')

    # Initialiser les extensions
    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

    # Ajout explicite des en-têtes CORS sur chaque réponse
    @app.after_request
    def after_request(response):
        # Nous définissons explicitement l'origine pour éviter le doublon
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8000'
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
        response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
        return response

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
