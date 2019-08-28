"""
Author : sunshicheng 
DateTime : 19-8-28 下午9:38
FileName : __init__.py.py

创建身份验证蓝本
"""

from flask import Blueprint

auth = Blueprint('auth',__name__)

from . import views

