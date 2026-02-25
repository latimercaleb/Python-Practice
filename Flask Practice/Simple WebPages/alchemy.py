# Getting started with sql-Alc
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

base_dir = os.path.abspath(os.path.dirname(__file__))
print(base_dir)
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']=''
