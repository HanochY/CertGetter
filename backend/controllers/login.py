from utils.exceptions import *
from models.user import *
from flask import request, flash, render_template, session, redirect

def login(username, password):
    if not check_user_exists(username):
        raise UserNotFoundError
    if not get_password(username) == password:
        raise WrongPasswordError


def register(username, password, confirm_password):
    if not password == confirm_password:
        raise PasswordConfirmationError
    if check_user_exists(username):
        raise UserAlreadyExistsError
    

def post_form():
    if request.form['button'] == 'login':
        try:
            username, password = (request.form.get(value) for value in ('login_username', 'login_password'))
            login(username, password)
        except Exception as e:
            print(e)
            flash(e.message)
            return render_template('login.html')
        else:
            session["username"] = username
            return redirect('/grabber')
        
    elif request.form['button'] == 'register':
        try:
            username, password, confirm_password = (request.form(value) for value in ('register_username', 'register_password', 'confirm_register_password'))
            register(username, password, confirm_password)
        except Exception as e:
            flash(e.message)
            return render_template('login.html')
        else:
            User(username, password).save()
