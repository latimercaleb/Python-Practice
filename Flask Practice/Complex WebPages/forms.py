
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

class RecruitForm(FlaskForm):
    name = StringField("Your Name: ")
    title = StringField("Your Hero Name: ")

class ResignForm(FlaskForm):
    id = IntegerField("Your Hero ID to Retire: ")
    submit = SubmitField("Complete Resignation")

class AcademyRegistrationForm(FlaskForm):
    name = StringField("Your School Name: ")
    disciple_id = IntegerField("Your Hero ID to Register: ")
    submit = SubmitField("Complete Academy Registration")