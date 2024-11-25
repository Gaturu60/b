# # app.py
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
# from flask_jwt_extended import JWTManager
# from flask_migrate import Migrate
# from routes.admin_routes import admin_bp
# from routes.user_routes import user_bp
# from models import db
# from flask_cors import CORS

# # Initialize extensions
# bcrypt = Bcrypt()
# jwt = JWTManager()
# migrate = Migrate()

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object('config.Config')  # Config from config.py

#     # Initialize extensions
#     db.init_app(app)
#     bcrypt.init_app(app)
#     jwt.init_app(app)
#     migrate.init_app(app, db)
#     CORS(app, supports_credentials=True)

#     # Register Blueprints
#     app.register_blueprint(admin_bp, url_prefix='/admin')
#     app.register_blueprint(user_bp, url_prefix='/user')

#     return app

# if __name__ == '__main__':
#     app = create_app()
#     app.run(debug=True)

# import os
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
# from flask_jwt_extended import JWTManager
# from flask_migrate import Migrate
# from flask_cors import CORS
# from routes.admin_routes import admin_bp
# from routes.user_routes import user_bp
# from models import db

# # Initialize extensions
# bcrypt = Bcrypt()
# jwt = JWTManager()
# migrate = Migrate()

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object('config.Config')  # Config from config.py

#     # Initialize extensions
#     db.init_app(app)
#     bcrypt.init_app(app)
#     jwt.init_app(app)
#     migrate.init_app(app, db)
#     CORS(app, supports_credentials=True)

#     # Define a default route for '/'
#     @app.route('/')
#     def home():
#         return "Welcome to the Flask App!"

#     # Register Blueprints
#     app.register_blueprint(admin_bp, url_prefix='/admin')
#     app.register_blueprint(user_bp, url_prefix='/user')

#     return app

# if __name__ == '__main__':
#     app = create_app()
#     # Use Render's PORT environment variable or default to 5000
#     port = int(os.environ.get("PORT", 5000))
#     # Bind to host '0.0.0.0' for Render deployment
#     app.run(host='0.0.0.0', port=port, debug=False)


import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_cors import CORS
from routes.admin_routes import admin_bp
from routes.user_routes import user_bp
from models import db

# Initialize extensions
bcrypt = Bcrypt()
jwt = JWTManager()
migrate = Migrate()

def create_app():
    # Initialize Flask app
    app = Flask(__name__)

    # Load configuration from environment variables (use .env file for local dev if needed)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///default.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')  # Make sure to set this in your environment variables
    app.config['CORS_HEADERS'] = 'Content-Type'

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    CORS(app, supports_credentials=True)

    # Define a default route for '/'
    @app.route('/')
    def home():
        return "Welcome to the Flask App!"

    # Register Blueprints
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(user_bp, url_prefix='/user')

    return app

if __name__ == '__main__':
    app = create_app()
    # Use Render's PORT environment variable or default to 5000
    port = int(os.environ.get("PORT", 5000))
    # Bind to host '0.0.0.0' for Render deployment
    app.run(host='0.0.0.0', port=port, debug=False)
