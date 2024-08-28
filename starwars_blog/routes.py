from flask import render_template, flash, redirect
from flask import url_for, request, current_app as app
from flask_login import current_user, login_user, logout_user
from flask_login import login_required, LoginManager
from starwars_blog import db
from starwars_blog.models import User, Post, Comment
from urllib.parse import urlparse as url_parse


# Main homepage
@app.route('/')
@app.route('/index')
def index():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('index.html', title='Home', posts=posts)


# Login function and requests with authentication
@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == "POST":
        login_input = request.form.get("login")
        password = request.form.get("password")
        remember_me = 'remember_me' in request.form
        user = User.query.filter(
            (User.username == login_input) | (User.email == login_input)
        ).first()

        if user is None or not user.check_password(password):
            flash("Invalid username or password")
            return redirect(url_for('login'))

        login_user(user, remember=remember_me)
        flash("You are now logged in")
        return redirect(url_for('index'))

    return render_template('login.html', title='Sign In')


# Logout dunction
@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
    return redirect(url_for('index'))


# Register function
@app.route('/register', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you are now a registered user!")
        return redirect(url_for('login'))
    return render_template('register.html', title='Register')


# New post function
@app.route('/post/new', methods=["GET", "POST"])
@login_required
def new_post():
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        film_name = request.form.get("film_name", "")
        film_num = request.form.get("film_num", "")
        year_of_release = request.form.get("year_of_release", "")
        favourite_character = request.form.get("favourite_character", "")

        post = Post(
            title=title,
            body=body,
            user_id=current_user.id,
            film_name=film_name,
            film_num=film_num,
            year_of_release=year_of_release,
            favourite_character=favourite_character
        )

        db.session.add(post)
        db.session.commit()
        flash("Your post is now live!")
        return redirect(url_for('index'))
    return render_template('create_post.html', title='Create Post')


@app.route('/post/<int:post_id>', methods=["GET", "POST"])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == "POST":
        body = request.form["body"]

        comment = Comment(body=body, post_id=post.id, user_id=current_user.id)

        db.session.add(comment)
        db.session.commit()
        flash("Your comment has been added.")
        return redirect(url_for('post', post_id=post_id))

    comments = Comment.query.filter_by(post_id=post_id).all()

    return render_template(
        'post.html',
        title=post.title,
        post=post,
        comments=comments)


@app.route('/post/edit/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)

    # Ensure only the post creator can edit
    if post.user_id != current_user.id:
        flash('You cannot edit this post.')
        return redirect(url_for('index'))

    if request.method == 'POST':
        post.title = request.form['title']
        post.body = request.form['body']
        post.film_name = request.form.get('film_name', "")
        post.film_num = request.form.get('film_num', "")
        post.year_of_release = request.form.get('year_of_release', "")
        post.favourite_character = request.form.get('favourite_character', "")

        db.session.commit()
        flash('Your post has been updated.')
        return redirect(url_for('post', post_id=post.id))

    return render_template('edit_post.html', title='Edit Post', post=post)


@app.route('/post/delete/<int:post_id>', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)

    # Only allow the user who created the post to delete it
    if post.user_id != current_user.id:
        flash('You cannot delete this post.')
        return redirect(url_for('index'))

    db.session.delete(post)
    db.session.commit()
    flash('Post has been deleted.')
    return redirect(url_for('index'))


@app.route('/comment/delete/<int:comment_id>', methods=['POST'])
@login_required
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)

    # Only allow the user who created the comment to delete it
    if comment.user_id != current_user.id:
        flash('You cannot delete this comment.')
        return redirect(url_for('post', post_id=comment.post_id))

    db.session.delete(comment)
    db.session.commit()
    flash('Comment has been deleted.')
    return redirect(url_for('post', post_id=comment.post_id))
