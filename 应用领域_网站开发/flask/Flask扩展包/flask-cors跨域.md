# flask-cors跨域扩展

跨域是非flask全栈地址的前端发起的请求（浏览器中由前端发起的跨域请求）

```shell
pip install flask-cors
```

## 允许所有的域

```python
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许所有域名跨域
```

## 允许指定路由

```python
from flask import Flask
from flask_cors import cross_origin

app = Flask(__name__)


@app.route('/api/data')
@cross_origin(origins='https://example.com')  # 仅仅允许该路由的跨域而且还需要指定origins来自哪个域
def data():
    return {'msg': 'ok'}
```