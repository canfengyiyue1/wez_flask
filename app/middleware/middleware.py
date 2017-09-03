from functools import wraps, reduce
from flask import redirect,request,url_for
from .kernel import mis

class Middleware:
    def __init__(self,mid_arr):
        self.mid_arr = mid_arr

    def decorator(self,func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_arr = self.dispatch(mis[self.mid_arr],func)
            return func_arr(request, *args, **kwargs)
        return wrapper


    def originToPostable(self,func):
        """wrap origin function"""
        return lambda req,  *args, **kwargs: func(*args, **kwargs)


    def carry(self,pre, next_func):
        """wraps func"""
        return lambda req, *args, **kwargs: next_func(req, pre, *args, **kwargs)


    def dispatch(self,arr, func, *args, **kwargs):
        """dispatch"""
        postable = self.originToPostable(func)
        arr.reverse()
        return reduce(self.carry, arr, postable)

class HttpMiddleware:
    def __init__(self):
        self.func_map = {}

    def register(self,name):
        def fetch(func):
            @wraps(func)
            def func_wrapper(*args, **kwargs):
                func_arr= self.dispatch(mis[name],func)
                self.func_map[name] =func_arr
                return func_arr(request, *args, **kwargs)
            return func_wrapper
        return fetch

    def call_method(self, name=None):
        func = self.func_map.get(name,None)
        if func is None:
            raise Exception("No middleware registered against -" + str(name))
        return func()

    def originToPostable(self,func):
        """wrap origin function"""
        return lambda req,  *args, **kwargs: func(*args, **kwargs)


    def carry(self,pre, next_func):
        """wraps func"""
        return lambda req, *args, **kwargs: next_func(req, pre, *args, **kwargs)


    def dispatch(self,arr, func, *args, **kwargs):
        """dispatch"""
        postable = self.originToPostable(func)
        arr.reverse()
        return reduce(self.carry, arr, postable)

