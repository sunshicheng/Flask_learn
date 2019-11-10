"""
第一版的完整文件

"""

import os
from flask_mail import Mail
from threading import Thread
from datetime import datetime
from flask_mail import Message
from flask_moment import Moment
from flask_wtf import FlaskForm
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField
from flask import Flask, render_template, session, redirect, url_for, flash

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# session验证
app.config['SECRET_KEY'] = 'hard to guess string'
# 链接数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqllite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 使用邮件
app.config['MAIL_SERVER'] = 'smtp.exmail.qq.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <sunshicheng@xiaozhu.com>'
app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')

mail = Mail(app)
db = SQLAlchemy(app)
moment = Moment(app)
bootstrap = Bootstrap(app)
migrate = Migrate(app, db)


class NameForm(FlaskForm):
    name = StringField('输入姓名', validators=[DataRequired()])
    submit = SubmitField('提交')


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


def send_async_email(app, msg):
    with app.app_context():
        mail.send_message(msg)


def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email(), args=[app, msg])
    thr.start()
    return thr


# index页面路由,加上时间,视图操作函数添加
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
            if app.config['FLASKY_ADMIN']:
                send_email(app.config['FLASKY_ADMIN'], 'New User', 'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        # form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', current_time=datetime.utcnow(), form=form, name=session.get('name'),
                           known=session.get('known', False))


# 拼接user页面路由
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name, current_time=datetime.utcnow())


# 404页面路由
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# 500页面路由
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)


if __name__ == '__main__':
    app.run()
