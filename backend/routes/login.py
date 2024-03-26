from flask import Blueprint, render_template, redirect
import controllers.login as controller
from utils.exceptions import *


login_blueprint = Blueprint("login_blueprint", __name__)

@login_blueprint.route('/')
def main():
    return redirect('/login')

@login_blueprint.get('/login')
def get_forms():
    return render_template('login.html')

@login_blueprint.post('/login')
def post_form():
    return controller.post_form()