from . import default_bp
from app.models import User
from flask import render_template, flash, url_for, request, abort, redirect, jsonify, send_file, make_response
from flask_login import current_user, login_user, logout_user, login_required
import json

# Login
@default_bp.route('/', methods=['GET', 'POST'])
@default_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json(silent=True)

        if "username" not in data:
            return abort(400)
        if "password" not in data:
            return abort(400)

        username = data["username"]
        password = data["password"]

        user = User.query.filter_by(username=username).first()
        
        # Check user pass
        if user is None: 
            return jsonify({"status": 404, "msg": "Usuário não existente"})
        if not user.check_password(password):
            return jsonify({"status": 404, "msg": "Senha preenchida incorreta"})
        
        login_user(user)
        return jsonify({"status": 200, "redirect": "/home"})
    else:
        if current_user.is_authenticated:
            return redirect(url_for('home'))

        return render_template('login.html')

@login_required
@default_bp.route('/home')
def index():
    return "Hello"