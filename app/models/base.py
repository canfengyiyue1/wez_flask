from app import db
import uuid
from flask import g
from time import time
from functools import partial, reduce

db_pre = 'we_'

class Base(object):

    @staticmethod
    def getTablename(tablename):
        return db_pre + tablename
    def save(self):
        self = generate_upeated_at(self)
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def uuid(kwargs):
        if 'weid' not in kwargs:
            kwargs['weid'] = str(uuid.uuid4())
        return kwargs


# use this function generate some field
def decorator_some(func):
    arr = [generate_wezchina_id, generate_weid, generate_created_at, generate_zchina_user_id]
    def wrapper(self, **kwargs):
        reduce_arr =list(map(lambda fc: partial(fc, self), arr))
        result = reduce(lambda p,n : n(**p), reduce_arr, kwargs)
        func(self, **result)
    return wrapper

def generate_wezchina_id(self, **kwargs):
    if 'wezchina_id' in self.__class__.__dict__ and 'wezchina_id' not in kwargs:
        kwargs['wezchina_id'] = g.domain.id
    return kwargs

def generate_zchina_user_id(self, **kwargs):
    if 'zchina_user_id' in self.__class__.__dict__\
            and 'zchina_user_id' not in kwargs\
            and 'user' in g:
        kwargs['zchina_user_id'] = g.user.id
    return kwargs


def generate_weid(self, **kwargs):
    if 'weid' in self.__class__.__dict__ and 'weid' not in kwargs:
        kwargs['weid'] = str(uuid.uuid4())
    return kwargs

def generate_created_at(self, **kwargs):
    if 'created_at' in self.__class__.__dict__:
        kwargs['created_at'] = int(time())
    return kwargs

def generate_upeated_at(self):
    if 'updated_at' in self.__class__.__dict__:
        self.updated_at = int(time())
    return self





# use this decorator to generate uuid
def decorator_uuid(func):
    def wrapper(self, **kwargs):
        if 'weid' not in kwargs:
            kwargs['weid'] = str(uuid.uuid4())
        func(self, **kwargs)
    return wrapper


# this function use to decorate wezchina_id
def decorator_wechina_id(func):
    def wrapper(self, **kwargs):
        if 'wechina_id' not in kwargs:
            kwargs['wechina_id'] = g.domain.id
        func(self, **kwargs)
    return wrapper

# this function use to generate created_at
def decerator_create(func):
    def wrapper(self, **kwargs):
        kwargs['created_at'] = int(time())
        func(self, **kwargs)
    return wrapper


# this function use to generate created_at
def decerator_update(func):
    def wrapper(self, **kwargs):
        kwargs['updated_at'] = int(time())
        func(self, **kwargs)
    return wrapper



