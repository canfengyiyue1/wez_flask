from app import db
from .base import Base, decorator_some

class Zchina_product(db.Model,Base):
    __tablename__ = Base.getTablename('zchina_products')
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    weid = db.Column(db.String(36))# 产品ID
    module_id = db.Column(db.Integer) #模块ID
    type = db.Column(db.Integer) #产品类别
    sort = db.Column(db.Integer) #同类产品升级顺序
    name = db.Column(db.String(20)) #产品名称
    displayname = db.Column(db.String(20))  # 产品显示名称
    description = db.Column(db.String(200)) #产品描述
    intro = db.Column(db.String(200)) #详情描述
    price = db.Column(db.String(20)) #产品价格  元/年
    forsale = db.Column(db.Integer) #开放销售 0 不开放 1 开放
    status = db.Column(db.Integer) #状态
    created_at = db.Column(db.Integer) #创建时间
    updated_at = db.Column(db.Integer) #更新时间

    functions = db.relationship('Zchina_product_function', back_populates='product')

    @decorator_some
    def __init__(self, **kwargs):
        super(Zchina_product,self).__init__(**kwargs)
