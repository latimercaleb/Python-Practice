# Make a username requirements check (Template practice)
# Take a user name, check and see if it passes 3 requirements(one lowercase letter, one uppercase letter, must end in a number)
# Needs navbar with home button, landing page redirects to report page after submitting form. Report page indicates if username is valid or not, if it is invalid it should explain why
# Start this after restyling with tailwind and use tailwind in this practice


# Steps
# Make a plan to approach this problem
# Test solution 
# Refine solution using tailwind
# Double back across all old code using tailwind


from flask import Flask, render_template
app = Flask(__name__)



@app.route('/') # Land at form-exercise-home.html, prototype out template, design form, handle submission event
def hostSource():
    return 

@app.route('/report') # Land at form-exercise-report.html, parse through user_report(might need request), check for  3 requirements(one lowercase letter, one uppercase letter, must end in a number), return success or error, if error return useful error message
def report(user_report): 
    return

if __name__ == '__main__':
    app.run(debug=True)