from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, Optional, NumberRange, URL

## Used to create and add pet into home page
class create_pet_field(FlaskForm):
    pet_name = StringField("Pet name")
    species = SelectField("Species", choices=[('porcupine', 'Porcupine'), ('cat', 'Cat'), ('dog', 'Dog')])
    photo_url = StringField("Photo URL", validators=[URL(), Optional()])
    age = IntegerField ("Age", validators=[NumberRange(min=0, max=30), Optional()])
    notes = StringField ("Notes")

## Used to edit pet and apply edit to home page
class edit_pet_field(FlaskForm):
    species = SelectField("Species", choices=[('porcupine', 'Porcupine'), ('cat', 'Cat'), ('dog', 'Dog')])
    photo_url = StringField("Photo URL", validators=[URL(), Optional()])
    age = IntegerField ("Age", validators=[NumberRange(min=0, max=30), Optional()])
    notes = StringField ("Notes")
    available = BooleanField("Is animal still available?")