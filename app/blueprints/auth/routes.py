from flask import render_template, request, redirect, url_for, flash
import flask
from .import bp as auth
from .forms import LoginForm, RegisterForm, EditProfileForm
from .models import User
from flask_login import login_user, logout_user, current_user, login_required

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        try:
            new_user_data = {
                'first_name' : form.first_name.data.title(),
                'last_name' : form.last_name.data.title(),
                'email' : form.email.data.lower(),
                'icon' : int(form.icon.data),
                'password' : form.password.data
            }
            new_user_object = User()
            new_user_object.from_dict(new_user_data)
        except:
            flash("There was an unexpected error creating the user account", "danger")
            return render_template('auth/register.html.j2', form=form)
        flash("You have successfully registered an account", "success")
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html.j2', form=form)


# used to display the login page - all the routes below
@auth.route('/', methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data.lower()
        password = form.password.data
        print('Here')
        print(password)
        user_account = User.query.filter_by(email=email).first()
        print(user_account)
        if user_account is not None and user_account.check_hashed_password(password):
            login_user(user_account)
            flash("You have successfully logged in", "success")
            return redirect(url_for('main.pokemon'))
        else:
            flash("Invalid username/password combo ", "danger")
            return redirect(url_for('auth.login'))

        # if email in app.config.get('REGISTERED_USERS', {}).keys() and\
        #      password == app.config.get('REGISTERED_USERS', {}).get(email).get('password'):
        #      return f"Login was successful, Welcome {app.config.get('REGISTERED_USERS', {}).get(email).get('name')}"
        # error_string = "Incorrect Email/Password"
        # return render_template("index.html.j2", form=form, error=error_string)
    return render_template("auth/index.html.j2", form=form)
        


@auth.route('/logout', methods=['GET', 'POST'])
@login_required        
def logout():
    if current_user:
        logout_user()
        flash("You have successfully logged out from your account", "warning")
        return redirect(url_for('auth.login'))


@auth.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    form = EditProfileForm()
    print('here 5')
    if request.method == 'POST' and form.validate_on_submit():
        new_user_data = {
            'first_name' : form.first_name.data.title(),
            'last_name' : form.last_name.data.title(),
            'email' : form.email.data.lower(),
            'icon' : int(form.icon.data) if int(form.icon.data) != 8001 else current_user.icon,
            'password' : form.password.data
        }
        print('here 1')
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user and current_user.email != user.email:
            flash("Email is already in use", "danger")
            print('here 2')
            return redirect(url_for('auth.edit_profile'))

        try:
            current_user.from_dict(new_user_data)
            flash('Profile was updated successfully', 'success')
            return redirect(url_for('main.pokemon'))
        except:
            print('here 3')
            flash("There was an unexpected error creating the user account", "danger")
            return redirect('auth.edit_profile')
    return render_template('auth/register.html.j2', form=form)
