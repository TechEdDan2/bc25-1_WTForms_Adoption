"""
app.py

This is the main application file for the WTForms Adoption Agency project.
It initializes the Flask app, configures the database, and defines routes
for managing pets (viewing, adding, editing, and deleting).

Key Components:
- Flask app initialization and configuration
- Database connection setup
- Routes for CRUD operations on pets
"""
from flask import Flask, render_template, request, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, db, Pet

from forms import AddPetForm, EditPetForm
# ----------------- #

app = Flask(__name__)

# Flask configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption_db'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the Debug Toolbar
app.config['SECRET_KEY'] = 'passwordistaco123'
debug = DebugToolbarExtension(app)

# Initialize the database connection and create tables
with app.app_context():
    connect_db(app)
    db.create_all()


# ----------------- #
#   Routes
# ----------------- #
@app.route('/')
def home():
    """
    Render the home page.

    - Fetches all pets from the database.
    - Displays them in a card layout on the homepage.

    Returns:
        Rendered template for the home page.
    """
    pets = Pet.get_all_pets()
    return render_template('home.html', pets=pets)

@app.route('/pets/<int:pet_id>')
def pet_details(pet_id):
    """Render the pet details page."""
    pet = Pet.query.get_or_404(pet_id)
    return render_template('details.html', pet=pet)

@app.route('/pet/new', methods=['GET', 'POST'])
def add_pet():
    """
    Add a new pet to the database.

    - GET: Renders the form for adding a new pet.
    - POST: Validates the form and adds the pet to the database.

    Returns:
        - Redirects to the home page after successful submission.
        - Renders the add pet form if validation fails.
    """
    form = AddPetForm()

    if form.validate_on_submit():
        # Create a new pet instance
        name = request.form['name']
        species = request.form['species']
        age = request.form['age']
        notes = request.form['notes']
        photo_url = request.form['photo_url']

        new_pet = Pet(name=name, species=species, age=age, notes=notes, photo_url=photo_url)
        db.session.add(new_pet)
        db.session.commit()

        flash(f'Added {name} to the database!', 'success')
        return redirect('/')
    
    return render_template('add_pet_form.html', form=form)

@app.route('/pet/<int:pet_id>/edit', methods=['GET', 'POST'])
def edit_pet(pet_id):
    """
    Edit an existing pet's details.
    - GET: Renders the form pre-filled with the pet's current details.
    - POST: Updates the pet's details in the database.
    Args:
        pet_id (int): The ID of the pet to edit.
    Returns:
        - Redirects to the home page after successful update.
        - Renders the edit pet form if validation fails.
    """
    pet = Pet.query.get_or_404(pet_id)
    species_choices = [('dog', 'Dog'), ('cat', 'Cat'), ('hamster', 'Hamster'), ('parrot', 'Parrot'), ('porcupine', 'Porcupine')]

    form = EditPetForm(obj=pet)
    form.species.choices = species_choices
    form.available = pet.available

    if request.method == 'POST':
        pet.name = request.form['name']
        pet.species = request.form['species']
        pet.age = request.form['age']
        pet.notes = request.form['notes']
        pet.available = request.form.get('available') == 'on'
        pet.photo_url = request.form['photo_url']

        db.session.commit()

        flash(f'Updated {pet.name}!', 'success')
        return redirect('/')

    return render_template('edit_pet_form.html', pet=pet, form=form)

@app.route('/pet/<int:pet_id>/delete', methods=['POST'])
def delete_pet(pet_id):
    """Delete a pet."""
    pet = Pet.query.get_or_404(pet_id)
    db.session.delete(pet)
    db.session.commit()

    flash(f'Deleted {pet.name}!', 'success')
    return redirect('/')

