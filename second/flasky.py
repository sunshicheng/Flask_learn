"""
1. 路由的基本写法
@app.route('/')
def index():
	return 'hello '

2. 和上诉相同功能的写法
app.add_url_rule('/', 'index', index)

3. 写成动态的路由
@app.route('/user/<name>')
def user(name):
	return 'hello,{}'.formate(name)
"""

from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
# 格式化时间
from flask_moment import Moment
from datetime import datetime
# 表单验证
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(FlaskForm):
    name = StringField('输入姓名', validators=[DataRequired()])
    submit = SubmitField('提交')


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        # 第一次不做处理
        # name = form.name.data
        # form.name.data = ''
        session['name'] = form.name.data
        return redirect(url_for('index'))
    #return render_template('index.html', current_time=datetime.utcnow(), form=form, name=name))
    return render_template('index.html', current_time=datetime.utcnow(), form=form, name=session.get('name'))


# 添加一个动态路由
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
