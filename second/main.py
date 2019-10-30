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



from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'hello!'

#添加一个动态路由
@app.route('/user/<name>')
def user(name):
	return 'hello,{}!'.format(name)
