from app import create_app
from flask_cors import CORS

app = create_app()
app.url_map.strict_slashes = False
CORS(app, supports_credentials=True)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:8000"}})

if __name__ == '__main__':
    app.run(debug=False)