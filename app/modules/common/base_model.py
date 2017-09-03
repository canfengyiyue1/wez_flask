from app import db
db_pre = 'we_'
class Base():
    @staticmethod
    def getTablename(tablename):
        return db_pre + tablename
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self


