"""
Author : sunshicheng 
DateTime : 19-8-28 下午9:42
FileName : views.py

身份验证蓝本中的路由和视图函数

"""
from . import auth
from ..models import User
from .forms import LoginForm
from flask_login import login_user, login_required, logout_user
from flask import render_template, redirect, request, url_for, flash


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        flash('用户名或者密码错误')
    return render_template('auth/login.html', form=form)


# @auth.route('/logout')
# @login_required()
# def logout():
#     logout_user()
#     flash('你已经退出了。')
#     return redirect(url_for('main.index'))
