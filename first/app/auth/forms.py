"""
Author: sunshicheng
Datetime: 2019/8/29 下午6:43
File : forms.py

登录表单

"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(FlaskForm):
    email = StringField('邮箱:', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('密码:', validators=[DataRequired])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')
