import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Load environment variables if env.py exists
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

# Set the secret key for session management
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

# Database URI config
if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri and uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Initialize Flask-Login
login = LoginManager(app)
login.login_view = 'login'

# Import routes and models
from starwars_blog import routes, models