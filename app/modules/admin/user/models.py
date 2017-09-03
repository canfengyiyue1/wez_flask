from app import login_manager
from app.models.zchina_user import Zchina_user as UserModel
from app.models.zchina_user_auth import Zchina_user_auth as UserAuthModel
from app.models.zchina_user_cert import Zchina_user_cert as UserCertModel


class User(UserModel):
    @classmethod
    def findByMobile(cls, mobile):
        return cls.query.filter_by(mobile=mobile).first()

    @classmethod
    def users(cls):
        return cls.query.all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class UserAuth(UserAuthModel):

    @classmethod
    def auths(cls):
        return cls.query.all()



class UserCert(UserCertModel):

    @classmethod
    def auths(cls):
        return cls.query.all()
