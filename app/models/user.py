from app import db, login_manager
from flask_login import UserMixin ,AnonymousUserMixin
from .base import Base, decorator_some

class User(UserMixin, db.Model,Base):
    __tablename__ = Base.getTablename('users')
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    weid = db.Column(db.String(50))
    mobile = db.Column(db.String(15), unique=True, index=True)
    name = db.Column(db.String(20)) #姓名
    sex = db.Column(db.String(2)) #性别
    ethnicity = db.Column(db.String(255)) #民族
    birth = db.Column(db.String(30)) #出生日期
    id_number = db.Column(db.String(20))  #身份证号
    id_card_front = db.Column(db.Text) #身份证正面图片
    authority = db.Column(db.String(50))#签发机关
    valid_period_start = db.Column(db.String(30)) #有效期 起始时间
    valid_period_end = db.Column(db.String(30)) #有效期 结束时间
    status = db.Column(db.Integer,default=1) #用户状态 1正常
    avatar = db.Column(db.Text) #头像图片
    intro = db.Column(db.String(200)) #个人简介
    email = db.Column(db.String(30)) # 邮箱
    origo = db.Column(db.String(255)) #籍贯
    country = db.Column(db.String(255)) #国家
    province = db.Column(db.String(50)) #身份证：省
    city = db.Column(db.String(50))  #身份证：市
    id_check_num = db.Column(db.Integer,default=0) #被查询次数
    position = db.Column(db.String(50)) #现职位
    organization = db.Column(db.String(50)) #所在单位
    manual_status = db.Column(db.Integer,default=1) #认证状态 1,未认证 2，审核中，3，已认证
    created_at = db.Column(db.Integer) #创建时间
    updated_at = db.Column(db.Integer) #更新时间

    @decorator_some
    def __init__(self, **kwargs):
        super(User,self).__init__(**kwargs)

    @classmethod
    def findByMobile(cls, mobile):
        return cls.query.filter_by(mobile=mobile).first()

    def __repr__(self):
        return '<User> %r' % self.mobile

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

