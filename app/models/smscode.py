from app import db
from .base import Base, decorator_some


class SmsCode(db.Model, Base):
    __tablename__ = Base.getTablename('sms_codes')
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    wezchina_id = db.Column(db.Integer)
    mobile = db.Column(db.String(15))
    verify_code = db.Column(db.String(15))
    created_at = db.Column(db.Integer)
    client_ip = db.Column(db.String(20))

    @decorator_some
    def __init__(self, **kwargs):
        super(SmsCode,self).__init__(**kwargs)

    def __repr__(self):
        return "<SmsCode> (mobile='%s',verify_code='%s')" % (self.mobile, self.verify_code)
