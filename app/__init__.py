from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from . import config 

app = Flask(__name__)
app.config.from_object(config.Config) 

# Sql Alchemy / Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Login manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from .admin import admin_bp
from .default import default_bp

app.register_blueprint(admin_bp)
app.register_blueprint(default_bp)

def execute_app():
    return app
