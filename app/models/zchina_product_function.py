from app import db
from .base import Base, decorator_some

class Zchina_product_function(db.Model,Base):
    __tablename__ = Base.getTablename('zchina_product_functions')
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    weid = db.Column(db.String(36))
    product_id  = db.Column(db.Integer, db.ForeignKey('we_zchina_products.id'))
    module_function_id   = db.Column(db.Integer, db.ForeignKey('we_zchina_module_functions.id'))
    type = db.Column(db.Integer) #分类
    name = db.Column(db.String(20)) #功能名称
    displayname = db.Column(db.String(20))  # 功能显示名称
    description = db.Column(db.String(255)) #功能简介
    intro = db.Column(db.Text) #功能详情
    price = db.Column(db.String(20)) #产品价格  元/年
    forsale = db.Column(db.Integer) #开放销售 0 不开放 1 开放
    status = db.Column(db.Integer) #状态 1 正常 2 关闭
    created_at = db.Column(db.Integer) #创建时间
    updated_at = db.Column(db.Integer) #更新时间

    product = db.relationship('Zchina_product', back_populates='functions')


    @decorator_some
    def __init__(self, **kwargs):
        super(Zchina_product_function,self).__init__(**kwargs)
