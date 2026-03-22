from flask import Flask, render_template, request, redirect, url_for
import stripe

app = Flask(__name__)
public_key= "Find me in the docs"
stripe.api_key = "Find me in the docs"

@app.route('/')
def home():
    render_template('home.html', public_key=public_key)

@app.route('/donated')
def donated():
    return render_template('donated.html')

