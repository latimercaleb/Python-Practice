import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1' # Only for testing purposes, allows for http instead of https
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1' # Only for testing purposes, allows for more relaxed scope checking
from flask import Flask, redirect, url_for, render_template
from flask_dance.contrib.google import make_google_blueprint, google # This is the library that provides the OAuth client for Flask
from dotenv import load_dotenv

load_dotenv()
app=Flask(__name__)
print("Hello creds?")
g_client_id = os.environ.get('Client_id').strip()
g_client_secret = os.environ.get('Client_secret').strip()
print(g_client_id)
print(g_client_secret)
app.config['SECRET_KEY'] =  'no_secrets_here'
app.config['GOOGLE_OAUTH_CLIENT_ID'] = g_client_id # This MUST be set to your Google OAuth client ID, which you can obtain from the Google Developer Console, otherwise app won't work
# TODO: Need to setup client & secret later, via google developer console, set up gitignore and add to env var for safety practices 
blueprint = make_google_blueprint(client_id=g_client_id, client_secret=g_client_secret, offline=True, scope=['profile', 'email']) # This creates a blueprint for Google OAuth, you need to provide your client id and secret here
app.register_blueprint(blueprint, url_prefix='/login') # This registers the blueprint with the Flask app, the url_prefix is where the OAuth routes will be available

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login/google')
def login():
    if not google.authorized: # This checks if the user is already authorized with Google
        return redirect(url_for('google.login')) # If not authorized, redirect to the Google login page
    response = google.get('/oauth2/v2/userinfo') # If authorized, make a request to the Google API to get the user's information
    assert response.ok, response.text # Check if the response is successful
    email = response.json()['email'] # Get the user's email from the response
    return render_template('welcome.html', email=email) # Render the welcome page with the user's email

@app.route('/welcome')
def welcome():
    # TODO: Integrate try/catch logic here to handle cases where the user is not authorized or there is an error with the Google API request
    response = google.get('/oauth2/v2/userinfo') # If authorized, make a request to the Google API to get the user's information
    assert response.ok, response.text # Check if the response is successful
    email = response.json()['email'] # Get the user's email from the response
    return render_template('welcome.html', email=email) # Render the welcome page with the user's email

if __name__ == '__main__':
    app.run(debug=True)
