# -*- coding: utf-8 -*-
from flask import render_template, redirect, url_for, current_app, request, flash
from flask_login import current_user
from flask_login import login_required,LoginManager
from app import login_manager
from . import user
# from app.middleware.base import handle
from app.middleware.middleware import HttpMiddleware
from flask.views import View
from .models import UserAuth, UserWeAuth, UserSet, UserAuthForm, UserWeAuthForm, UserProduct, UserSolution, product, solution
from werkzeug.utils import secure_filename
import os
from ...models.zchina_user import Zchina_user

template_pre = 'default/user/'
middle = HttpMiddleware()
@user.before_request
@middle.register('auth_user')
def before_request():
    pass


@user.route('/')
@login_required
def index():
    return render_template(template_pre+'index.html')

@user.route('/setting',methods=['GET','POST'])
@login_required
def setting():
    ID = Zchina_user.query.filter_by(mobile=current_user.mobile).first().id
    if(not request.form):
        userInfo = UserSet().getUserInfo(ID)
        return render_template(template_pre + 'setting.html', userinfo=userInfo)
    else:
        userInfo = UserSet().updateUserInfo(request.form, ID)
        flash(message="资料更新成功")
        return render_template(template_pre + 'setting.html', userinfo=userInfo)


# 用户实名认证
@user.route('/userAuth', methods=['GET', 'POST'])
@login_required
def userAuth():
    ID = Zchina_user.query.filter_by(mobile=current_user.mobile).first().id
    form = UserAuthForm()
    userAuthObj = UserAuth()
    if(not userAuthObj.userID_existed(ID)):
        userAuthId = userAuthObj.insertUidData(ID)
    else:
        userAuthId = userAuthObj.getUserAuthID(ID)

    if form.validate_on_submit():  # 如果 通过 post 提交的表单，数据通过了所有验证器的检查
        if(not userAuthObj.allowed_file(form.ID_photo_front.data.filename) and not userAuthObj.allowed_file(form.ID_photo_back.data.filename)):
            flash(message='只允许上传图片文件', category='error')
            return render_template(template_pre + 'user_auth.html', form=form)
        userdir = 'user'+str(ID)
        path = 'user_uploads/%s'%(userdir)
        if(not os.path.exists(path)):
            os.mkdir('user_uploads/%s'%(userdir))

        front_fileneme=secure_filename(form.ID_photo_front.data.filename)
        frontPhotoExtention = userAuthObj.file_extension(front_fileneme)
        frontPhotoSaveLocation = 'user_uploads/%s/'%(userdir)+'front_photo%s.%s'%(ID, frontPhotoExtention)
        form.ID_photo_front.data.save(frontPhotoSaveLocation)

        back_fileneme=secure_filename(form.ID_photo_back.data.filename)
        backPhotoExtemtion = userAuthObj.file_extension(back_fileneme)
        backPhotoSaveLocation = 'user_uploads/%s/'%(userdir)+'back_photo%s.%s'%(ID, backPhotoExtemtion)
        form.ID_photo_back.data.save(backPhotoSaveLocation)

        data = {'name':form.name.data, 'id_number':form.id_number.data, 'birthday':form.birthday.data, 'sex':form.sex.data, 'address':form.address.data, 'ID_photo_front':frontPhotoSaveLocation, 'ID_photo_back': backPhotoSaveLocation}

        userAuthObj.formDataToDatabase(data, userAuthId)
        flash(message="验证资料已提交，等待审核")
        form.id_number.data = userAuthObj.id_number_hide(form.id_number.data)
        return render_template(template_pre +'user_auth.html', form=form)

    # if form.validate_on_submit():  # 如果 通过 post 提交的表单，数据通过了所有验证器的检查
    #
    #     data = {'name':form.name.data, 'id_number':form.id_number.data, 'birthday':form.birthday.data, 'sex':form.sex.data,'address':form.address.data,'ID_photo_front':form.ID_photo_front.data,'ID_photo_back': form.ID_photo_back.data}
    #     userAuthObj.formDataToDatabase(data, userAuthId)
    #     form.id_number.data = userAuthObj.id_number_hide(form.id_number.data)
    #     return render_template(template_pre +'user_auth.html', form=form)

    else:
        #尚未认证的
        userAuthInfo = userAuthObj.getUserAuthInfo(userAuthId)
        form.name.data = userAuthInfo.name
        if(userAuthInfo.id_number):
            form.id_number.data = userAuthObj.id_number_hide(userAuthInfo.id_number)
        else:
            form.id_number.data = userAuthInfo.id_number
        form.birthday.data = userAuthInfo.birthday
        form.sex.data = userAuthInfo.sex
        form.address.data = userAuthInfo.address
        form.ID_photo_front.data = userAuthInfo.ID_photo_front
        form.ID_photo_back.data = userAuthInfo.ID_photo_back
        return render_template(template_pre + 'user_auth.html', form=form)


