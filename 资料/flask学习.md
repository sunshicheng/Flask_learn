### 知识点总结 

1. 源码地址：<[https://github.com/miguelgrinberg/flasky](<https://github.com/miguelgrinberg/flasky>)>
2. 四个常用的前置或者之后要处理的函数
   - before_first_request : 在处理第一个请求之前运行
   - before_request:  在每次请求之前运行
   - after_request:  如果没有异常抛出，在每次请求之后运行
   - teardown_request:  即使有异常抛出，也在每次请求之后运行
3. 安装插件 flask-script,pip install flask-script
4. 重定向函数，redirect()，一般状态码是302
5. 特殊的函数abort(),用于处理报错。
6. 使用了python-script来启动服务，用manage.run(app)来启动服务。
   - 启动服务命令 ：python hello.py runserver --host 0.0.0.0
7. jinia过滤器的使用
8. 开启debug模式：export FLASK_DEBUG=1
9. flask启动方法
   - 使用python main.py runserver
   - 先export FLASK_APP=hello.py，然后执行flask run

10. markdown编辑器也可以使用zelttlr
11. 数据库操作
    - db.session.add() 增加数据到缓存 -> db.session.commit()提交数据到数据库
    - 删除行 db.session.delete() -> db.session.commit()
 12. 迁移数据库操作：
    - 创建迁移仓库：flask db init
    - 自动创建迁移脚本：flask db migrate -m "initial migration"
    - 更新数据库： flask db upgrade
 13. flask集成邮件




### 操作流程



1. ```
   1. 下载flask-script 用于传入命令行参数
   2. 下载flask-bootstrap 用于使用bootstrap模板(http://getbootstrap.com)
   3. 下载 flask-moment 格式化本地时间(http://momentjs.com/docs/#/displaying/)
   4. Flask-WTF(http://pythonhosted.org/Flask-WTF/)扩展可以把处理 Web 表单的过程变成一
      种愉悦的体验。这个扩展对独立的 WTForms(http://wtforms.simplecodes.com)包进行了包
      装,方便集成到 Flask 程序中。
   5. pip install flask_wtf 模板操作
   6. pip install flask-sqlalchemy 链接数据库
   7. pip install flask-migrate 迁移数据库
   8. pip install flask-mail 电子邮件支持
   ```

