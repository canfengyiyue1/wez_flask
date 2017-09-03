from flask import Blueprint
admin = Blueprint('admin', __name__, template_folder='templates/default/admin')
from . import views

def init_app(app):
    app.register_blueprint(admin, url_prefix='/admin')
    from .user import admin_user as admin_user_blueprint
    app.register_blueprint(admin_user_blueprint, url_prefix='/admin/user')
    from .module import init_app as admin_module
    admin_module(app)
    from .product import init_app as admin_product
    admin_product(app)


