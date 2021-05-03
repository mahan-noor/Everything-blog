from flask import render_template,request,redirect,url_for,abort
from . import main
from ..request import get_quotes
from ..models import Comment,User,Post
from .forms import CommentForm,UpdateProfile,PostForm
from flask_login import login_required,current_user
import datetime
from .. import db,photos
import requests


# Views
@main.route('/')
def index():
    posts = Post.query.all()
    

    title = 'GZRU | Home'
    quotes = requests.get("http://quotes.stormconsultancy.co.uk/random.json").json()
    # random_quotes = get_quotes
    return render_template('index.html', title=title,posts=posts, quotes = quotes)

@main.route('/new_post/', methods = ['GET','POST'])
@login_required
def new_post():

    post_form = PostForm()
    if post_form.validate_on_submit():
        post_title = post_form.title.data
        post_content = post_form.blogpost.data

        new_post = Post(post_title = post_title,post_content = post_content, user_id = current_user.id)
        new_post.save_post()
        return redirect(url_for('main.index'))

    return render_template('new_post.html',post_form=post_form)

@main.route('/post/<int:id>', methods = ['GET','POST'])
def single_post(id):
    post = Post.query.filter_by(id=id).first()
    comments = Comment.query.filter_by(post_id=id).all()
    form = CommentForm()

    if form.validate_on_submit():
        comment = form.comment.data
        form.comment.data =''

        new_comment = Comment(comment=comment,post_id=post.id,user_id=current_user.id,comment_by=current_user.username)

        db.session.add(new_comment)
        db.session.commit()

        return redirect(url_for('main.single_post', id = post.id))


    return render_template('single_post.html', post=post, comments=comments, form=form)
