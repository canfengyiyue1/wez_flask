from app import db
from .base import Base,decorator_some

class Zchina_solution(db.Model,Base): #解决方案
    __tablename__ = Base.getTablename('zchina_solutions')
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    weid = db.Column(db.String(36))
    config = db.Column(db.Text) #解决方案详细配置
    type = db.Column(db.Integer) #分类
    sort = db.Column(db.Integer) #同类解决方案升级
    name = db.Column(db.String(20))  # 产品名称
    displayname = db.Column(db.String(20))  # 方案显示名称
    description = db.Column(db.String(200))  # 方案描述
    intro = db.Column(db.String(200))  # 详情描述
    price = db.Column(db.String(20))  # 产品价格  元/年
    forsale = db.Column(db.Integer)  # 开放销售 0 不开放 1 开放
    status = db.Column(db.Integer)  # 状态
    created_at = db.Column(db.Integer) #创建时间
    updated_at = db.Column(db.Integer) #更新时间


    @decorator_some
    def __init__(self, **kwargs):
        super(Zchina_solution,self).__init__(**kwargs)
