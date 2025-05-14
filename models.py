from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Optional

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "/static/assets/images/WTForms.png"

# Function to connect to the database
def connect_db(app):
    """Connect the database to the Flask app."""
    db.app = app
    db.init_app(app)



# ----------- #
#   Models
# ----------- #

class Pet(db.Model):
    """Pet model."""
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean, default=True)
    photo_url = db.Column(db.String, nullable=True)

    def image_url(self):
        """Return a default image URL if no photo URL is provided."""
        return self.photo_url or DEFAULT_IMAGE_URL

    def __repr__(self):
        return f'<Pet {self.name}>'
    
    @classmethod
    def get_all_pets(cls):
        """Return all pets."""
        return cls.query.all()