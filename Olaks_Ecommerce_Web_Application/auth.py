from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route('/login')
def auth_page():
    return "This is an authentication page"
