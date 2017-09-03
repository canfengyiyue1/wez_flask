from flask import Blueprint
admin_module = Blueprint('admin_module', __name__, template_folder='templates/default/admin/module')
from . import module_views

admin_module_function = Blueprint('admin_module_function', __name__, template_folder='templates/default/admin/module/function')
from . import function_views


#from .module_views import ModuleView

def init_app(app):
    app.register_blueprint(admin_module, url_prefix='/admin/module')
    app.register_blueprint(admin_module_function, url_prefix='/admin/module/<mid>')
#    register_api(app, ModuleView, 'admin_module', '/admin/module/', pk='id')
#
#
#def register_api(app, view, endpoint, url, pk='id', pk_type='string'):
#    view_func = view.as_view(endpoint)
#    app.add_url_rule(url, defaults={pk: None}, view_func=view_func, methods=['GET',])
#    app.add_url_rule(url, view_func=view_func, methods=['POST',])
#    app.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func,
#                     methods=['GET', 'PUT', 'DELETE'])
#
