from app import db
from .base import Base, decorator_some


class Zchina_user_auth(db.Model,Base): #实名认证表
    __tablename__ = Base.getTablename('zchina_user_auths')
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    weid = db.Column(db.String(60)) # 系统唯一ID
    zchina_user_id    = db.Column(db.Integer, db.ForeignKey('we_zchina_users.id'))
    id_number = db.Column(db.String(20)) #身份证
    name = db.Column(db.String(20)) #名字
    birthday = db.Column(db.String(20)) #生日
    sex = db.Column(db.String(10)) #性别
    address = db.Column(db.String(100)) #住址
    ID_photo_front = db.Column(db.String(255)) #身份证照正面
    ID_photo_back = db.Column(db.String(255)) #身份证照背面
    active = db.Column(db.Integer) # 实名认证状态  0 未认证  1 通过  2  审核中
    created_at = db.Column(db.Integer) #创建时间
    updated_at = db.Column(db.Integer) #更新时间



    @decorator_some
    def __init__(self, **kwargs):
        super(Zchina_user_auth,self).__init__(**kwargs)
