from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        if username and password:
            flash('got the info', category='succsess')
        else:
            flash('wrong email or password', category='error')
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return render_template('logout.html')

@auth.route('/sign-up', methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        pass
    if request.method == "POST":
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be at least 4 characters', category='error')
        elif len(firstName) < 2:
            flash('Name must be at greater than 1 character', category='error')
        elif password1 != password2:
            flash('Passwords do no match', category='error')
        elif len(password1) < 7:
            flash('Passwords must be atleast 7 characters', category='error')
        else:
            flash('Account created successfully', category='success')

    return render_template('sign_up.html')