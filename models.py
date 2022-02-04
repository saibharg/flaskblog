from blog import db, login_manager
import datetime
from flask_login import LoginManager,UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    id=db.Column(db.Integer(),primary_key=True)
    username=db.Column(db.String(50),nullable=False,unique=True)
    email_address=db.Column(db.String(120),nullable=False,unique=True)
    password= db.Column(db.String(1000),nullable=False)
    post = db.relationship('Post',backref='post',lazy=True)
    comment = db.relationship('Comment',backref='author',lazy=True)

class Post(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    title = db.Column(db.String(100),nullable=False,unique=True)
    timestamp = db.Column(db.DateTime(),default=datetime.datetime.now())
    content = db.Column(db.Text(length=1000),nullable=False)
    user_id = db.Column(db.Integer(),db.ForeignKey('user.id'),nullable=False)
    comment = db.relationship('Comment',backref='post',lazy=True)

class Comment(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    comment = db.Column(db.String(100),nullable=False,unique=False)
    post_id = db.Column(db.Integer(),db.ForeignKey('post.id'),nullable=False)
    author_id = db.Column(db.String(500),db.ForeignKey('user.username'),nullable=False)
    timestamp = db.Column(db.DateTime(), index=True, default=datetime.datetime.utcnow)
    

    

    