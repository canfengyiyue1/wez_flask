from app import db
from .base import Base, decorator_some

class Zchina_solution_service(db.Model,Base):
    __tablename__ = Base.getTablename('zchina_solution_services')
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    weid = db.Column(db.String(36))
    zchina_user_id    = db.Column(db.Integer, db.ForeignKey('we_zchina_users.id'))#所属用户ID
    solution_id = db.Column(db.Integer, db.ForeignKey('we_zchina_solutions.id'))#
    config = db.Column(db.Text) #解决方案详细配置
    plat_id = db.Column(db.Integer)
    type = db.Column(db.Integer) #分类
    start_at = db.Column(db.Integer)  # 开始时间
    end_at = db.Column(db.Integer)  # 结束时间
    status = db.Column(db.Integer) #状态
    created_at = db.Column(db.Integer) #创建时间
    updated_at = db.Column(db.Integer) #更新时间


    @decorator_some
    def __init__(self, **kwargs):
        super(Zchina_solution_service,self).__init__(**kwargs)
