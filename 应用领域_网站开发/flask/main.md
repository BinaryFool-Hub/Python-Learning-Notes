# 基础路由及启动

```python
from flask import Flask  # flask的核心类

# 初始化web应用程序的示例对象,入口默认使用__name__作为主要入口
app = Flask(__name__)


# 通过实例化对象提供的route路由装饰器绑定视图与url地址的关系,函数即视图
@app.route("/")
def index():
    # 默认flask支持函数视图，视图名称不能重复
    # 视图的返回值将被flask包装成响应对象的HTML文档内容，返回给客户端
    return "hello flask"


if __name__ == '__main__':
    """
    启动实例化对象,即flask全栈
    host: 允许被访问的ip，0.0.0.0表示任意主机
    port: 全栈的运行端口，默认5000
    """
    app.run(host='0.0.0.0', port=5000)
```

# 项目加载配置

## 方式一

直接在实例化对象下面定义

```python
from flask import Flask

app = Flask(__name__)

# 想更改多个
config = {
    'DEBUG': True
}
app.config.update(config)

# 只想改一个
# app.config['DEBUG'] = True
```

## 方式二

来自python文件的类对象

```python
"""配置，类对象"""


class Settings(object):
    DEBUG = True
```

```python
"""flask实例"""
from flask import Flask
from settings import Setting

app = Flask(__name__)

# 来自类对象的设置
app.config.from_object(Setting)
```

## 方式三

来自python文件的变量和值

```python
"""配置，python文件"""
DEBUG = True
```

```python
"""flask实例"""
from flask import Flask

app = Flask(__name__)

# 来自python文件的配置
app.config.from_pyfile('setting.py')
```

# 路由配置

## 路由地址和请求方法

```python
from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

"""
装饰器的参数：
    rule: 当前视图地址,/表示根目录
    methods: 当前视图允许的请求方法，不区分大小写，不写默认是GET
"""


@app.route(rule="/", methods=['GET', 'POST'])
def index():
    return "hello flask"


if __name__ == '__main__':
    app.run()
```

## 路由参数接收

- 支持的类型有
    - string（默认）：不包含 / 的任意字符串。
    - int：正整数。
    - float：浮点数。
    - path：类似 string，但可以包含 /。
    - uuid：UUID 对象。

```python
from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

"""
在rule路由地址中可以写想要接收的变量，如果没用限制数据类型默认返回字符串:/<data>
限制数据类型请求也很简单，只需要在里面加一个数据类型即可：/<int:number>
"""


@app.route(rule="/<data>/<int:number>", methods=['GET', 'POST'])
def index(data, number):
    print(data, number)
    return "hello flask"


if __name__ == '__main__':
    app.run()
```

## 自定义路由参数转换

在开发中路由参数接收支持的类型中，虽然可以接收字符串，但可能会不能满足我们的需求，但那么这个时候就需要用到正则匹配，根据自己的规则去限定请求参数再进行访问

```python
"""类型转换器，一般都放于单独文件中"""

# 导入基类
from werkzeug.routing.converters import BaseConverter


# 定义路由参数转换器类
class SmsConverter(BaseConverter):
    # 这写你要匹配的正则表达式即可
    regex = r'1[3-9]\d{9}'
```

```python
"""flask全栈，注册和使用"""

from flask import Flask
from converters import SmsConverter  # 导入写好的转换器

app = Flask(__name__)
app.config['DEBUG'] = True

# 注册到flask实例对象
app.url_map.converters['sms'] = SmsConverter


# 使用和常规的一样
@app.route(rule="/<sms:number>", methods=['GET', 'POST'])
def index(number):
    print(type(number))  # str
    print(number)
    return "hello flask"
```

# 数据请求及响应

## 请求

获取客户端请求携带的信息需要导入request方法来获取，直接在视图下面操作即可

```python
"""
导入request方法可以获取到客户端携带的请求信息
"""
from flask import Flask, request

app = Flask(__name__)


@app.route("/index")
def index():
    """获取请求信息方法"""
    print(request)  # 里面有很多方法可以使用

    return "success"


if __name__ == '__main__':
    app.run(host="0.0.0.0")
```

