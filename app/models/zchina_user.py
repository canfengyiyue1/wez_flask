from app import db, login_manager
from .base import Base,decorator_some, decorator_wechina_id
from flask_login import UserMixin ,AnonymousUserMixin

class Zchina_user(UserMixin, db.Model,Base): #主站用户表
    __tablename__ = Base.getTablename('zchina_users')
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)  # 系统唯一ID
    weid = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('we_users.id'))
    wezchina_id = db.Column(db.Integer, db.ForeignKey('we_zchinas.id'))
    real_name = db.Column(db.String(30)) #用户名
    mobile =  db.Column(db.String(20)) #手机号
    balance = db.Column(db.Float(0.0),default=0.0) #余额
    nickname = db.Column(db.String(30)) #用户昵称
    wx_open_id = db.Column(db.String(255)) #微信open ID
    user_type_id = db.Column(db.Integer) #用户类型
    zchina_cert = db.Column(db.Integer,default=0) #微众认证
    zchian_auth = db.Column(db.Integer,default=0) # 实名认证
    solutions_id = db.Column(db.Integer) #解决方案id
    active = db.Column(db.Integer,default=1) #用户状态 ：0 删除，1有效，2 封停，3 在线，4 离线
    created_at = db.Column(db.Integer) #创建时间
    updated_at = db.Column(db.Integer) #更新时间

    @decorator_some
    def __init__(self, **kwargs):
        super(Zchina_user,self).__init__(**kwargs)


    @classmethod
    def findByMobile(cls, mobile):
        return cls.query.filter_by(mobile=mobile).first()

    def __repr__(self):
        return '<Zchina_user> %r' % self.mobile




@login_manager.user_loader
def load_user(user_id):
    return Zchian_user.query.get(int(user_id))
