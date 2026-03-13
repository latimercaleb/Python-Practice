import os 
from forms import RecruitForm, ResignForm, AcademyRegistrationForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Additional reqs
# Add new model, table and ui screen for adding an X (call this something) => Academy (if no school then freelancer)
# X can take a name and an ID of a raider and connect them
# Table should render X in conjunction with raiders or None if there is none
# Use flash to send styled toasts/notifications for new X or new raiders
# Rules: Work from back to front, no solution help, compare only at the end and test all functionality


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
    academy_key = db.Column(db.Integer, db.ForeignKey('academy.id'))
    def __init__(self, name, title):
        self.name = name
        self.title = title
    
    def get_school(self): 
        return self.academy_key

    def __repr__(self):
        return f"{self.name} the {self.title}! Hero #{self.id}! From {self.get_school()}"
    

class Academy(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    heroes = db.relationship("hero", backref='academy', lazy='joined')
    
    def __init__(self, name, hero_id):
        self.name = name
        self.hero_id = hero_id
    
    def __repr__(self):
        return f"{self.name} home of {self.heroes}"
    
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

@app.route('/academy_registration', methods=['GET', 'POST'])
def academy_signup():
    academy_form = AcademyRegistrationForm()
    if academy_form.validate_on_submit():
        new_school = Academy(academy_form.name.data, academy_form.disciple_id.data)
        db.session.add(new_school)
        db.session.commit()
        return redirect(url_for('roster'))
    return render_template('academy_registration.html', academy = academy_form)

@app.route('/resign', methods=['GET', 'POST'])
def resign(): 
    resign = ResignForm()
    if resign.validate_on_submit():
        hero_id = resign.id.data
        Hero.query.filter_by(id=hero_id).delete()
        db.session.commit()
        return redirect(url_for('roster'))
    return render_template('resign.html', resignation_form = resign)

@app.route('/roster')
def roster(): 
    hero_roster = Hero.query.all()
    academy = Academy.query.all()
    print(hero_roster)
    print(academy)
    return render_template('roster.html', heroes = hero_roster)

if __name__ == '__main__':
    app.run(debug=True)