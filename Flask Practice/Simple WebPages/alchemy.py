# Getting started with sql-Alc
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# Setup 
base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///' + os.path.join(base_dir, 'raider-data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)
# Migrate(app,db) Fix locally, need path adjustments

# Initial Model
class Raider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job = db.Column(db.Text)
    name = db.Column(db.Text)
    level = db.Column(db.Integer)
    guild_id = db.Column(db.Integer, db.ForeignKey('squadron.id'))

    def __init__(self, job, name, level, guild_id): #Todo finish this constuctor
        self.job = job
        self.level = level

    def __repr__(self): 
        return f"Job is {self.job} with level {self.level}"
    

class Guild(db.Model):
    __tablename__='squadron'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    raider_count = db.Column(db.Integer)
    # One to many
    # One guild to many X
    guild_member = db.relationship('Raider', backref='Guild', lazy='dynamic') # Review documentation
    # One to one
    # One guild to one master
    guild_master = db.relationship('Master', backref='Guild', useList=False)

    def __init__(self, name, raider_count):
        self.name = name
        self.raider_count = raider_count

    def __repr__(self): 
        # TODO: Add logic to seperate return by if guild has a master or not, start with this tmrw
        return f"Guild is {self.name} with a member count of {self.raider_count}"
    
    def show_member_names(self):
        print ('The members of {self.name} are: ')
        for member in self.guild_member:
            print (member.name)
    

class Master(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    level = db.Column(db.Integer)
    guild_id = db.Column(db.Integer, db.ForeignKey('squadron.id'))

    def __init__(self, name, guild_id): # TODO: Adjust this
        self.name = name
        self.raider_count = raider_count
    pass

class Uhh2(db.Model):
    pass