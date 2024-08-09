from flask import render_template, flash, redirect, url_for, request, current_app as app
from flask_login import current_user, login_user, logout_user, login_required, LoginManager
from starwars_blog import db
from starwars_blog.models import User, Post, Comment
from urllib.parse import urlparse as url_parse



@app.route('/')
@app.route('/index')
def index():
    posts = Post.query.all()
    return render_template('index.html', title='Home', posts=posts)

@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == "POST":
        login_input = request.form["username"]
        password = request.form["password"]
        user = User.query.filter(
            (User.username == login_input) | (User.email == login_input)
        ).first()
        if user is None or not user.check_password(password):
            flash("Invalid username or password")
            return redirect(url_for('login'))
        login_user(user, remember=request.form.get("remember_me"))
    return render_template('login.html', title='Sign In')
        