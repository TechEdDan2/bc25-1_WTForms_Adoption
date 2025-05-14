"""Seed file to make sample data for database."""

from models import db, Pet
from app import app

# Create all tables
with app.app_context():
    db.drop_all()
    db.create_all()

# If the table already exists, delete all records
Pet.query.delete()

# Sample pets
pet1 = Pet(
    name='Fluffy',
    species='Porcupine',
    age=3,
    notes='Friendly and playful.',
    available=True,
    photo_url= '/static/assets/images/porcupine.png'
)

pet2 = Pet(
    name='Sparky',
    species='Dog',
    age=5,
    notes='Loves to fetch and play.',
    available=True
)

pet3 = Pet(
    name='Gus',
    species='Dog',
    age=7,
    notes='Cuddly and affectionate. A Good Doggie.',
    available=True,
    photo_url='/static/assets/images/jadon-barnes-AWJ-FbEvO1M-unsplash.jpg'
)

# Photo by <a href="https://unsplash.com/@jadonbarnes?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Jadon Barnes</a> on <a href="https://unsplash.com/photos/a-close-up-of-a-dog-looking-up-at-something-AWJ-FbEvO1M?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
      

# add new objects to the session
db.session.add_all([pet1, pet2])

# Commit the session to the database
db.session.commit()