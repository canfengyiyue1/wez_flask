from app import db
from .base import Base, decorator_some


class Zchina_module(db.Model,Base): #模块表
    __tablename__ = Base.getTablename('zchina_modules')
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    weid = db.Column(db.String(36)) #模块ID
    name = db.Column(db.String(50)) #模块名称
    displayname = db.Column(db.String(100))  # 模块显示名称
    description = db.Column(db.String(255))  # 描述
    type = db.Column(db.Integer) #分类
    status = db.Column(db.Integer) #状态
    created_at = db.Column(db.Integer) #创建时间
    updated_at = db.Column(db.Integer) #更新时间

    functions = db.relationship('Zchina_module_function', back_populates='module')

    @decorator_some
    def __init__(self, **kwargs):
        super(Zchina_module,self).__init__(**kwargs)
