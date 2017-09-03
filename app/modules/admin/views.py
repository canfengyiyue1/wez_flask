#coding:utf-8
from flask import render_template,redirect, url_for,request
from .models import UserView,Products,Solutions,module
from . import admin
template_pre = 'default/admin/'

@admin.route('/')
def index():
    return render_template(template_pre+'index.html')


@admin.route('/products',defaults={'type':'index'})
@admin.route('/products/<type>')
def product(type):
    return render_template(template_pre + 'productsManage.html',type=type)

