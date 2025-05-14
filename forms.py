from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, InputRequired, Optional, NumberRange, URL

class AddPetForm(FlaskForm):
    """Form for adding a new pet."""
    
    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[('select', 'Select'),('dog', 'Dog'), ('cat', 'Cat'), ('hamster', 'Hamster'), ('parrot', 'Parrot'), ('porcupine', 'Porcupine')], validators=[InputRequired()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30, message="Age must be a positive number")])
    notes = StringField("Notes")
    photo_url = StringField("Photo URL", validators=[Optional(), URL(message="Invalid URL")])
    

class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""
    
    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[('dog', 'Dog'), ('cat', 'Cat'), ('hamster', 'Hamster'), ('parrot', 'Parrot'), ('porcupine', 'Porcupine')], validators=[InputRequired()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30, message="Age must be a positive number")])
    notes = StringField("Notes")
    available = BooleanField("Available for Adoption")
    photo_url = StringField("Photo URL", validators=[Optional(), URL(message="Invalid URL")])