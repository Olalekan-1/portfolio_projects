from flask import Blueprint

admin = Blueprint('admin', __name__)


@admin.route('/admin')
def admin_page():
    return "This is an Admin page"