# 用户企业加V认证
@user.route('/userWeAuth', methods=['GET', 'POST'])
@login_required
def userWeAuth():
    ID = Zchina_user.query.filter_by(mobile=current_user.mobile).first().id
    form = UserWeAuthForm()
    userWeAuthObj = UserWeAuth()
    if(not userWeAuthObj.userID_existed(ID)):
        userWeAuthId = userWeAuthObj.insertUidData(ID)
    else:
        userWeAuthId = userWeAuthObj.getUserAuthID(ID)

    if form.validate_on_submit():  # 如果 通过 post 提交的表单，数据通过了所有验证器的检查
        data = {'name': form.name.data, 'address': form.address.data, 'nature': form.nature.data, 'license': form.license.data, 'authorization': form.authorization.data}
        userWeAuthObj.formDataToDatabase(data, userWeAuthId)
        flash(message="资料已提交，等待审核")
        return render_template(template_pre +'user_we_auth.html', form=form)

    else:
        userWeAuthInfo = userWeAuthObj.getUserWeAuthInfo(userWeAuthId)
        form.name.data = userWeAuthInfo.name
        form.address.data = userWeAuthInfo.address
        form.nature.data = userWeAuthInfo.nature
        form.license.data = userWeAuthInfo.license
        form.authorization = userWeAuthInfo.authorization
        return render_template(template_pre + 'user_we_auth.html', form=form)


@user.route('/productList')
def productList():
    products = product.listAll()
    return render_template(template_pre + 'product_list.html', products=products)


@user.route('/buyProduct', methods=['GET', 'POST'])
@login_required
def buyProduct():
    ID = Zchina_user.query.filter_by(mobile=current_user.mobile).first().id
    proID = request.form['proID']
    userProductObj = UserProduct()
    if(not userProductObj.pID_existed(pId=proID,userId=ID)):
        userProductObj.buyProduct(pId=proID, userId=ID)
        flash(message="产品购买成功")
    products = product.listAll()
    return render_template(template_pre + 'product_list.html', products=products, proID=proID)


@user.route('/userProduct')
@login_required
def userProduct():
    ID = Zchina_user.query.filter_by(mobile=current_user.mobile).first().id
    userProduct = UserProduct()
    products = userProduct.orderList(ID)
    return render_template(template_pre + 'user_product.html', products=products)



@user.route('/solutionList')
def solutionList():
    solutions = solution.listAll()
    return render_template(template_pre + 'solution_list.html', solutions=solutions)

@user.route('/buySolution',methods=['GET', 'POST'])
@login_required
def buySolution():
    ID = Zchina_user.query.filter_by(mobile=current_user.mobile).first().id
    sloID = request.form['sloID']
    userSolutionObj = UserSolution()
    if(not userSolutionObj.sID_existed(sloID,ID)):
        userSolutionObj.buySolution(sId=sloID, userId=ID)
        flash(message="方案购买成功")
    solutions = solution.listAll()
    return render_template(template_pre + 'solution_list.html', solutions=solutions, sloID=sloID)

@user.route('/userSolution')
@login_required
def userSolution():
    ID = Zchina_user.query.filter_by(mobile=current_user.mobile).first().id
    userSolution = UserSolution()
    solutions = userSolution.orderList(ID)
    return render_template(template_pre + 'user_solution.html', solutions=solutions)


@user.route('/userOrder')
@login_required
def userOrder():
    ID = Zchina_user.query.filter_by(mobile=current_user.mobile).first().id
    userProduct = UserProduct()
    userSolution = UserSolution()
    products = userProduct.orderList(ID)
    solutions = userSolution.orderList(ID)
    return render_template(template_pre + 'user_orderList.html', products=products, solutions=solutions)



