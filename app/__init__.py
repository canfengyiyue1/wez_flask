import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_debugtoolbar import DebugToolbarExtension
import pymysql
pymysql.install_as_MySQLdb()

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()
toolbar = DebugToolbarExtension()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = '/'


def register_models():
    import sys
    basedir = os.path.abspath(os.path.dirname(__file__))
    models_dir = os.path.join(basedir,'models')
    sys.path.append(models_dir)

def create_app(config_name):
    #register_models()
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].__init__(app)
    app.debug = True

    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    toolbar.init_app(app)

    # This is for global domain check
    from .handlers.domain import Domain
    domain = Domain()
    domain.init_app(app)

    from .modules.home import init_app as home_blueprint
    home_blueprint(app)

    from .modules.user import user as user_blueprint
    app.register_blueprint(user_blueprint,url_prefix='/user')

    from .modules.admin import init_app as admin_blueprint
    admin_blueprint(app)

    from .modules.func_test import func_test as test_blueprint
    app.register_blueprint(test_blueprint, url_prefix='/test')

    return app
