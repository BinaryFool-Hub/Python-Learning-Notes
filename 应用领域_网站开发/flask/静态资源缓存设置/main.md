# 介绍

如果静态资源太大了客户端每次请求在服务端都需要检查是否发生变化然后重新加载给前端

如果我们使用静态资源缓存机制就不会导致频繁发送请求了

# 方案一(推荐)

## 第一步

在模板文件中链接静态文件可以添加一个版本号，只需要在一次更新后更改版本号客户端即可得到新的文件(原理：在get请求参数的变化)

```
<link rel="stylesheet" href="{{ url_for('static', filename='style.css', v='1.0.1') }}">
```

## 第二步

直接在app的配置选项中添加一个设置即可

会自动设置响应头：Cache-Control: public, max-age=604800

```
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = int(timedelta(days=7).total_seconds())  # 7天缓存
```

# 方案二

同样使用方案一的步骤一版本号

然后在钩子装饰器里面添加一个请求头即可

```
@app.after_request
def set_cache_headers(response):
    if request.path.startswith('/static/'):  # 如果是静态文件
       if response.status_code == 200:  # 如果状态码是200
          response.headers['Cache-Control'] = 'public, max-age=604800'  # 返回响应头在客户端缓存多久
          
    return response  # 其他则正常返回	
```

# 查看是否成功

开发者面板size为：memory cache

如果还有大小响应则表示不成功
