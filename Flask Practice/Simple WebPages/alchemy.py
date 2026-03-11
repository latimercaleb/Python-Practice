# Getting started with sql-Alc
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Setup 
base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///' + os.path.join(base_dir, 'raider-data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)
Migrate(app,db) # Fix locally, need path adjustments

# Main Unit
class Raider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job = db.Column(db.Text)
    name = db.Column(db.Text)
    level = db.Column(db.Integer)
    guild_id = db.Column(db.Integer, db.ForeignKey('squadron.id'))

    def __init__(self, job, name, level, guild_id):
        self.job = job
        self.name = name
        self.level = level
        self.guild_id = guild_id

    def __repr__(self): 
        return f"Job is {self.job} with level {self.level} for {self.name} at id {self.id}"
    
# Host unit, has many main units
class Guild(db.Model):
    __tablename__='squadron'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    raider_count = db.Column(db.Integer)
    # One to many
    # One guild to many X
    guild_member = db.relationship('Raider', backref='Guild', lazy='dynamic')
    # One to one
    # One guild to one master
    guild_master = db.relationship('Master', backref='Guild', uselist=False)

    def __init__(self, name, raider_count):
        self.name = name
        self.raider_count = raider_count

    def __repr__(self): 
        if self.raider_count > 0:
            return f"Guild is {self.name} with a member count of {self.raider_count}"
        else: 
            return f"Guild is {self.name} with no members under {self.guild_master}"
    
    def show_member_names(self):
        print ('The members of {self.name} are: ')
        for member in self.guild_member:
            print (member.name)
    

# One unit, has one host unit, is not a main unit
class Master(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    level = db.Column(db.Integer, default=999)
    guild_id = db.Column(db.Integer, db.ForeignKey('squadron.id'))

    def __init__(self, name, guild_id):
        self.name = name
        self.guild_id = guild_id