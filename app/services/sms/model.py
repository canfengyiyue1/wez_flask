from app.models.smscode import SmsCode as Model

class SmsCode(Model):
    @classmethod
    def findSms(cls,mobile, code):
        return cls.query.filter_by(mobile=mobile,verify_code=code).order_by('id desc').first()


