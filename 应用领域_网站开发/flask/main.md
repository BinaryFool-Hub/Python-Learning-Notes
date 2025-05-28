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

# request数据请求及响应

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

# redirect重定向

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

# 请求全局钩子

- flask 的“钩子（Hook）”是一种 在请求处理过程的不同阶段插入自定义逻辑 的机制，主要用于做一些全局性的处理，比如：
    - 请求前做权限检查或参数校验
    - 请求后统一格式化响应
    - 记录日志、统计耗时
    - 打开和关闭数据库连接等
- Flask 中常用的钩子有三种(本来有四种，但是结合开发习惯等因素删除了before_first_request)：
    - @app.before_request：在每一个请求之前自动调用（视图函数执行之前）
    - @app.after_request：在每一个请求之后自动调用（视图函数执行之后，响应返回之前）
    - @app.teardown_request：请求处理完后自动调用（无论是否发生异常）
- 可以把 Flask 的钩子（Hook）理解为一种“轻量级的中间件机制”，不过它和真正的“中间件”还是有一些区别的
- Flask 的钩子是实现中间件功能的方式之一，但不如传统中间件机制灵活和通用。

## before_request

每次客户端访问，视图执行之前，都会自动执行被 @app.before_request 所装饰的函数

常用于每次视图访问之前的公共逻辑代码的运行\[身份认证，权限判断，请求日志]

在每一个请求之前自动调用（视图函数执行之前）

### 方案一(推荐)

直接使用装饰器注册

```python
"""
每个请求前都会执行这个注册的钩子代码
"""

from flask import Flask, request

app = Flask(__name__)


@app.before_request  # 直接使用装饰器注册
def before_request_event():
    if request.path.startswith('/static/'):  # 如果是你的静态文件访问就不继续执行下面代码了
        return

    print("每个请求前都执行了改代码")


@app.route('/')
def index():
    print("index")
    return "index"


@app.route('/page')
def page():
    print("page")
    return "page"


if __name__ == '__main__':
    app.run()
```

### 方案二

使用app实例化对象注册

```python
"""
每个请求前都会执行这个注册的钩子代码
"""

from flask import Flask, request

app = Flask(__name__)


def before_request_event():
    if request.path.startswith('/static/'):  # 如果是你的静态文件访问就不继续执行下面代码了
        return

    print("每个请求前都执行了改代码")


"""注册前置钩子"""
app.before_request(before_request_event)  # 使用app实例化对象注册


@app.route('/')
def index():
    print("index")
    return "index"


@app.route('/page')
def page():
    print("page")
    return "page"


if __name__ == '__main__':
    app.run()
```

## after_request

在每一个请求之后自动调用（视图函数执行之后，响应返回之前），常用于视图访问之后的公告逻辑代码\[结果加工，格式转换，日志记录]

在上面的`before_request`写了两种方案，after_request钩子也可以，但是示例代码只展示一种推荐的

```python
"""
每个请求后响应前都会执行这个注册的钩子代码
"""

from flask import Flask, request

app = Flask(__name__)


# 注册钩子
@app.after_request
def after_request_event(response):  # 需要接收一个参数
    """如果before_request钩子return了就不会执行这段代码了，可以不需要写忽略静态文件"""
    # if request.path.startswith('/static/'):
    # return

    """获取到的数据都可以再一次处理，添加响应头等行为"""
    print(response.status_code)  # 获取响应状态码
    print(response.headers)  # 获取响应头
    print(response.get_data(as_text=True))  # 获取响应正文,as_text=True是以文本形式展示
    print("每个请求后响应前都执行了改代码")

    return response  # 需要返回响应给下一个模块处理


@app.route('/')
def index():
    print("index")
    return "index"


@app.route('/page')
def page():
    print("page")
    return "page"


if __name__ == '__main__':
    app.run()
```

## teardown_request

论请求是否成功、是否抛异常，都会在请求结束后执行，常被用于做一些“收尾工作”或“清理操作”

常用于 关闭数据库连接，清理线程或资源，记录异常日志，打印请求结束标记，清除全局变量（如 g 对象中的数据）等行为

在上面的`before_request`写了两种方案，after_request钩子也可以，但是示例代码只展示一种推荐的

