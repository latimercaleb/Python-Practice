import os 
from forms import RecruitForm, ResignForm
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
        return f"{self.name} the {self.title}! Hero #{self.id}!"

# Controller
@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/recruit', methods=['GET', 'POST'])
def recruit(): 
    recruit = RecruitForm()
    if recruit.validate_on_submit():
        new_recruit = Hero(recruit.name.data, recruit.title.data)
        db.session.add(new_recruit)
        db.session.commit()
        return redirect(url_for('roster'))
    return render_template('recruit.html', recruitment_form = recruit)

@app.route('/resign', methods=['GET', 'POST'])
def remove_hero(): 
    resign = ResignForm()
    if resign.validate_on_submit():
        hero_id = resign.id.data
        Hero.query.filter_by(id=hero_id).delete()
        db.session.commit()
        return redirect(url_for('roster'))
    return render_template('resign.html', resignation_form = resign)

@app.route('/roster')
def list_roster(): 
    hero_roster = Hero.query.all()
    return render_template('roster.html', heroes = hero_roster)

if __name__ == '__main__':
    app.run(debug=True)