"""Models for Blogly."""

import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"

class User(db.Model):
    """ User """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.Text(30), nullable = False)
    last_name = db.Column(db.Text(30), nullable = False)
    image_url = db.Column(db.String, nullable = False, default= DEFAULT_IMAGE_URL)

    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"
    
def connect_db(app):
        """ Connect to Database """

        db.app = app
        db.init_app(app)

class Post(db.Model):
    """ Post """
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text, nullable = False)
    content = db.Column(db.Text, nullable = False)
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    @property
    def friendly_date(self):
        """ Return formated date """

        return self.created_at.striftime("%a %b %-d %Y, %-I:%M %p")

def connect_db(app):
    """ Connect to database """

    db.app = app
    db.init_app(app)