```python
"""
每个请求处理完后无论成功失败都会执行这个注册的钩子代码
"""

from flask import Flask, request

app = Flask(__name__)


# 注册钩子
@app.teardown_request
def teardown_request_event(exception):  # 需要接收一个参数，如果成功是None，否则有错误信息
    print(f'错误日志记录：{exception}')

    # 如果是你的静态文件访问就不继续执行下面代码了
    if request.path.startswith('/static/'):  # 根据你的情况是否需要处理
        return

    print("每个请求后响应前都执行了改代码")


@app.route('/')
def index():
    print("index")
    return "index"


@app.route('/page')
def page():
    print("page")
    return "page"


if __name__ == '__main__':
    app.run()
```

# 上下文变量

上下文变量都需要在视图/路由上下文的空间里面使用，否则报错

## current_app

current_app 是 Flask 提供的一个上下文变量，用来在任意位置安全地访问当前正在运行的 Flask 应用对象（Flask 实例），即使你不在一个直接能访问 app 的作用域内。

注意：它必须在应用上下文中使用

current_app 是一个上下文变量，如果你在没有请求或没有推送上下文的情况下使用，会报错

应用程序上下文,用于存储flask应用实例对象中的变量，可以通过current_app.name打印当前app的名称，也可以在current_app中存储一些变量，例如：

- 应用的启动脚本是哪个文件，启动时指定了哪些参数
- 加载了哪些配置文件，导入了哪些配置
- 连接了哪个数据库
- 有哪些可以调用的工具类、常量
- 当前flask应用在哪个机器上，哪个IP上运行，内存多大

简单理解就是公共容器

```python
from flask import Flask, current_app

app = Flask(__name__)


@app.route('/')
def index():
    """
    应用上下文提供了一个容器，使你能够在整个应用程序中共享数据和对象。
    应用上下文提供给我们使用的变量，也是只能在视图或被试图调用的地方进行使用
    应用上下文所有的数据来源都是app
    """
    print(current_app)  # 应用上下文管理对象
    print(current_app.config)  # 获取当前项目的所有配置信息
    print(current_app.url_map)  # 获取当前项目的所有路由信息,<Rule '/static/<filename>路由是flask内部定义的静态文件路由

    return ' '


if __name__ == '__main__':
    app.run()
```

## g变量

g 作为 flask 程序全局的一个临时变量,充当着中间媒介的作用,我们可以通过它传递一些数据，
g 保存的是当前请求的全局变量，不同的请求会有不同的全局变量，通过不同的thread id区别

注意：客户端不同的请求，会有不同的全局变量g，或者说，每一个客户端都拥有属于自己的g变量（不会冲突）。

全局数据存储对象，用于保存服务端存储的全局变量数据\[可以理解为用户级别的全局变量存储对象]

```python
"""
可以被全局改变的上下文变量g
不支持g['info']的方式操作，只有点的方式
"""
from flask import Flask, g

app = Flask(__name__)


def test():
    g.user = 'BinaryFool'


@app.route('/')
def index():
    g.user = '小明'
    print(g.user)

    # 改变值
    test()
    print(g.user)

    return ' '


if __name__ == '__main__':
    app.run()
```

## 创建一个应用上下文环境调用

使用with创建上下文环境，就不需要在视图中单独使用了

如果调试作用输出的内容会在控制台日志顶端

```python
from flask import Flask, g, current_app

app = Flask(__name__)

with app.app_context():  # 使用with创建上下文环境，就不需要在视图中单独使用了
    print(current_app)
    print(g)
```

# url_for动态生成url

作用是根据视图函数的名字生成对应的 URL 地址，从而避免你在代码中硬编码 URL

假设你的视图函数或路由路径将来改变了，如果你在代码中写死了 URL（比如 /user/profile），那你就得手动修改所有用到这个路径的地方，非常麻烦。
而使用 url_for 可以自动根据函数名生成 URL，修改路由时只需要改一处即可，维护起来更方便。

```python
from flask import Flask, url_for

app = Flask(__name__)


@app.route('/page/<name>')
def page_fun(name):
    return f"{name}的page页面"


@app.route('/')
def index():
    name = '管理员'

    # 会自动处理返回路由路径，参数一传入视图即可，其他的参数是传入路由需要接收的数据
    url = url_for('page_fun', name=name)
    print(url)

    return url


if __name__ == '__main__':
    app.run()
```

