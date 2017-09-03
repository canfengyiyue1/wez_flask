from flask import g, redirect, request, current_app
from . import func_test
from app.services.realname.realname_service import checkOnline


template_pre = 'default/func_test/'

def dd(*args, **kwargs):
    print('----',*args, **kwargs)
    return False

@func_test.route('/realname')
def realname():
    name = '黄刚'
    idcard = '420106198108093252'
    result = checkOnline(name=name, idcard = idcard)
    print(result)
    pass

