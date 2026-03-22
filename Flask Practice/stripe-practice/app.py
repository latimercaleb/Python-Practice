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

@app.route('/charge', methods=['POST'])
def charge():
    # Transaction amount
    transaction_total = 250 # Amount in cents, so this is $2.50

    # Customer details
    consumer = stripe.Customer.create(
        email=request.form['stripeEmail'],
        source=request.form['stripeToken']
    )

    #Payment data
    charge = stripe.Charge.create(
        customer=consumer.id,
        amount=transaction_total,
        currency='usd',
        description='Flask Charge'
    )

    return redirect(url_for('donated'))

if __name__ == '__main__':
    app.run(debug=True)