from . import admin_bp
from flask_login import current_user, login_user, logout_user, login_required

@login_required
@admin_bp.route('/admin/create/user')
def create_user():
    return "Create user"