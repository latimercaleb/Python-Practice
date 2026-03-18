from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
from project.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={"placeholder": "Enter username"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "test@example.com"})
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password_confirmed', message='Passwords must match')], render_kw={"placeholder": "Enter password"})
    password_confirmed = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": "Confirm password"})
    submit = SubmitField('Sign Up')

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email previously registered')
    
    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "test@example.com"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Enter password"})
    submit = SubmitField('Log In')

    