from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.models import User, Post, Comment
from werkzeug.urls import url_parse


@app.route("/")
@app.route("/index")
def index():
    posts = Post.query.all()
    return render_template("index.html", )

