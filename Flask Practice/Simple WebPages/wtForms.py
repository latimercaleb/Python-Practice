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

# Routing
@app.route("/", methods=['GET', 'POST'])
def home(): 
    raiderJob = False
    raiderRole = False
    raiderForm = RaiderTemplate()
    if raiderForm.validate_on_submit():
        raiderJob = raiderForm.job.data
        raiderRole = raiderForm.role.data
        raiderForm.job.data = ''
        raiderForm.role.data = ''
    return render_template('wtForms-index.html', form=raiderForm, job=raiderJob, role=raiderRole)

if __name__ == '__main__':
    app.run(debug=True)