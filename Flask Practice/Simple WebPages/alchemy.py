# Getting started with sql-Alc
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Setup 
base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)
Migrate(app,db)
# Initial Model
class Raider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job = db.Column(db.Text)
    level = db.Column(db.Integer)

    def __init__(self, job, level):
        self.job = job
        self.level = level

    def __repr__(self): 
        return f"Job is {self.job} with level {self.level}"
