from flask import Blueprint
admin_product = Blueprint('admin_product', __name__, template_folder='templates/default/admin/product')
from . import product_views

admin_product_function = Blueprint('admin_product_function', __name__, template_folder='templates/default/admin/product/function')
from . import function_views

admin_product_service = Blueprint('admin_product_service', __name__, template_folder='templates/default/admin/product/service')
from . import service_views

def init_app(app):
    app.register_blueprint(admin_product, url_prefix='/admin/product')
    app.register_blueprint(admin_product_function, url_prefix='/admin/product_function')
    app.register_blueprint(admin_product_service, url_prefix='/admin/product/<fid>')
