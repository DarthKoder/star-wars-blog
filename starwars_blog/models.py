from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from starwars_blog import db, login


# This is the class that is for the user to create an account and create and index on the database storing the credentials
class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True, nullable=False)
    email = db.Column(db.String(100), index=True, unique=True, nullable=True)
    password_hash = db.Column(db.String(255))
    posts = db.relationship('Post', backref='author', lazy=True)  # Relationship to Post

    def set_password(self, password):
        # This is to set the user's password hash
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        # This will check if the provided password matches the stored password hash
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'
    
    
# This will load the user by their user ID
@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# This class is for the post creation layout
class Post (db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    film_name = db.Column(db.String(50), nullable=True)
    film_num = db.Column(db.Integer, nullable=True)
    year_of_release = db.Column(db.Integer, nullable=True)
    favourite_character = db.Column(db.String(100), nullable=True)
    user = db.relationship('User', backref=db.backref('posts', lazy=True))
    comments = db.relationship('Comment', backref='post', cascade="all, delete-orphan")
    
    @property
    def user(self):
        return User.query.get(self.user_id)
    

# This class is for the comment creation layout
class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id", ondelete='CASCADE'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", backref="comments")
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)