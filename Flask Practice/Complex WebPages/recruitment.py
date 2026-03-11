import os 
# from forms import RecruitForm, ResignFOrm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Config
base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///' + os.path.join(base_dir, 'recruitment-data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SECRET_KEY'] = 'no_secrets_here'

db = SQLAlchemy(app)
Migrate(app,db) 

# Model
class Hero(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    title = db.Column(db.Text)

    
    def __init__(self, name, title):
        self.name = name
        self.title = title

    def __repr__(self): 
        # TODO Decide string representation for this
        pass

# Controller
@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/recruit', methods=['GET', 'POST'])
def recruit(): 
    recruit = AddForm()
    if recruit.validate_on_submit():
        # Extract fields if valid
        # Do database action
        return redirect(url_for('roster'))
    return render_template('recruit.html', recruitment_form = recruit)

@app.route('/roster')
def list_roster(): 
    hero_roster = Hero.query.all()
    return render_template('roster.html', heroes = hero_roster)

@app.route('/resign', methods=['GET', 'POST'])
def remove_hero(): 
    resign = RemoveForm()
    if resign.validate_on_submit():
        # Extract fields if valid
        # Do database action
        return redirect(url_for('roster'))
    return render_template('resign.html', resignation_form = resign)