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
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=generate_password_hash(form.password.data))
        db.session.add(user)
        db.session.commit()
        flash('Registered new user!')
        return redirect(url_for('login')) # TODO: Maybe rather than redirecting to login, we should log the user in immediately after registration and redirect to welcome page.
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first() # This works since constraint enforces unique email addresses
        if user and check_password_hash(user.password, form.password.data):
            flash('Login successful!')
            login_user(user, remember=form.remember_me.data)
            next = request.args.get('next')
            if next == None or not next.startswith('/'):
                next = url_for('welcome')
            return redirect(next)
        else:
            flash('Should have useful error message here. Either email or password is incorrect.')
    return render_template('login.html', form=form)

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

if __name__ == '__main__':
    app.run(debug=True)