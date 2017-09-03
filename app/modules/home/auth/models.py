from app import login_manager
from app.models.zchina_user import Zchina_user as UserModel
from app.models.smscode import SmsCode as SmsModel


class User(UserModel):
    @classmethod
    def findByMobile(cls, mobile):
        return cls.query.filter_by(mobile=mobile).first()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class SmsCode(SmsModel):
    @classmethod
    def findSms(cls,mobile, code):
        return cls.query.filter_by(mobile=mobile,verify_code=code).order_by('id desc').first()
