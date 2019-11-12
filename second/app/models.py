"""
Author : sunshicheng 
DateTime : 19-8-7 下午8:55
FileName : models.py

"""

from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError('密码不是可读属性！')

    @password.setter
    # 通过generate_password_hash()生成密码，变成不可读属性
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        # 只接受一个参数，就是密码
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username


# 注册给Flask-login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
