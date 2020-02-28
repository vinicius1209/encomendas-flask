from . import admin_bp
from flask_login import current_user, login_user, logout_user, login_required

@admin_bp.route('/create/user')
@login_required
def create_user():
    return "Create user"