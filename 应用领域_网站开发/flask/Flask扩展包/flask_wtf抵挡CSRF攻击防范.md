# flask_wtf抵挡CSRF攻击防范

官方文档：http://www.pythondoc.com/flask-wtf/

CSRF：跨站请求攻击，简单地说，是攻击者通过一些技术手段欺骗用户的浏览器去访问一个自己曾经认证过的网站并运行一些操作（如发邮件，发消息，甚至财产操作如转账和购买商品）。由于浏览器曾经认证过，所以被访问的网站会认为是真正的用户操作而去运行。这利用了web中用户身份验证的一个漏洞：**简单的身份验证只能保证请求发自某个用户的浏览器，却不能保证请求本身是用户自愿发出的**。

如果有账户名为Alice的用户访问了恶意站点，而她之前刚访问过银行不久，登录信息尚未过期（session、cookie、token），那么她就会损失1000资金。

这种恶意的网址可以有很多种形式，藏身于网页中的许多地方。此外，攻击者也不需要控制放置恶意网址的网站。例如他可以将这种地址藏在论坛，博客等任何网站中。这意味着**如果服务端没有合适的防御措施的话，用户即使访问熟悉的可信网站也有受攻击的危险**。

透过例子能够看出，攻击者并不能通过CSRF攻击来直接获取用户的账户控制权，也不能直接窃取用户的任何信息。他们能做到的，是**欺骗用户浏览器，让其以用户的名义运行操作**。

flask_wtf本身提供了生成表单HTML页面的功能(基于wtforms提供)，常用于开发前后端不分离的表单页面，同时Flask-wtf 扩展模块还提供了一套完善的 csrf 防护体系，对于我们开发者来说，使用flask_wtf模块就可以非常简单解决CSRF攻击问题。

```shell
pip install flask_wtf
```

## 导入和把app注册进去

设置应用程序的 secret_key，用于加密生成的 csrf_token 的值，
导入 flask_wtf 中的 CSRFProtect类，进行初始化，并在初始化的时候关联 app

```python
from flask import Flask, render_template, request
from flask_wtf import CSRFProtect  # 导入模块

app = Flask(__name__, template_folder="templates")

# 设置依赖的设置key，自定义
app.config["SECRET_KEY"] = " my secret key"

# 实例化并且把app注册进去
csrf = CSRFProtect()
csrf.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/transfer", methods=["post"])
def transfer():
    print(request.form)  # 输出请求表单携带的数据
    return "转账成功！"


if __name__ == '__main__':
    app.run(debug=True)
```

## 在表单中使用 CSRF 令牌

form表单发送请求将携带csrf_token()发送，如果注册了csrf将会进行校验

```
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
<form action="/transfer" method="post">
    <input type="hidden" name="csrf_token" value="{{ csrf_token() }}"/> {# 使用该变量来创建token值 #}
    <label>
        账号：
        <input type="text" name="username">
    </label><br><br>
    <label>
        密码：
        <input type="text" name="password">
    </label><br><br>
    <input type="submit" value="转账">
</form>
</body>
</html>
```

