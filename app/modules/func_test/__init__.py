from flask import Blueprint
func_test = Blueprint('func_test', __name__, template_folder='template/default/func_test')
from . import views
