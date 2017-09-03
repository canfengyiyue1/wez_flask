#coding:utf-8
from flask import render_template,redirect, url_for,request
from .models import User, UserAuth, UserCert
from . import admin_user
template_pre = 'default/admin/user/'

@admin_user.route('/')
def index():
    users = User.users()
    return render_template(template_pre+'index.html',lists=users)

@admin_user.route('/realname')
def realname():
    users = UserAuth.auths()
    return render_template(template_pre+'realname.html', lists=users)


@admin_user.route('/vcert')
def vcert():
    users = UserCert.auths()
    return render_template(template_pre+'vcert.html', lists = users)


