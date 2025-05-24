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

# 重定向请求

```python
"""待完善笔记"""
```