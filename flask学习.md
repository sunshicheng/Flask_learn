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
        14. flask管理已经登录的用户会话
        15. flask修改成项目




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
   9. pip install flask-login 使用flask-login验证用户身份
   ```

### 书中的知识点记录：

##### 第二章

1. flask --help

2. flask run --help

3. flask shell

4. 应用上下文和请求上下文

   | 变量名      | 上下文     | 说明                                                   |
   | ----------- | ---------- | ------------------------------------------------------ |
   | current_app | 应用上下文 | 当前应用的应用实例                                     |
   | g           | 应用上下文 | 处理请求时用作临时存储的对象，每次请求时都会重设这个值 |
   | reuqest     | 请求上下文 | 请求对象，封装了客户端发出的http请求的内容             |
   | session     | 请求上下文 | 用户会话，值为一个字典，存储请求之间需要记住的值       |

   

5. flask 请求对象

   | 属性或方法   | 说明                                                         |
   | ------------ | ------------------------------------------------------------ |
   | form         | 一个字典，存储请求提交的所有表单字段                         |
   | args         | 一个字典，存储通过url查询字符串传递的所有参数                |
   | values       | 一个字典，from和args的合集                                   |
   | cookies      | 一个字典，存储请求的所有cookie                               |
   | headers      | 一个字典，存储请求的所有http首部                             |
   | files        | 一个字典，存储请求上传的所有文件                             |
   | get_data()   | 返回请求主体缓冲的数据                                       |
   | get_json()   | 返回一个Python字典，包含解析请求主体后得到的json             |
   | blueprint    | 处理请求的flask蓝本的名称                                    |
   | endpoint     | 处理请求的flask端点的名称，flask把视图函数的名称用作路由端点的名称 |
   | method       | http请求方法                                                 |
   | scheme       | url方案（http或者https）                                     |
   | is_secure()  | 通过安全的链接（https）发送请求返回True                      |
   | host         | 请求定义的主机名。如果客户端定义了端口号，还包括端口号       |
   | path         | url的路径部分                                                |
   | query_string | url的查询字符串的部分，返回原始二进制值                      |
   | full_path    | url的路径和查询字符串部分                                    |
   | url          | 客户端请求的完整url                                          |
   | base_url     | 同url，但是没有查询字符串的部分                              |
   | remote_addr  | 客户端的IP地址                                               |
   | environ      | 请求原始的WSGI环境字典                                       |

   

6. flask请求钩子

   - before_request 注册一个函数，在每次请求之前运行
   - before_first_request 注册一个函数，只在处理第一个请求之前运行，可以通过这个钩子添加服务器初始化任务。
   - after_request，注册一个函数，如果没有未处理的异常，在每次请求之后运行。
   - teardown_request，注册一个函数，即使有未处理的异常抛出，也在每次请求之后运行。

7. Flask响应对象

   | 属性或方法      | 说明                                         |
   | --------------- | -------------------------------------------- |
   | status_code     | HTTP数字状态码                               |
   | headers         | 一个类似字典的对象，包含随响应发送的所有首部 |
   | set_cookies()   | 为响应添加一个cookie                         |
   | delete_cookie() | 删除一个cookie                               |
   | content_length  | 响应主体的长度                               |
   | content_type    | 响应主体的媒体类型                           |
   | set_data()      | 使用字符串或字节值设定响应                   |
   | get_data()      | 获取响应主体                                 |

   redirect()，重定向

   abort()，处理错误报错

8. Flask扩展

##### 第三章

1. Jinja模板渲染templates目录

2. Jinja模板的变量

   - Jinja能识别所有类型的变量，例如，字典，列表，和对象。

   - 变量可以使用**过滤器**修改,过滤器是在变量名之后，二者之间以竖线分割。{{name|capitalize}}

   - Jinja变量过滤器

     | 过滤器名   | 说明                                       |
     | ---------- | ------------------------------------------ |
     | safe       | 渲染时不转义                               |
     | capitalize | 把值的首字母转换成大写，其他字母转换成小写 |
     | lower      | 把值转换成小写形式                         |
     | upper      | 把值转换成大写形式                         |
     | title      | 把值中每个单词的首字母都转换成大写         |
     | trim       | 把值的首尾空格删掉                         |
     | striptags  | 渲染之前把值中所有的HTML标签都删掉         |

3. 控制结构

   - 条件判断语句

     ```html
     {% if user %}
     	hello ,{{user}}
     {% else %}
     	hello,stranger.
     {% endif %}
     ```

     

   - for循环

     ```html
     <ul>
     	{% for commet in comment %}
     		<li>{{comment}}</li>
     	{% endfor %}
     </ul>
     ```

     

   - 宏定义，相当于python的函数

     ```html
     {% macro render_comment(comment) %}
     	<li>{{comment}}</li>
     {% endmacro %}
     <ul>
         {% for ccomment in ccomment %}
         	{% render_comment(comment) %}
         {% endfor %}
     </ul> 
     ```

     

   - 模板，需要一个base.html，然后使用extends去继承这个页面。

4. 使用flask-bootstrap集成bootstrap，使用pip install flask-bootstrap。bootstrap的base.html可以使用的区块如下。如果需要覆盖原来的css和js需要使用super()函数来完成。

   | 区块名       | 说明                       |
   | ------------ | -------------------------- |
   | doc          | 整个HTML文档               |
   | html_attribs | <html>标签的属性           |
   | html         | <html>标签中的内容         |
   | head         | <head>标签中的内容         |
   | title        | <title>标签中的内容        |
   | metas        | 一组<meta>标签             |
   | styles       | css声明                    |
   | body_attribs | <body> 标签的属性          |
   | body         | <body> 标签中的内容        |
   | navbar       | 用户定义的导航栏           |
   | content      | 用户定义的页面内容         |
   | scripts      | 文档底部的 JavaScript 声明 |

5. 自定义错误页面

6. 使用Flask-Moment本地化时间，Flask-Moment 实 现 了 Moment.js 的 format()、fromNow()、fromTime()、calendar()、valueOf()和 unix() 等方法。请查阅 Moment.js 的文档(http://momentjs.com/docs/#/displaying/)。

#### 第四章 web表单

1. 使用flask_wtf ,pip install flask_wtf。

2. WTForms相关支持:

   - WTForms支持的HTML标准字段

     | 字段类型            | 说明                                  |
     | ------------------- | ------------------------------------- |
     | BooleanField        | 复选框，值为 True 和 False            |
     | DateField           | 文本字段，值为 datetime.date 格式     |
     | DateTimeField       | 文本字段，值为 datetime.datetime 格式 |
     | DecimalField        | 文本字段，值为 decimal.Decimal        |
     | FileField           | 文件上传字段                          |
     | HiddenField         | 隐藏的文本字段                        |
     | MultipleFileField   | 多文件上传字段                        |
     | FieldList           | 一组指定类型的字段                    |
     | FloatField          | 文本字段，值为浮点数                  |
     | FormField           | 把一个表单作为字段嵌入另一个表单      |
     | IntegerField        | 文本字段，值为整数                    |
     | PasswordField       | 密码文本字段                          |
     | RadioField          | 一组单选按钮                          |
     | SelectField         | 下拉列表                              |
     | SelectMultipleField | 下拉列表，可选择多个值                |
     | SubmitField         | 表单提交按钮                          |
     | StringField         | 文本字段                              |
     | TextAreaField       | 多行文本字段                          |

     

   - WTForms验证函数

     | 验证函数      | 说明                                                  |
     | ------------- | ----------------------------------------------------- |
     | DataRequired  | 确保转换类型后字段中有数据                            |
     | Email         | 验证电子邮件地址                                      |
     | EqualTo       | 比较两个字段的值;常用于要求输入两次密码进行确认的情况 |
     | InputRequired | 确保转换类型前字段中有数据                            |
     | IPAddress     | 验证 IPv4 网络地址                                    |
     | Length        | 验证输入字符串的长度                                  |
     | MacAddress    | 验证 MAC 地址                                         |
     | NumberRange   | 验证输入的值在数字范围之内                            |
     | Optional      | 允许字段中没有输入，将跳过其他验证函数                |
     | Regexp        | 使用正则表达式验证输入值                              |
     | URL           | 验证 URL                                              |
     | UUID          | 验证 UUID                                             |
     | AnyOf         | 确保输入值在一组可能的值中                            |
     | NoneOf        | 确保输入值不在一组可能的值中                          |

     

3. 把表单渲染成HTML

4. 重定向和用户会话，处理刷新的时候的弹窗，并且记住用户的session信息，这样才能保证数据在新的页面

5. 消息闪现，flash和get_flashed_messages()来完成。



#### 第五章 数据库

1. 关系型数据库和非关系型数据库。

2. 使用Flask-SQLAlchemy 管理数据库

   | 数据库引擎 | URL                                               |
   | ---------- | ------------------------------------------------- |
   | MySQL      | mysql://username:password@hostname/database       |
   | Postgres   | postgressql://username:password@hostname/database |
   | SQLite     | sqlite:////absolute/path/database                 |

   hotname表示数据库所在的主机。

3. 常用的SQLAlchemy列类型

   | 类型名       | Python类型         | 说明                                                       |
   | ------------ | ------------------ | ---------------------------------------------------------- |
   | Integer      | int                | 普通整数，通常是 32 位                                     |
   | SmallInteger | int                | 取值范围小的整数，通常是 16 位                             |
   | BigInteger   | int 或 long        | 不限制精度的整数                                           |
   | Float        | float              | 浮点数                                                     |
   | Numeric      | decimal.Decimal    | 定点数                                                     |
   | String       | str                | 变长字符串                                                 |
   | Text         | str                | 变长字符串，对较长或不限长度的字符串做了优化               |
   | Unicode      | unicode            | 变长 Unicode 字符串                                        |
   | UnicodeText  | unicode            | 变长 Unicode 字符串，对较长或不限长度的字符串<br/>做了优化 |
   | Boolean      | bool               | 布尔值                                                     |
   | Date         | datetime.date      | 日期                                                       |
   | Time         | datetime.time      | 时间                                                       |
   | DateTime     | datetime.datetime  | 日期和时间                                                 |
   | Interval     | datetime.timedelta | 时间间隔                                                   |
   | Enum         | str                | 一组字符串                                                 |
   | PickleType   | 任何 Python 对象   | 自动使用 Pickle 序列化                                     |
   | LargeBinary  | str                | 二进制 blob                                                |

   

4. 常用的SQLAlchemy列选项

   | 选项名      | 说明                                                         |
   | ----------- | ------------------------------------------------------------ |
   | primary_key | 如果设为 True，列为表的主键                                  |
   | unique      | 如果设为 True，列不允许出现重复的值                          |
   | index       | 如果设为 True，为列创建索引，提升查询效率                    |
   | nullable    | 如果设为 True，列允许使用空值;如果设为 False，列不允许使用空值 |
   | default     | 为列定义默认值                                               |

   

5. 关系，SQLAlchemy关系选项

   | 选项名        | 说明                                                         |
   | ------------- | ------------------------------------------------------------ |
   | backref       | 在关系的另一个模型中添加反向引用                             |
   | primaryjoin   | 明确指定两个模型之间使用的联结条件;只在模棱两可的关系中需要指定 |
   | lazy          | 指定如何加载相关记录，可选值有 select(首次访问时按需加载)、immediate(源对象<br/>加载后就加载)、joined(加载记录，但使用联结)、subquery(立即加载，但使用子查
询)，noload(永不加载)和 dynamic(不加载记录，但提供加载记录的查询) |
   | uselist       | 如果设为 False，不使用列表，而使用标量值                     |
   | order_by      | 指定关系中记录的排序方式                                     |
   | secondary     | 指定多对多关系中关联表的名称                                 |
   | secondaryjoin | SQLAlchemy 无法自行决定时，指定多对多关系中的二级联结条件    |

   

6. 数据库操作