from app import db
from .base import Base


class Zchina_user_log(db.Model,Base): #用户操作日志表
    __tablename__ = Base.getTablename('zchina_user_logs')
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    zchina_user_id    = db.Column(db.Integer, db.ForeignKey('we_zchina_users.id'))
    user_operation = db.Column(db.Text) #用户操作