### 获取请求方法

```python
from flask import request

"""获取本次请求的方法"""
print(request.method)
```

### 获取请求url

```python
from flask import request

"""获取本次请求url"""
print(request.url)  # 完整url
print(request.path)  # 路由的路径
```

### 获取请求头信息

```python
from flask import request

print(request.headers)  # 可以当成字典取值
```

### 获取用户客户端环境信息

```python
from flask import request

print(request.user_agent)  # 请求设备标志UA
print(request.remote_addr)  # 客户端远程地址
print(request.server)  # 服务端的端点，格式：(IP, 端口)
```

### 获取查询字符串参数

只适用于 GET 请求 中的 URL 查询参数

举例：https://www.baidu.com?key=flask --> 问好后面的键值对

```python
from flask import request

print(request.args.get("key"))  # 获取参数值，默认返回字符串
print(request.args.getlist("key"))  # 获取同名参数列表，如 ?a=1&a=2
```

### 获取请求体

```python
from flask import request

"""获取请求体,如果客户端上传的是xml文档，html格式，二进制流格式，base64格式，就要用data接收"""
print(request.data)
print(type(request.data))  # bytes
```

### 获取form表单数据

```python
from flask import request

"""接受表单上传数据"""
print(request.form)  # 可以字典取值
```

### 获取json数据

```python
from flask import request

"""接收json数据"""
print(request.json)  # 可以字典取值
print(request.is_json)  # 判断是否json数据
```

### 获取文件数据

```python
from flask import request

"""接收文件数据"""
file = request.files['file']  # 获取文件内容，字段是file的
filename = file.filename  # 获取文件名称
file.save(filename)  # 使用文件名保存文件到本地
```

## 响应

默认返回的是HTML字符串代码

### 返回json数据

```python
"""
导入jsonify方法可以处理返回json数据给客户端
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/index/", methods=['GET', 'POST'])
def index():
    json_data = {
        'name': '小明',
        "age": 19
    }

    # return json_data  # 虽然可以直接返回json数据，但使用 jsonify() 更安全、规范、兼容
    return jsonify(json_data)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
```

### 自定义状态码和响应头

- 常用写法：return 响应体, 状态码, 响应头
    - 一般返回数据会写一个状态码，默认200可以不写
    - 使用方法返回的响应通常不需要额外操作，例如：jsonify 默认就会设置 Content-Type: application/json，所以通常不用手动再加这个头，除非你要自定义其他 header。

```python
from flask import Flask, make_response, Response

app = Flask(__name__)


@app.route("/")
def index():
    """常用以下写法"""
    # return 'ok', 201, {"Company": "python-310"}

    """拆分原理"""
    # response = make_response('ok', 201, {"Company": "python-310"})
    # return response

    """再拆分原理"""
    # response = Response("ok")
    # response.headers["Company"] = "oldboy" # 自定义响应头
    # response.status_code = 201             # 自定义响应状态码
    # return response


if __name__ == '__main__':
    app.run()
```

# 重定向

```python
"""
导入redirect方法可以处理重定向操作
"""
from flask import Flask, redirect

app = Flask(__name__)


@app.route('/page')
def page():
    return "ok"


@app.route("/")
def index():
    """
    301: 永久重定向，页面已经没有了，站点没有了，永久转移了。
    302: 临时重定向，一般验证失败、访问需要权限的页面进行登录跳转时，都是属于临时跳转。
    """

    # 外部页面重定向
    # response = redirect("https://www.qq.com", 302)

    # 内部重定向(视图重定向)
    response = redirect("/page", 302)

    return response


if __name__ == '__main__':
    app.run()
```

# cookie会话控制(不常用了)

Cookie是由服务器端生成，发送给客户端浏览器，浏览器会将Cookie的key/value保存，下次请求同一网站时就随着请求头自动发送该Cookie给服务器（前提是浏览器设置为启用cookie）。Cookie的key/value可以由服务器端自己定义。

Cookie是存储在浏览器中的一段**纯文本信息**，建议不要存储敏感信息如密码，因为电脑上的浏览器可能被其它人使用

Cookie基于域名安全，不同域名的Cookie是不能互相访问的

