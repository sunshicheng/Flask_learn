from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


# index页面路由,加上时间
@app.route('/')
def index():
    return render_template('index.html',current_time=datetime.utcnow())


# 拼接user页面路由
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name,current_time=datetime.utcnow())


# 404页面路由
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# 500页面路由
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    manager.run()
