#coding:utf-8
from flask import render_template,redirect, url_for,request
from .models import UserView,Products,Solutions,module
from . import admin
template_pre = 'default/admin/'


@admin.route('/users',defaults={'type':'index'})
@admin.route('/users/<type>')
def userInfo(type):
    return render_template(template_pre+'usersManage.html',type=type,)

@admin.route('/users/search/')
def userSearch():
    pass

@admin.route('/users/manage/')
def userManage():
    pass


@admin.route('/users/drop/')
def userDrop():
    return 'User information deleted '

@admin.route('/users/auth/')
def userAuth():
    id = request.form['id']
    authInfo = UserView()
    if id is None:
        authData=authInfo.userAuth()
        return authData
    else:
        authData=authInfo.userAuth(id)
        return authData


@admin.route('/users/cert/')
def userCret():
    id = request.form['id']
    cretInfo = UserView()
    if id is None:
        cretData=cretInfo.userCret()
        return cretData
    else:
        cretData=cretInfo.userCret(id)
        return cretData


