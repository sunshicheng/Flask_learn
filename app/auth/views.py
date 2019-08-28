"""
Author : sunshicheng 
DateTime : 19-8-28 下午9:42
FileName : views.py

身份验证蓝本中的路由和视图函数

"""

from flask import render_template
from . import auth

@auth.route('/login')
def login():
    return render_template('auth/login.html')