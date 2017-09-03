from app import db
from .base import Base, decorator_some

class Zchina_product_service(db.Model,Base):
    __tablename__ = Base.getTablename('zchina_product_services')
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    weid = db.Column(db.String(36))
    solution_id = db.Column(db.String(36))  #解决方案标识ID
    module_id = db.Column(db.String(36)) # 模块唯一ID
    zchina_user_id = db.Column(db.String(36)) #所属用户ID
    product_id  = db.Column(db.Integer, db.ForeignKey('we_zchina_products.id'))
    plat_id = db.Column(db.String(36))
    start_at = db.Column(db.String(30)) #开始时间
    end_at = db.Column(db.String(30))  #结束时间
    status = db.Column(db.Integer) #状态
    created_at = db.Column(db.Integer) #创建时间
    updated_at = db.Column(db.Integer) #更新时间



    @decorator_some
    def __init__(self, **kwargs):
        super(Zchina_product_service,self).__init__(**kwargs)
