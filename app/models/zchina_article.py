from .. import db
from .base import Base,decorator_some

tablename = 'zchina_articles'

class Zchina_article(db.Model,Base):
    __tablename__ = Base.getTablename(tablename)
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    weid = db.Column(db.String(64))
    zchina_user_id    = db.Column(db.Integer, db.ForeignKey('we_zchina_users.id'))
    cate_id = db.Column(db.Integer, db.ForeignKey('we_zchina_article_cates.id'))
    title = db.Column(db.String(255))
    status = db.Column(db.SmallInteger, default=1)
    href = db.Column(db.String(255))
    source_url = db.Column(db.String(120))
    cover = db.Column(db.String(255))
    views = db.Column(db.Integer, default=0)
    summary = db.Column(db.String(255))
    content = db.Column(db.Text)
    created_at = db.Column(db.Integer) #创建时间
    updated_at = db.Column(db.Integer) #更新时间

    @decorator_some
    def __init__(self, **kwargs):
        super(Zchina_article,self).__init__(**kwargs)


    def __repr__(self):
        return '<%s> %s %s' % (tablename, self.name, self.uuid)
