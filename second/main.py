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

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())


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