# Jinjia2模板渲染

Jinja2 是一个基于 Python 的模板引擎，它被广泛用于 Web 开发中，Flask内置的模板语言Jinja2，它的设计思想来源于 Django 的模板引擎DTP(DjangoTemplates)，并扩展了其语法和一系列强大的功能，使得在生成动态内容时变得非常方便。

- Flask提供的 **render_template** 函数封装了该模板引擎Jinja2
- **render_template** 函数的第一个参数是模板的文件名，后面的参数都是键值对，表示模板中变量对应的数据值。

简而言之：操作html模板文件实现数据的传递，还可以操作python传递过来的变量/对象等

## 模板基本使用

需要手动在项目根目录创建`templates`模板文件夹用于存放模板的，
编辑器是pycharm的需要把文件夹右键标记为模板文件并且选择模板语言为Jinjia2，这样pycharm识别的时候才不会警告，而且还提高了编写代码的效率

使用参数的传递可以把数据变量传递到HTML模板，模板使用`{{}}`占位写入变量名称来接收变量值即可

python传递过来到HTML模板的数据可以像操作python一样操作他们（取值，等）

```html
{#
{{}} -> 是占位符
{#  #\} -> 是模板注释语法，\可以删除，用于转义的
#}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
</head>
<body>

<h1>{{ content }}</h1>

<h2>数据类型</h2>
<p>{{ list[-1] }}</p>
<p>{{ dict }}</p>
<p>取值数据类型: {{ dict['name'] }}</p>
<p>取值数据类型: {{ dict.name }}</p> {# 在HTML里面还可以这样使用来取值，python不行 #}
<p>{{ set }}</p>
<p>{{ bool }}</p>

</body>
</html>
```

```python
from flask import Flask, render_template

"""
template_folder:指定模板存放的路径，默认值为templates路径(可以不写)，可以选择自定义的，但是推荐使用默认
文件夹需要手动创建(项目根目录)，里面存放的是HTML模板文件

static_folder:指定静态文件的路径，默认值是static(可以不写)，可以选择自定义的，但是推荐使用默认
里面存放css，js，img，……，需要手动创建文件夹(项目根目录)
"""
app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def index():
    title = 'index'
    content = '这是我的第一个flask模板程序'
    context = {
        "title": title,
        "content": content,
        'list': [1, 2, 'a', 'v'],
        'dict': {'name': '小明', 'age': 19},
        'set': {1, 2, 34, 4},
        'bool': True
    }

    """
    这三种写法都可以把数据传递到HTML
    **locals(): 本地上下文，会把当前函数中的所有局部变量都传进模板，包括你没打算传的临时变量、调试变量、数据库连接对象等，看模板需要哪个挑哪个
    显示传递：明确只传了需要的变量，控制了变量的数量和命名，安全性高，代码可读性强。
    **context：限定上下文，只暴露指定的键值对给模板文件，这样代码又不冗长而且美观（推荐的做法👍）
    
    最终输出的 HTML 是字符串组成的，所以可以返回任何数据类型。如果需要处理可以进一步在HTML模板中操作他们，这时候他们还不是完全的字符串，
    还是python的数据类型，可以像操作python一样操作他们（取值，等）
    """
    # return render_template('index.html', title=title, content=content)
    # return render_template('index.html', **locals())
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run()
```

## 模板中全局的变量/函数

| 类型   | 名称                                    | 是否自动注入 |
|------|---------------------------------------|--------|
| 请求信息 | `request`, `session`, `g`             | ✅ 是    |
| 路由函数 | `url_for()`, `get_flashed_messages()` | ✅ 是    |
| 登录信息 | `current_user`（配合 Flask-Login）        | ✅ 是    |
| 其他全局 | `config`（需要手动注入）                      | ❌ 否    |

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>

