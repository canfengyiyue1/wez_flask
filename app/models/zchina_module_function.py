from app import db
from .base import Base, decorator_some


class Zchina_module_function(db.Model,Base): #功能表
    __tablename__ = Base.getTablename('zchina_module_functions')
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    weid = db.Column(db.String(36)) #功能ID
    module_id = db.Column(db.Integer, db.ForeignKey('we_zchina_modules.id'))
    name = db.Column(db.String(20)) #功能名称
    displayname = db.Column(db.String(100))  # 功能显示名称
    description = db.Column(db.String(200)) #描述
    status = db.Column(db.Integer,default=0) #状态
    created_at = db.Column(db.Integer) #创建时间
    updated_at = db.Column(db.Integer) #更新时间

    module = db.relationship('Zchina_module', back_populates='functions')

    @decorator_some
    def __init__(self, **kwargs):
        super(Zchina_module_function,self).__init__(**kwargs)

