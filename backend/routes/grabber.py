from flask import Blueprint, render_template, session, send_file
import controllers.grabber as controller
from utils.exceptions import *
from middleware.authentication import require_login

grabber_blueprint = Blueprint("grabber_blueprint", __name__)

@grabber_blueprint.get('/grabber')
@require_login
def get_grabber():
    return render_template('grabber.html', username=session["username"])


@grabber_blueprint.post('/grabber')
@require_login
def grab():
    return send_file(r"..\resources\example.txt", as_attachment=True)

