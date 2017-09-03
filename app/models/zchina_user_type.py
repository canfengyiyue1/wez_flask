from app import db
from .base import Base

class Zchina_user_type(db.Model,Base): #用户类型表
    __tablename__ = Base.getTablename('zchina_user_types')
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    zchina_user_id    = db.Column(db.Integer, db.ForeignKey('we_zchina_users.id'))
    user_type_id = db.Column(db.Integer)
    user_type = db.Column(db.String(20)) #用户类型
