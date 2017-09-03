from app import db
from .base import Base, decorator_some

class Zchina(db.Model,Base):
    __tablename__ = Base.getTablename('zchinas')
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    weid = db.Column(db.String(64))
    name = db.Column(db.String(60))
    manager = db.Column(db.String(60))
    domain = db.Column(db.String(60))
    start_at = db.Column(db.Integer) #开始时间
    end_at  = db.Column(db.Integer) #结束时间
    #article_cates = db.relationship('Zchina_article_cate',back_populates='zchina')
    #articles = db.relationship('Zchina_article',back_populates='zchina')


    @decorator_some
    def __init__(self, **kwargs):
        super(Zchina,self).__init__(**kwargs)


    def __repr__(self):
        return '<Zchina> %r' % self.name
