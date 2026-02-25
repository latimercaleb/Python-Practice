from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import ( StringField, 
                     SubmitField, 
                     BooleanField,
                     DateTimeField, 
                     RadioField, 
                     SelectField, 
                     TextAreaField, 
                     TelField )
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'no_secrets_today'

#WTForms class
class RaiderTemplate(FlaskForm):
    job = StringField("What job are you?")
    role = StringField("What role are you?")
    submit = SubmitField("Submit")

class StatForm(FlaskForm): # A little more complicated, practicing types
    strength = StringField("How Strong?", validators=[DataRequired()])
    dex = BooleanField("Dexterity Type?")
    magic = RadioField("Magician Type: ", choices=[('magic_type_1','Holy'),('magic_type_2','Void')])
    enchantment_type = SelectField("Pick a blessing: ", choices=[('enchantment_1','Spark'), ('enchantment_2','Poison'), ('enchantment_3','Recovery')])
    comments = TextAreaField()
    submit = SubmitField('Enter')

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

@app.route("/stats", methods=['GET', 'POST'])
def statForm():
    stats = StatForm()
    if stats.validate_on_submit():
        session['strength'] = stats.strength.data
        session['dex'] = stats.dex.data
        session['magic'] = stats.magic.data
        session['enchantment_type'] = stats.enchantment_type.data
        session['comments'] = stats.comments.data
        return redirect(url_for('exit'))
    return render_template('wtForms-index.html', form=stats)

@app.route("/thankYou")
def exit():
   return render_template('wtForms-thankYou.html')

if __name__ == '__main__':
    app.run(debug=True)