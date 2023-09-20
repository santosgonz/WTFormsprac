from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Pet
from pet import create_pet_field, edit_pet_field

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secretlmao123123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

## Initial Home page route
@app.route('/')
def home ():
    pet = Pet.query.all()
    return render_template('home.html', pet = pet)

## Add pets to our route
@app.route('/add', methods = ["GET", "POST"])
def add_pet():
    ## create form object from create_pet_field in pet.py
    # print (request.form)
    form = create_pet_field()
    ## What the form below is validating from pet.py
        ##     Pet(name="", species="", photo_url = "", age = NUM, notes = "", available = BOOLEAN)
    if form.validate_on_submit():
        name = form.pet_name.data
        species = form.species.data
        age = form.age.data
        photo_url = form.photo_url.data
        notes = form.notes.data
        pet = Pet(name=name, species=species, photo_url = photo_url, age = age, 
                  notes = notes)
        ##Adding available to another Edit route
        db.session.add(pet)
        db.session.commit()
        flash(f"New {species} added. Their name is {name}. {name} is {age} years old")
        return redirect('/')
    else:
        return render_template("add_pet.html", form=form)
 
 ##Edit pets in our route
@app.route("/edit/<int:pet_id>", methods = ["GET", "POST"])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    pets = Pet.query.all()
    form = edit_pet_field(obj=pet)
    if form.validate_on_submit():
        pet.species = form.species.data
        pet.age = form.age.data
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect('/')

    return render_template("edit_pet.html", pet=pet, pets=pets, form=form)