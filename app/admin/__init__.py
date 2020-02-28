from flask import Blueprint

admin_bp = Blueprint('admin_bp', __name__, url_prefix='/admin', template_folder='templates', static_folder='static')

from . import routes