from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextField, SelectField,HiddenField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError

class ProductForm(FlaskForm):
    id = HiddenField('id',default=0)
    module_id = HiddenField('module_id',default=0)
    sort = HiddenField('sort',default=0)
    name = StringField('名称',validators = [Required()])
    displayname = StringField('显示名称',validators = [Required()])
    description = TextField('简介',validators = [Required()])
    intro = TextField('内容',validators = [Required()])
    price = StringField('价格',validators = [Required()])
    status = StringField('状态',validators = [Required()])
    forsale = StringField('是否卖出',validators = [Required()])
    type = SelectField('类型',choices=[['1','type1'],['2','type2']])
    submit = SubmitField('保存')


class FunctionForm(FlaskForm):
    id = HiddenField('id',default=0)
    module_id = HiddenField('module_id',default=0)
    name = StringField('名称',validators = [Required()])
    displayname = StringField('显示名称',validators = [Required()])
    description = StringField('简介',validators = [Required()])
    submit = SubmitField('保存')

class ServiceForm(FlaskForm):
    id = HiddenField('id',default=0)
    module_id = HiddenField('module_id',default=0)
    name = StringField('名称',validators = [Required()])
    displayname = StringField('显示名称',validators = [Required()])
    description = StringField('简介',validators = [Required()])
    submit = SubmitField('保存')
