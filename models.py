from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)
    

class Pet(db.Model):
    __tablename__ = 'pets'
    id = db.Column(db.Integer,
                   primary_key = True,
                   autoincrement = True)
    name = db.Column(db.String(25),
                           nullable = False)
    species = db.Column(db.String(50),
                          nullable = False)
    photo_url = db.Column(db.String)
    age = db.Column(db.Integer,
                           nullable = True)
    notes = db.Column(db.String,
                          nullable = True)
    available = db.Column(db.Boolean, 
                          nullable=False, 
                          default=True)
    
    # Pet(name="", species="", photo_url = "", age = NUM, notes = "", available = BOOLEAN)



    # def __repr__(self):
    #     return f"<User(id={self.id}, first_name='{self.first_name}', last_name='{self.last_name}', image_url='{self.image_url}')>"

def connect_db(app):
    db.app = app
    db.init_app(app)