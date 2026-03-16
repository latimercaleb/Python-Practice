import os 
from forms import RecruitForm, ResignForm, AcademyRegistrationForm
from flask import Flask, render_template, url_for, redirect, flash, session, get_flashed_messages
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
    # academy_key = db.Column(db.Integer, db.ForeignKey('academy.id'))
    academy = db.relationship("Academy", backref='hero', uselist=False)
    def __init__(self, name, title):
        self.name = name
        self.title = title
    
    def get_school(self): 
        return self.academy_key

    def __repr__(self):
        if self.academy:
            return f"{self.name} the {self.title}! Hero #{self.id}! From {self.academy.name}"
        else: 
            return f"{self.name} the {self.title}! Hero #{self.id}! A Freelance warrior"
    

class Academy(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'))

    def __init__(self, name, hero_id):
        self.name = name
        self.hero_id = hero_id
    
    def __repr__(self):
        return f"{self.name}"
    
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
        flash(f"New recruit: {new_recruit.name} added to roster!")
        session['new_recruit'] = True
        return redirect(url_for('roster'))
    return render_template('recruit.html', recruitment_form = recruit)

@app.route('/academy_registration', methods=['GET', 'POST'])
def academy_signup():
    academy_form = AcademyRegistrationForm()
    if academy_form.validate_on_submit():
        hero_id = academy_form.disciple_id.data
        new_school = Academy(academy_form.name.data, hero_id)
        db.session.add(new_school)
        db.session.commit()
        flash(f"New academy: {new_school.name} added to roster!")
        session['new_recruit'] = True
        return redirect(url_for('roster'))
    return render_template('academy_registration.html', academy = academy_form)

@app.route('/resign', methods=['GET', 'POST'])
def resign(): 
    resign = ResignForm()
    if resign.validate_on_submit():
        hero_id = resign.id.data
        retired_hero = Hero.query.filter_by(id=hero_id).first()
        flash(f"Former Hero: {retired_hero.name} removed from roster!")
        db.session.delete(retired_hero)
        db.session.commit()
        session['new_recruit'] = False
        return redirect(url_for('roster'))
    return render_template('resign.html', resignation_form = resign)

@app.route('/roster')
def roster():
    hero_roster = Hero.query.all()
    messageList = get_flashed_messages()
    if not messageList:
        session.clear()

    return render_template('roster.html', heroes = hero_roster)

if __name__ == '__main__':
    app.run(debug=True)