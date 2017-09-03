from functools import wraps, reduce
from flask import current_app, request, url_for,redirect


def test(req, next_func, *args, **kwargs):
    return next_func(req, *args, **kwargs)

def test2(req, next_func, *args, **kwargs):
    print('--test2---',req, next_func)
    return next_func(req, *args, **kwargs)
    #return redirect(url_for('auth.login'),code=302)

mis = {'t1': [test, test2]}


def handle(mid_arr):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_arr = dispatch(request, mis[mid_arr], func)
            return func_arr(request, *args, **kwargs)
        return wrapper
    return decorate


def originToPostable(func):
    """wrap origin function"""
    return lambda req,  *args, **kwargs: func(*args, **kwargs)


def carry(pre, next_func):
    """wraps func"""
    print('-----post-----',pre)
    return lambda req, *args, **kwargs: next_func(req, pre, *args, **kwargs)


def dispatch(req, arr, func, *args, **kwargs):
    """dispatch"""
    postable = originToPostable(func)
    arr.reverse()
    return reduce(carry, arr, postable)
