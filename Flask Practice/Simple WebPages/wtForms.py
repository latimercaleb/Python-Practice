from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'no_secrets_today'

#WTForms class
class RaiderTemplate(FlaskForm):
    job = StringField("What job are you?")
    role = StringField("What role are you?")
    submit = SubmitField("Submit")
