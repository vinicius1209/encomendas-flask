from flask import Blueprint

default_bp = Blueprint('default_bp', __name__, template_folder='templates', static_folder='static', static_url_path='/default/static')

from . import routes