from datetime import datetime, date
from config import db, ma


class Person(db.Model):
    __tablename__ = 'person'
    person_id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50), default='')
    email = db.Column(db.String(50), unique=True, index=True)
    timestamp = db.Column(db.DateTime,
                          default=date.today,
                          onupdate=date.today)
    
    def __init__(self, fname, email):
        self.fname = fname
        self.email = email


class PersonSchema(ma.Schema):
    class Meta:
        fields = ('fname', 'email', 'timestamp')
        model = Person
        

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.Integer)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    admin = db.Column(db.Boolean)