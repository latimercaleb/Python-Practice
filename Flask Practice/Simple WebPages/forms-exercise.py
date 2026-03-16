from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/') 
def pageOne():
    return render_template('form-exercise-home.html')

@app.route('/report')
def report():
    errorList = []
    userName = request.args.get('userName')

    isValidUserName = True
    hasLowerCase = False
    hasUpperCase = False
    
    print(userName)

    if not userName[-1].isdigit():
        errorList.append("User Name does not end with a numeric")

    for character in userName:
        if character.islower():
            hasLowerCase = True
        elif character.isupper():
            hasUpperCase = True
        if hasLowerCase and hasUpperCase == True:
            break
    
    if hasLowerCase == False:
        errorList.append("User Name is missing lower case letter")
    if hasUpperCase == False:
        errorList.append("User Name is missing upper case letter")
    if len(errorList) > 0:
        isValidUserName = False
        

    return render_template('form-exercise-report.html', validUsr= isValidUserName, name= userName, usrNameErrors= errorList)

if __name__ == '__main__':
    app.run(debug=True)