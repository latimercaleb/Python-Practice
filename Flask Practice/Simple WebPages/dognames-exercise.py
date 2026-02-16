# Set up your imports here!
from flask import Flask, render_template
app = Flask(__name__)



@app.route('/') # Fill this in!
def landing():
    # Welcome Page
    # Create a generic welcome page.
    return '<h1>Welcome Page</h1>'

@app.route('/<dogName>')
def doggyLatin(dogName):
    lastChar = dogName[-1]
    if lastChar == 'y':
        newDog = dogName[:-1] + "iful"
        return f"Welcome in {newDog}"
    elif lastChar != 'y':
        newDog = dogName + "y"
        return f"Welcome in {newDog}"

if __name__ == '__main__':
    app.run(debug=True)