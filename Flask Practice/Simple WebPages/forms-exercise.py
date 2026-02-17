# Make a username requirements check (Template practice)
# Take a user name, check and see if it passes 3 requirements(one lowercase letter, one uppercase letter, must end in a number)
# Needs navbar with home button, landing page redirects to report page after submitting form. Report page indicates if username is valid or not, if it is invalid it should explain why
# Start this after restyling with tailwind and use tailwind in this practice


# Steps 
# Refine solution using tailwind
# Double back across all old code using tailwind


from flask import Flask, render_template, request
app = Flask(__name__)



@app.route('/') # Land at form-exercise-home.html, prototype out template, design form, handle submission event
def pageOne():
    return render_template('form-exercise-home.html')

@app.route('/report') # Land at form-exercise-report.html, parse through user_report(might need request), check for  3 requirements(one lowercase letter, one uppercase letter, must end in a number), return success or error, if error return useful error message
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