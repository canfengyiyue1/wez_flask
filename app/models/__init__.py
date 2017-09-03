from . import smscode, user, zchina, zchina_article, zchina_artilce_cate,zchina_user,zchina_module_function,\
        zchina_module,zchina_product,zchina_solution,zchina_solution_service,zchina_user_auth,zchina_user_cert,\
        zchina_user_log,zchina_user_type,zchina_product_function_service,zchina_product_service,zchina_product_function

User = user.User
SmsCode = smscode.SmsCode
Zchina = zchina.Zchina
Zchina_article = zchina_article.Zchina_article
Zchina_article_cate = zchina_artilce_cate.Zchina_article_cate

all_models = {
        'User':User,
        'SmsCode':SmsCode,
        'Zchina':Zchina,
        'Zchina_article':Zchina_article,
        'Zchina_article_cate':Zchina_article_cate
        }
