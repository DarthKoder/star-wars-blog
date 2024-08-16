from flask import render_template, flash, redirect, url_for, request, current_app as app
from flask_login import current_user, login_user, logout_user, login_required, LoginManager
from starwars_blog import db
from starwars_blog.models import User, Post, Comment
from urllib.parse import urlparse as url_parse


# Main homepage
@app.route('/')
@app.route('/index')
def index():
    posts = Post.query.all()
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
        post = Post(title=title, body=body, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        flash("Your post is now live!")
        return redirect(url_for('index'))
    return render_template('create_post.html', title='Create Post')


@app.route('/post/<int:post_id>', methods=["GET", "POST"])
def post(post_id):
    post=Post.query.get_or_404(post_id)
    if request.method == "POST":
        body = request.form["body"]
        comment = Comment(body=body, post_id=post.id, user_id=current_user.id)
        db.session.add(comment)
        db.session.commit()
        flash("Your comment has been added.")
        return redirect(url_for('post', post_id=post_id))
    comments = Comment.query.filter_by(post_id=post_id).all()
    return render_template('post.html', title=post.title, post=post, comments=comments)


@app.route('/post/edit/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    
    # Only the author can edit the post
    if post.user_id != current_user.id:
        flash('You cannot edit this post.')
        return redirect(url_for('index'))

    if request.method == 'POST':
        post.title = request.form['title']
        post.body = request.form['body']
        db.session.commit()
        flash('Your post has been updated.')
        return redirect(url_for('post', post_id=post.id))

    return render_template('edit_post.html', title='Edit Post', post=post)