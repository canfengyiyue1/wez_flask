from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError

class LoginForm(FlaskForm):
    mobile = StringField('Mobile', validators = [Required(), Length(1,11)])
    sms_code = StringField('Code',validators = [Required()])
    submit = SubmitField('Log In')
