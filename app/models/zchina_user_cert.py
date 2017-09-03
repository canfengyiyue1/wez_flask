from app import db
from .base import Base,decorator_some

class Zchina_user_cert(db.Model,Base): #微众企业认证
    __tablename__ = Base.getTablename('zchina_user_certs')
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    weid = db.Column(db.String(64))  #系统唯一ID
    zchina_user_id    = db.Column(db.Integer, db.ForeignKey('we_zchina_users.id'))
    name = db.Column(db.String(100)) #企业名称
    address = db.Column(db.String(200)) #企业地址
    nature = db.Column(db.String(255)) #企业性质
    license = db.Column(db.String(255))  #企业执照
    authorization = db.Column(db.String(255)) # 授权书
    active = db.Column(db.Integer) # 企业认证状态  0 未认证  1 通过  2  审核中



    @decorator_some
    def __init__(self, **kwargs):
        super(Zchina_user_cert,self).__init__(**kwargs)