{# 可以看到并没有传入/导入全局变量，但是可以直接操控，因为flask官方注入了 #}

{{ g.__dict__ }}
{{ session.__dict__ }}

</body>
</html>
```

```python
"""并没有导入和使用session,g，但是就是可以在HTML模板使用，因为官方已经为他们注入了"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
```

## 模板中的流程控制语句

在HTML模板执行流程控制语句(python语法)需要是`{% %}`来包裹语法,但是一句就一个这个语句标识符，但是需要有结束的代码块({% endif %}等)

### if判断

参数从python后端传入了，这里不再冗长的写python

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>

传递的值：{{ value }}

<div>
    {# if判断逻辑，逻辑不成立的就不会渲染标签，成立则会渲染标签 #}

    {% if value < 60 %}
    <p>不及格</p>
    {% elif value < 80 %}
    <p>及格</p>
    {% elif value < 90 %}
    <p>优秀</p>
    {% else %}
    <p>其他分数</p>
    {% endif %}
</div>

</body>
</html>
```

### for循环

参数是列表里面嵌套字典（这是例子，你可以传入任何列表里面嵌套的类型）：\[{'name': '小明'},{'name': '小白'}]

for 循环内部自动提供一个叫 loop 的特殊变量，它是一个循环助手对象，包含了当前循环的各种状态信息，相当于python传递过来的字典，直接用取即可

| 属性名              | 类型   | 说明                                |
|------------------|------|-----------------------------------|
| `loop.index`     | int  | 当前是第几次循环（从 1 开始）                  |
| `loop.index0`    | int  | 当前是第几次循环（从 0 开始）                  |
| `loop.revindex`  | int  | 距离结束还有几次（从 1 开始）                  |
| `loop.revindex0` | int  | 距离结束还有几次（从 0 开始）                  |
| `loop.first`     | bool | 是否是第一次循环                          |
| `loop.last`      | bool | 是否是最后一次循环                         |
| `loop.length`    | int  | 要循环的总次数                           |
| `loop.cycle()`   | 函数   | 在多个值之间交替输出（先使用第一个值下一次使用第二个值，依次交替） |
| `loop.depth`     | int  | 当前嵌套的深度（从 1 开始）                   |
| `loop.depth0`    | int  | 当前嵌套的深度（从 0 开始）                   |
| `loop.parent`    | obj  | 外层循环的 `loop`（嵌套循环时用）              |

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>

传递的值：{{ values }}

<div>
    {# for循环 #}

    {% for value in values %}
    <p {{ loop.cycle('data-attr="ss"', 'data-attr="aa') }}> {# 会交替给属性，loop.cycle()方法是交替执行的 #}
    <span>{{ loop.index }}</span> {# 获取索引，1开始 #}
    <span>{{ value['name'] }}</span> {# 这是取里面字典的形式，也可以使用.的形式 #}
    {{ loop }}
    </p>
    {% endfor %}

</div>

</body>
</html>
```

## 过滤器

需要使用整块进行过滤可以使用`filter`语句：`{% filter upper %} {% endfilter %}`,语句意思为全部大写 --> 列表过滤器提到过

过滤器迭用：会等前面的过滤器运行完成后再进行二次过滤`{{ 'HELLO' | lower | upper}}`,小写后又大写(但是这是徒劳，用来举例)

### 字符串过滤器

flask默认对传入的模板数据字符不会转义，举例：传入标签，展示的是字符串标签，不会进行解析。目的是为了防止注入攻击，比如写了一个scrapy标签进行攻击。
非必要不建议使用转义

| 过滤器          | 描述                                            | 代码                                                                                                                                     |
|--------------|-----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| **safe**     | 实体字符的转义(默认不转义，全都是字符串的形式，包括标签，使用safe就可以转移)     | {{ '\<p>hello\</p>' \| safe}}                                                                                                          |
| lower        | 把字母转成小写                                       | {{ 'HELLO' \| lower }}                                                                                                                 |
| upper        | 把字母转成大写                                       | {{ 'hello' \| upper }}`                                                                                                                |
| **reverse**  | 序列类型的数据反转，支持字符串、列表、元祖                         | {{ 'olleh' \| reverse }}                                                                                                               |
| format       | 格式化输出                                         | {{ '%s = %d' \| format('name',17) }}`<br>`{{ '%s = %d' % ('name', 17) }}                                                               |
| striptags    | 渲染之前把值中所有的HTML标签都删掉                           | {{ '\<script>alert("hello")\</script>' \| striptags }}`<br>如内容中存在大小于号的情况，则不要使用这个过滤器，容易误删内容。{{ "如果x<y，z>x，那么x和z之间是否相等？" \| striptags }} |
| **truncate** | 字符串截断<br>truncate(截取长度, 是否强制截取False, 省略符号...) | {{ 'hello every one' \| truncate(9)}}                                                                                                  |

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>

<p>
    {#  字母转小写  #}
    {{ 'HELLO' | lower }}
</p>
<p>
    {#  字母转大写  #}
    {{ 'hello' |  upper }}
</p>
<p>
    {#  序列数据反转  #}
    {{ 'hello' |  reverse }}
</p>

<p>
    {#  去除开头结尾的标签  #}
    {{ '<h1>alert("hello")</h1>' |  striptags }}
    {#  有大于小于号会导致误删  #}
    {{ "如果x<y，z>x，那么x和z之间是否相等？" | striptags }}
</p>

<p>
    {#  字符串截断，传参按字符算，按词为个体，舍弃多余的词汇  #}

    {{ 'hello every one'  | truncate(7) }} <br> {#  截取7位 hello e, 后三位转... 就是hell...  #}

    {{ 'hello every one'  | truncate(9, killwords=True) }} <br>
    {{ "foo bar baz qux www"| truncate(11) }} <br>
    {{ "foo bar baz qux www aaa xxx xxx"|truncate(19) }} <br>
</p>


</body>
</html>
```

### 列表过滤器

| 过滤器    | 描述               | 代码                             |
|--------|------------------|--------------------------------|
| first  | 取序列类型变量的第一个元素    | {{ \[1,2,3,4,5,6] \| first }}  |
| last   | 取序列类型变量的最后一个元素   | {{ \[1,2,3,4,5,6] \| last }}   |
| length | 获取序列类型变量的长度      | {{ \[1,2,3,4,5,6] \| length }} |
| count  | 获取序列类型变量的长度      | {{ \[1,2,3,4,5,6] \| count }}  |
| sum    | 列表求和，成员只能是数值类型！！ | {{ \[1,2,3,4,5,6] \| sum }}    |
| sort   | 列表排序             | {{ \[6,2,3,1,5,4] \| sort }}   |

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>

<p>{{ [1,2,3,4,5,6] | first }}</p>
<p>{{ [1,2,3,4,5,6] | last }}</p>
<p>{{ [1,2,3,4,5,6] | length }}</p>
<p>{{ [1,2,3,4,5,6] | count }}</p>
<p>{{ [1,2,3,4,5,6] | sum }}</p>
<p>{{ [1,2,3,4,5,6] | sort }}</p>
<p>{{ [1,2,3,4,5,6] | sort(reverse=True) }}</p>

{#  语句块过滤，对这里面的整块占位符的值过滤  #}
{% filter upper %}
    <p>abc</p>
    <p>{{ ["a","c"] }}</p>
    <p>{{ ["a","c"] }}</p>
    <p>{{ ["a","c"] }}</p>
    <p>{{ ["a","c"] }}</p>
{% endfilter %}


</body>
</html>
```

### 自定义过滤器

#### 编写过滤器代码

建议使用单独的文件来,比如`utils/filters.py`来管理

```python
"""
自定义过滤器，参数二可选，但是参数一是必须的，不然你怎么处理传入的数据
"""


def add_str(data, string):
    """
    用于添加字符串的过滤器
    :param data: 数据
    :param string: 添加的字符
    :return: 结果
    """
    return f"{data}{string}"


"""过滤器字典，过滤器名称可以自行定义"""
FILTERS = {
    'add_str_filter': add_str
}
```

#### 注册过滤器

```python
from flask import Flask
from utils.filters import FILTERS  # 路径自定义

app = Flask(__name__)

for key, obj in FILTERS.items():
    app.add_template_filter(obj, key)  # 注意：是反的传递数据
```

#### 通过装饰器的方法编写和注册过滤器(不推荐)

```python
from flask import Flask

app = Flask(__name__)


@app.template_filter('add_str_filter')  # 传入装饰器自定义名称，下面的就是装饰器执行的具体代码
def add_str(data, string):
    """
    用于添加字符串的过滤器
    :param data: 数据
    :param string: 添加的字符
    :return: 结果
    """
    return f"{data}{'11'}"
```

#### 使用自定义过滤器

普通的如何使用这个就如何使用，如果不需要传递参数可以不打括号，但是可以打括号

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>

{# 自定义过滤器的使用 #}
<p>{{ 'info' | add_str_filter('字符') }}</p>


</body>
</html>
```

## 模板继承

在模板中，可能会遇到以下情况：

- 多个模板具有完全相同的顶部和底部内容
- 多个模板中具有相同的模板代码内容，但是内容中部分值不一样，弹窗
- 多个模板中具有完全相同的 html 代码块内容，侧边栏

像遇到这种情况，可以使用 JinJa2 模板中的 **模板继承** 来进行实现

模板继承是为了重用模板中的公共内容。一般Web开发中，继承主要使用在网站的顶部菜单、底部、弹窗。这些内容可以定义在父模板中，子模板直接继承，而不需要重复书写。

- block相当于在父模板中挖个坑，当子模板继承父模板时，可以进行对应指定同名区块进行代码填充。
- 子模板使用 extends 标签声明继承自哪个父模板，一个项目中可以有多个父模板，但每个子模板只能继承一个父模板。
- 父模板中定义的区块在子模板中被重新定义，在子模板中调用父模板的内容可以使用super()调用父模板声明的区块内容。如果不使用super()则会替换父模板的内容

编程习惯(根据自己喜好)：

- 把公共的HTML代码建立一个目录：templates/common
- 如果是主要的根基还可以命名为：base.html

### block代码块语法区别

两种方式都可以，如果想要增强阅读感就是用第二个方法，一般情况使用简洁的写法

| 写法                                    | 是否可用 | 是否推荐 | 说明              |
|---------------------------------------|------|------|-----------------|
| `{% block name %}{% endblock %}`      | ✅    | ✅    | 简洁，常见写法         |
| `{% block name %}{% endblock name %}` | ✅    | ✅    | 可读性更强，适合结构复杂的模板 |

### 构建基础架构

不被使用的代码块还是会展示原有的代码及其数据

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        header, footer {
            width: 1200px;
            height: 200px;
            background-color: #00acc1;
            margin: 0 auto;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        main {
            width: 1200px;
            min-height: 200px;
            background-color: #1de9b6;
            margin: 0 auto;
        }
    </style>
</head>
<body>

<h1>BinaryFool小站</h1>

{% block header %}
    <header>
        <h1>这是顶部部分</h1>
    </header>
{% endblock %}

<main>
    {% block container %}
        {# 这是给你编写代码的区域，container是区块名字 #}
    {% endblock %}
</main>

{% block footer %}
    <footer>
        <h1>这是底部部分</h1>
    </footer>
{% endblock %}

</body>
</html>
```

### 继承基础架构

这就是一个完整的界面了，因为已经通过extends语法继承了，只需要在代码块编写你的代码即可，继承的代码块位置不作限制，都可以进行顺序渲染
如果你不想改变原架构的代码块代码，不使用即可。
如果你继承代码块原来的代码，使用super()即可，位置你可以任意，都是继承父模板中的代码块的代码

```
{# 使用extends语法后面跟templates下面自己创建的路径即可，需要使用引号引起来，为了不影响阅读，继承代码一般放在开头 #}
{% extends 'common/base.html' %}

{# 你在构建基础架构的代码块语法怎么写的就在这怎么写就行，里面编写你的代码即可，参数等行为都是一样的 #}
{% block container %}
    <p>这是主要代码块</p>
{% endblock %}

{# 继承并且重写代码块 #}
{% block header %}
    {{ super() }}  {# 使用这个函数来进行继承，位置不限 #}
    <p>新增代码块</p>
{% endblock %}
```

## 模板包含

include 语句用于包含一个模板，并在当前命名空间中返回那个文件的内容渲 染结果

模板包含和模板继承有点相似，但是模板包含是把HTML代码拿过来进行拼接，不要有html和head等HTML结构标签，只是把里面的HTML代码拿过来使用而已

### 被include的文件

只需要简单的写HTML代码即可，不需要结构标签，不建议引入css和js标签，因为只是把这段代码放入引入该文件代码的区块地方，仅此而已

```
<div>
    <p>这是局域HTML代码</p>
</div>
```

### 使用include引入的文件

一个模板文件可以存在多个include

```
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>

{# 把里面的HTML拿过来放这里使用 #}
{% include 'common/sidebar.html' %}

<p>继续编写代码</p>

</body>
</html>
```