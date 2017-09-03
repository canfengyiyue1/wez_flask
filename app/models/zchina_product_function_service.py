from app import db
from .base import Base, decorator_some

class Zchina_product_function_service(db.Model,Base):
    __tablename__ = Base.getTablename('zchina_product_function_services')
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    weid = db.Column(db.String(36))
    orig_product_value_id = db.Column(db.String(50)) #产品功能 id
    type = db.Column(db.Integer) #分类
    product_id  = db.Column(db.Integer, db.ForeignKey('we_zchina_products.id'))
    function_id    = db.Column(db.Integer, db.ForeignKey('we_zchina_product_functions.id'))
    module_function_id   = db.Column(db.Integer, db.ForeignKey('we_zchina_module_functions.id'))
    zchina_user_id    = db.Column(db.Integer, db.ForeignKey('we_zchina_users.id'))
    plat_id = db.Column(db.Integer)
    start_at = db.Column(db.Integer) #开始时间
    end_at  = db.Column(db.Integer) #结束时间
    status = db.Column(db.Integer) #状态 1 正常 2 关闭
    created_at = db.Column(db.Integer) #创建时间
    updated_at = db.Column(db.Integer) #更新时间


    @decorator_some
    def __init__(self, **kwargs):
        super(Zchina_product_function_service,self).__init__(**kwargs)
