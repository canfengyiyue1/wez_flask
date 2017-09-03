from flask import current_app, g
from flask_login import login_user
from .import auth
from .models import User,SmsCode
from app import db


def mobileLogin(form):
    if form.validate_on_submit():
        sms_code = SmsCode.findSms(form.mobile.data,form.sms_code.data)
        if sms_code is None:
            return ('Invalid verify_code')
        user = User.findByMobile(form.mobile.data)
        if user is None:
            user = mobileReg(form.mobile.data)
        g.user = user
        login_user(user, True)
        return False


def mobileReg(mobile):
    user = User(mobile=mobile)
    user.save()
    return user


