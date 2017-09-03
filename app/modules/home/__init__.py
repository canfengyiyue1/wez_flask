from flask import Blueprint
home = Blueprint('home', __name__, template_folder='templates/default/home')
from . import views, errors

def init_app(app):
    app.register_blueprint(home)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
