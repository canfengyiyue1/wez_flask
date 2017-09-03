from app import db
from .base import Base, decorator_some

tablename = 'zchina_article_cates'

class Zchina_article_cate(db.Model,Base):
    __tablename__ = Base.getTablename(tablename)
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(60))
    en_name = db.Column(db.String(60))
    zchina_user_id    = db.Column(db.Integer, db.ForeignKey('we_zchina_users.id'))
    #zchina = db.relationship('Zchina', back_populates='article_cates')

    @decorator_some
    def __init__(self, **kwargs):
        super(Zchina_article_cate,self).__init__(**kwargs)

    def __repr__(self):
        return '<%s> %r' % (tablename, self.name)
