from project import app,db 
from flask import render_template, redirect, request, url_for, flash, abort, session
from project.forms import RegistrationForm, LoginForm
from flask_login import login_user, logout_user, login_required
from project.models import User
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def sign_up():
    pass

@app.route('/login', methods=['GET', 'POST'])
def login():
    pass

@app.route('/welcome') 
@login_required
def welcome():
    return render_template('authed.html')

@app.route('/logout') 
@login_required
def exit():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('index'))