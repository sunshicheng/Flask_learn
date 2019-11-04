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

from flask import Flask,render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
	return render_template('index.html')

#添加一个动态路由
@app.route('/user/<name>')
def user(name):
	return render_template('user.html',name=name)
