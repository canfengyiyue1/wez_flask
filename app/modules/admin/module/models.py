from app.models.zchina_user import Zchina_user as UserModel
from app.models.zchina_module import Zchina_module as ModuleModel
from app.models.zchina_module_function import Zchina_module_function as FunctionModel


class Module(ModuleModel):
    @classmethod
    def users(cls):
        return cls.query.all()


class Function(FunctionModel):
    @classmethod
    def auths(cls):
        return cls.query.all()


