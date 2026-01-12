from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Worrldo!</h1>'

@app.route('/info') # Static route
def info():
    return '<h1>Info world!</h1>'

@app.route('/info/<user>') # Dynamic route
def userInfo(user):
    return f'<h1>{user} world!</h1>'

@app.route('/infoTemplate') # Static route w/template
def infoTemplate():
    someBackendVar = 'foo'
    someBackendList = list(someBackendVar)
    someDictionary = {'key': 'val'}
    return render_template('index.html', vars=someBackendVar, vars2 = someBackendList, vars3 = someDictionary)

@app.route('/home') # Static route w/template
def home():
    return render_template('home.html')

@app.route('/user/<user>') # Static route w/template
def user(user):
    return render_template('user.html', name=user)


if __name__ == '__main__':
    app.run(debug=True)