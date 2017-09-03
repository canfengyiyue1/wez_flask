from flask import url_for, redirect
from flask_login import login_required,current_user


def auth_user(req, next_func, *args, **kwargs):
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'), code=302)
    return next_func(req, *args, **kwargs)



def test(req, next_func, *args, **kwargs):
    return next_func(req, *args, **kwargs)


def test2(req, next_func, *args, **kwargs):
    return next_func(req, *args, **kwargs)


mis = {
    'auth_user': [auth_user,test],
    't1':[test, test2]

}
