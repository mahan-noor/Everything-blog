from flask_login import UserMixin
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    comment = db.relationship('Comment',backref = 'role',lazy="dynamic")



    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)




    def __repr__(self):
        return f'User {self.username}'



class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'



class Post(db.Model): 

    __tablename__ ='posts'

    id = db.Column(db.Integer, primary_key = True)
    post_title = db.Column(db.String)
    post_content = db.Column(db.Text)
    posted_at = db.Column(db.Date)
    post_by =db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship("Comment",backref ="post", lazy="dynamic")

    def save_post(self):
        db.session.add(self)
        db.session.commit()



    def delete_post(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_user_posts(cls,id):
        post = Post.query.filter_by(user_id= id).order_by(Post.posted_at.desc().all)
        return posts

    @classmethod
    def get_post(cls,id):
        return Post.query.filter_by(id)







class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False)
    post_id =db.Column(db.Integer,db.ForeignKey('posts.id'))
    comment = db.Column(db.Text(),nullable = False)
    posted=db.Column(db.DateTime,default=datetime.utcnow)
    comment_by = db.Column(db.String)



    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def delete_comment(cls,id):
        gone =Comment.query.filter_by(id = id).first()
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def clear_comments(cls):
        commennts = Comment.query.filter_by(post_id =id).all()
        return comments


    @classmethod
    def get_comments(cls,id):
        commennts = Comment.query.filter_by(post_id =id).all()
        return comments
    

    
class Quote:
    """
    Quote class to define quote objects
    """

    def __init__(self,author,id,quote,permalink):
        self.author = author
        self.id = id
        self.quote = quote
        self.permalink = permalink


