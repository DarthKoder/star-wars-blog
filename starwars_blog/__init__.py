import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Create instances of extensions
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()

def create_app():
    app = Flask(__name__)

    # Load environment variables if env.py exists
    if os.path.exists("env.py"):
        import env

    # Set the secret key for session management
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

    # Database URI configuration
    if os.environ.get("DEVELOPMENT") == "True":
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
    else:
        uri = os.environ.get("DATABASE_URL")
        if uri and uri.startswith("postgres://"):
            uri = uri.replace("postgres://", "postgresql://", 1)
        app.config["SQLALCHEMY_DATABASE_URI"] = uri

    # Initialize extensions with the app instance
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    login.login_view = 'login'

    # Import routes and models to ensure they are registered with the app
    with app.app_context():
        from starwars_blog import routes, models

    return app
