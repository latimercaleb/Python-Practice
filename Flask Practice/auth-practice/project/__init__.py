import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Config
login_manager = LoginManager()
base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///' + os.path.join(base_dir, 'recruitment-data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SECRET_KEY'] = 'no_secrets_here'

db = SQLAlchemy(app)
Migrate(app,db)

login_manager.init_app(app)
login_manager.login_view = 'login'
