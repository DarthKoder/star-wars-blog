from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from starwars_blog import db, login


# This is the class that is for the user to create an account and create and index on the database storing the credentials
class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True,)
    email = db.Column(db.String(100), index=True, unique=True, nullable=True)
    password_hash = db.Column(db.String(50))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    
@login.user_loader(id)
def load_user(id):
    return User.query.get(int(id))


class Post (db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    film_name = db.Column(db.String(50), nullable=True)
    film_num = db.Column(db.Integer, nullable=True)
    year_of_release = db.Column(db.Integer, nullable=True)
    favourite_character = db.Column(db.String(100), nullable=True)
    
    
class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))