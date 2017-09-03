#from flask_admin.contrib.sqla import ModelView
from flask import Flask
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from flask_sqlalchemy import SQLAlchemy
from ...models import *
from app import db
# class CustomModelView(ModelView):
#     """View function of Flask-Admin for Models page."""
#     pass

from wtforms import fields, validators
import hashlib



class LoginForm:

    login = fields.StringField(label=u'管理员账号', validators=[validators.required()])
    password = fields.PasswordField(label=u'密码', validators=[validators.required()])

    def validate_login(self, field):

        user = self.get_user()
        if user is None:
            raise validators.ValidationError(u'账号不存在')
        #用sha256_crypt加密
        if not hashlib.sha256.verify(self.password.data, user.password):
            raise validators.ValidationError(u'密码错误')

    def get_user(self):
        pass
        #AdminUser是存储管理员用户密码的表
        #return db.session.query("管理员帐号表").filter_by(login=self.login.data).first()





class User(Form):
    #这三个变量定义管理员是否可以增删改，默认为True
    can_delete = False
    can_edit = False
    an_create = False

    column_labels = dict(
        id=u'id',
        weid=u'weid',
        real_name=u'用户名',
        mobile=u'手机号',
        balanec=u'余额',
        nickname=u'用户昵称',
        wx_open_id=u'微信打开id',
        user_type_id=u'用户类型',
        zchina_cert=u'微众认证',
        zchina_auth=u'实名认证',
        status=u'用户状态'
    )

    # 只需把自己写的处理模型的视图加进去就行了，category是可选的目录

    #admin.add_view(UserView(User, db.session, name=u'信息', category=u'用户'))

def changeInfo(self, Info,tablename):
    # 修改信息的方法,返回修改后的数据
    SQLAlchemy.db.session.query(tablename).update(Info)
    SQLAlchemy.db.session.commit()
    Info = tablename.query.get('%s' % Info.weid)
    return Info



class UserView(object):

    def userSearch(self,id=None):
        #查询用户信息
        tableName = zchina_user.Zchina_user()
        if id is None :

            userInfo = tableName.query.all()
            return userInfo

        else:
            userInfo = tableName.query.get('%s' %id)
            return userInfo
        # userInfo = db.session.query(User).limit(10).all()  #限制返回记录条目数量
        # userInfo = User.query.paginate(1,10)  #分页显示查询到的内容，查询第一页，且1页显示10条内容
        #   paginate对象的属性  :userInfo.items  获取这一页所包含的数据对象, userInfo.page  获取这页的页码，
        #    if user_page.has_next:   如果有下一页的话, 获取下一个的 pagination 对象
            #  user_page.next()

    def userManage(self,userData):
        #使用userchange修改信息
        tableName = zchina_user.Zchina_user()
        info=tableName.query.get('%s'%userData.id)
        userInfo=changeInfo(Info=info,tablename='zchina_users')
        return userInfo

    def userDrop(self,id):

        tableName = zchina_user.Zchina_user()
        userInfo=tableName.query.get('%s'%id)
        db.session.delete(userInfo)
        db.session.commit()



    def userAuth(self,id=None):
        #查询需要认证的信息
        tableName = zchina_user_auth.Zchina_user_auths()
        if id is None :

            userInfo = tableName.query.filter(active = 2).all()
            return userInfo

        else:
            userInfo = tableName.query.get('%s' %id)
            return userInfo


    def userCret(self,id=None):
        #查询需要微认证的信息
        tableName = zchina_user_cert.Zchina_user_cert()
        if id is None :

            userInfo = tableName.query.filter(active = 2).all()
            return userInfo

        else:
            userInfo = tableName.query.get('%s' %id)
            return userInfo

class Products(object):

    def productSearch(self,id=None):
            # 查询产品信息
        tableName = zchina_product.Zchina_product()
        if id is None:

            productInfo = tableName.db.query.all()
            return productInfo

        else:
            productInfo = tableName.query.get('%s' % id)
            return productInfo


    def productManage(self,id):
        tableName = zchina_product.Zchina_product()
        info = tableName.query.get('%s' % id)
        productInfo = changeInfo(Info=info,tablename='zchina_products')
        return productInfo

    def productService(self,id=None):

        tableName = zchina_product_service.Zchina_product_service()
        if id is None:

            serviceInfo = tableName.db.query.all()
            return serviceInfo

        else:
            serviceInfo = tableName.query.get('%s' % id)
            return serviceInfo



class Solutions(object):

    def solutionInfo(self, id=None):
        # 查询解决方案信息
        tableName = zchina_solution.Zchina_solution()
        if id is None:
            solutionInfo = tableName.db.query.all()
            return solutionInfo

        else:
            solutionInfo = tableName.query.get('%s' % id)
            return solutionInfo

    def solutionManage(self,id):
         # 使用userchange修改信息
        tableName = zchina_solution.Zchina_solution()
        info = tableName.query.get('%s' % id)
        solutionInfo = changeInfo(Info=info,tablename='zchina_solutions')
        return solutionInfo


    def solutionService(self,id=None):

        tableName = zchina_solution_service.Zchina_solution_service()
        if id is None:
            serviceInfo = tableName.db.query.all()
            return serviceInfo

        else:
            serviceInfo = tableName.query.get('%s' % id)
            return serviceInfo


class module(object):
    def moduleInfo(self, id=None):
        # 查询模块信息
        tableName = zchina_module.Zchina_module()
        if id is None:
            moduleInfo = tableName.db.query.all()
            return moduleInfo

        else:
            moduleInfo = tableName.query.get('%s' % id)
            return moduleInfo

    def moduleManage(self, id):
        # 使用userchange修改信息
        tableName = zchina_module.Zchina_module()
        info = tableName.query.get('%s' % id)
        moduleInfo = changeInfo(Info=info, tablename='zchina_modules')
        return moduleInfo
