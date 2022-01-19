from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Forumpost(db.Model):
    id = id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    username = db.Column(db.String(100))
    posts = db.relationship('Forumpost')