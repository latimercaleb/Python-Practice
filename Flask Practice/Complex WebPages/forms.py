
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class RecruitForm(FlaskForm):
    name = StringField("Your Name: ")
    title = StringField("Your Hero Name: ")

class ResignForm(FlaskForm):
    id = IntegerField("Your Hero ID to Retire: ")
    submit = SubmitField("Complete Resignation")