from app.models.zchina_user import Zchina_user as UserModel
from app.models.zchina_product import Zchina_product as ProductModel
from app.models.zchina_product_function import Zchina_product_function as FunctionModel
from app.models.zchina_product_service import Zchina_product_service as ServiceModel
from app.models.zchina_module import Zchina_module as ModuleModel


class Product(ProductModel):
    @classmethod
    def users(cls):
        return cls.query.all()


class Function(FunctionModel):
    @classmethod
    def auths(cls):
        return cls.query.all()

class Service(ServiceModel):
    @classmethod
    def auths(cls):
        return cls.query.all()

class Module(ModuleModel):
    @classmethod
    def users(cls):
        return cls.query.all()