**在`数据请求及响应/响应/自定义状态码和响应头`中提到make_response可以制作一个响应对象,需要使用里面的方法来操作cookie，下面代码都是在视图下面操作的**

## 设置cookie

不能直接存储中文，如果需要要进行转码等行为

```python
from flask import make_response
from datetime import datetime, timedelta

"""设置cookie，通过response传递到客户端进行保存"""
response = make_response('内容')
response.set_cookie('user', 'BinaryFool')  # 默认是session会话，关闭浏览器后当前cookie就会被删除
response.set_cookie('age', '19', max_age=30)  # max_age是指定最大有效时间，过期以后浏览器删除cookie，单位是秒
response.set_cookie('token', 'abc', expires=datetime.utcnow() + timedelta(hours=1))  # 到具体时间点过期，以为浏览器存储的是utc时间，这里也需要使用utc时间
# return response  # 返回到客户端即可
```

## 获取cookie

```python
from flask import request

# 获取前端请求的cookie
print(request.cookies)  # 可以使用字典取值, 没有值则返回None
```

## 删除cookie

删除cookie，重新设置cookie的时间，让浏览器自己根据有效期来删除

```python
from flask import make_response

response = make_response('删除cookie')

"""删除操作肯定是在浏览器完成的，所以我们重置下cookie名称的对应有效时间为0即可。"""
# 设置 max_age=0 会让浏览器立刻删除 Cookie，而此时即使 expires 被设置成未来的时间，也会被忽略，以 max_age 为准，设置清除只需要设置一个即可，不需要两个都写
response.set_cookie('username', '', max_age=0)
response.delete_cookie('username')  # 和上面的等效，只不过底层实现方法有略微区别，推荐使用这个

# return response  # 返回到客户端即可
```

# Session会话控制

对于敏感、重要的信息，建议要存储在服务器端，不能存储在浏览器中，如手机号、验证码等信息

在服务器端进行状态保持的方案就是`Session`

**Session依赖于Cookie**,session的ID一般默认通过cookie来保存到客户端。名字一般叫：sessionid

flask中的session需要加密,所以使用session之前必须配置SECRET_KEY选项,否则报错.

注意：一般框架都是把session数据保存到服务端，但是，flask里面的session是基于token方式存储在客户端的，并没有按照传统的方式保存在服务端的文件中。保存的session是加密的，无法看见，只能通过flask设定的密钥去解密

session操作都是基于路由视图下面的

## 配置session设置

```python
from flask import Flask, session
from datetime import timedelta

app = Flask(__name__)

# 设置密钥
app.config['SECRET_KEY'] = 'abcdfgsssss'  # 根据自己的需求填写，没用固定的，但是不能使用中文

# 设置session的过期时间
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)  # 控制持久化 session 的具体时长（默认 31 天）


@app.route('/')
def index():
    """
    session.permanent = True 持久化 不能写在全局，不然无效，session 是 请求上下文（request context） 绑定的，每次请求都会重新初始化。
    
    如果不设置session.permanent = True  # 启用持久化
    只在当前浏览器会话中有效
    关闭浏览器就会失效（浏览器自动清除）
    PERMANENT_SESSION_LIFETIME 设置 不会生效
    """
    session.permanent = True  # 启用持久化
    session['user'] = 'BinaryFool'
    return 'Logged in'
```

## 设置session

```python
from flask import session

"""设置session"""

# 单个键值对
session['username'] = 'BinaryFool'
session['age'] = 19

# 单个键多个键值对
session['info'] = {
  'username': 'BinaryFool',
  'age': '19'
}

# return 'ok' # 不需要返回session，会自动处理
```

## 获取session

请求参数等不需要传入session，会自动操作他们，直接使用即可

```python
from flask import session

"""获取session"""
print(session)  # 获取session对象
print(session.get('info'))  # 获取具体值
# return 'ok'  # 不需要返回session，会自动处理
```

## 删除session

```python
from flask import session

session.pop("username")  # 删除指定的key值
session.clear()  # 清除所有 session 项，不需要返回给前端，会自动处理
```

# 全局钩子

```python
# 待完成
```