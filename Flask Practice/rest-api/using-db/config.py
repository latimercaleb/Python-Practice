import os 
from flask_restful import Api
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'no_secrets_today'
app.config['JWT_SECRET_KEY'] = 'super-secret'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///' + os.path.join(base_dir, 'api-datasource.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

api = Api(app)
db = SQLAlchemy(app)
Migrate(app,db) 
