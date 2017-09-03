# -*- coding: utf-8 -*-
from app import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, SelectField
from wtforms.validators import DataRequired, Length
from ...models.zchina_user import Zchina_user
from ...models.zchina_user_auth import Zchina_user_auth
from ...models.zchina_user_cert import Zchina_user_cert
from ...models.zchina_product_service import Zchina_product_service
from ...models.zchina_solution_service import Zchina_solution_service
from ...models.zchina_product import Zchina_product
from ...models.zchina_solution import Zchina_solution


class UserAuthForm(FlaskForm):
    # 用户实名认证表单
    name = StringField('身份证姓名', validators=[DataRequired()])
    id_number = StringField('身份证号', validators=[DataRequired(), Length(18)])
    birthday = StringField('生日')
    sex = SelectField('性别',choices=[('男', '男'), ('女', '女')], validators=[DataRequired()])
    address = StringField('住址', validators=[DataRequired()])
    ID_photo_front = FileField('身份证正面照片', validators=[DataRequired()])
    ID_photo_back = FileField('身份证反面照片', validators=[DataRequired()])
    submit = SubmitField('提交')


class UserWeAuthForm(FlaskForm):
    # 用户企业加V认证表单
    name = StringField('企业名', validators=[DataRequired()])
    address = StringField('地址', validators=[DataRequired()])
    nature = StringField('企业性质', validators=[DataRequired()])
    license = StringField('企业执照', validators=[DataRequired()])
    authorization = StringField('授权书', validators=[DataRequired()])
    submit = SubmitField('提交')



#  用户设置
class UserSet:
    @staticmethod
    def getUserInfo(id=None):
        #userInfo = Zchina_user.query.get('%s' % id)
        userInfo = Zchina_user.query.filter_by(id=id).first()
        return userInfo

    @staticmethod
    def updateUserInfo(sql, id=None):
        #db.session.query(Zchina_user).update(sql)
        Zchina_user.query.filter_by(id=id).update(sql)
        db.session.commit()
        #info = Zchina_user.query.get('%s' %id)
        userInfo = Zchina_user.query.filter_by(id=id).first()
        return userInfo


# 用户实名认证
class UserAuth:
    def userID_existed(self,userID=None):  # 认证表中是否有UerId数据
        if(Zchina_user_auth.query.filter_by(zchina_user_id=userID).first() != None):
            return True
        else:
            return False
    def insertUidData(self, userID=None): #认证表中插入UerId数据
        db.session.add(Zchina_user_auth(zchina_user_id=userID))
        db.session.commit()
        userAuthId=Zchina_user_auth.query.filter_by(zchina_user_id=userID).first().id
        return userAuthId

    def getUserAuthID(self, userID=None):
        userAuthId = Zchina_user_auth.query.filter_by(zchina_user_id=userID).first().id
        return userAuthId

    def formDataToDatabase(self,data,userAuthId=None):
        Zchina_user_auth.query.filter_by(id=userAuthId).update(data)
        db.session.commit()
        userInfo = Zchina_user_auth.query.filter_by(id=userAuthId).first()
        return userInfo
    # 获取用户认证信息
    def getUserAuthInfo(self, userAuthId=None):
        userAuthInfo = Zchina_user_auth.query.filter_by(id=userAuthId).first()
        return userAuthInfo

    # 隐藏返回前端身份证号信息
    def id_number_hide(self,id_num):
        return id_num[:3] + '*************' + id_num[16:]

    # 判断上传文件是否为图片
    @staticmethod
    def allowed_file(filename):
        ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
        return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
    # 获取文件扩展名
    @staticmethod
    def file_extension(filename):
        return '.' in filename and filename.rsplit('.', 1)[1]

    # # 提供给第三方平台验证的实名信息
    # def get_id_info(self, userId=None):
    #     name = Zchina_user_auth.query().filter_by(zchina_user_id=userId).first().name
    #     id_num = Zchina_user_auth.query().filter_by(zchina_user_id=userId).first().id_number
    #     return [name, id_num]

    # # 与第三方平台对接
    # def user_info_checked(self):
    #     pass


# 用户加V企业认证
class UserWeAuth:
    def userID_existed(self,userID=None):  # 认证表中是否有UerId数据
        if(Zchina_user_cert.query.filter_by(zchina_user_id=userID).first() != None):
            return True
        else:
            return False

    def insertUidData(self, userID=None): #认证表中插入UerId数据
        db.session.add(Zchina_user_cert(zchina_user_id=userID))
        db.session.commit()
        userWeAuthId=Zchina_user_cert.query.filter_by(zchina_user_id=userID).first().id
        return userWeAuthId

    def getUserAuthID(self, userID=None):
        userWeAuthId = Zchina_user_cert.query.filter_by(zchina_user_id=userID).first().id
        return userWeAuthId

    def formDataToDatabase(self,data,userWeAuthId=None):
        Zchina_user_cert.query.filter_by(id=userWeAuthId).update(data)
        db.session.commit()
        userInfo = Zchina_user_cert.query.filter_by(id=userWeAuthId).first()
        return userInfo

    # 获取企业认证信息
    def getUserWeAuthInfo(self, userWeAuthId=None):
        userWeAuthInfo = Zchina_user_cert.query.filter_by(id=userWeAuthId).first()
        return userWeAuthInfo

class product:
    @classmethod
    def listAll(cls):
        products=Zchina_product.query.all()
        return products


# 用户产品信息
class UserProduct:
    def pID_existed(self, pId=None,userId=None):
        if(Zchina_product_service.query.filter_by(product_id=pId, zchina_user_id=userId).first()):
            return True
        else:
            return False

    def buyProduct(self,pId=None,userId=None):
        info = Zchina_product_service(product_id=pId, zchina_user_id=userId)
        db.session.add(info)
        db.session.commit()
        return

    def orderList(self,userId=None):
        products = []
        pIds = db.session.query(Zchina_product_service.product_id).filter_by(zchina_user_id=userId).all()
        for data in pIds:
            pID = data[0]
            pro = Zchina_product.query.filter_by(id=pID).first()
            products.append(pro)
        return products


class solution:
    @classmethod
    def listAll(cls):
        solutions = Zchina_solution.query.all()
        return solutions


# 用户解决方案信息
class UserSolution:

    def sID_existed(self, sId=None,userId=None):
        if(Zchina_solution_service.query.filter_by(solution_id=sId, zchina_user_id=userId,).first()):
            return True
        else:
            return False


    @staticmethod
    def buySolution(sId=None,userId=None): #信息写入Zchina_solution_service数据表
        info = Zchina_solution_service(solution_id=sId, zchina_user_id=userId)
        db.session.add(info)
        db.session.commit()
        return

    def orderList(self,userId=None):
        solutions = []
        sIds = db.session.query(Zchina_solution_service.solution_id).filter_by(zchina_user_id=userId).all()
        for data in sIds:
            sID = data[0]
            sol = Zchina_solution.query.filter_by(id=sID).first()
            solutions.append(sol)
        return solutions



