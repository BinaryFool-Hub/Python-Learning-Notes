# 介绍

- 在开发过程中，需要修改数据库模型，而且还要在修改之后更新数据库。最直接的方式就是删除旧表，但这样会丢失数据，所以往往更常见的方式就是使用alter来改变数据结构，原有数据中的新字段值设置默认值或null=True.
- 更好的解决办法是使用数据迁移，它可以追踪数据库表结构的变化，然后把变动的历史信息记录到数据库中。
- 在Flask中可以使用Flask-Migrate的第三方扩展来实现数据迁移。并且集成到Flask终端脚本中，所有操作通过`flask db`命令就能完成。
- 为了导出数据库迁移命令，Flask-Migrate提供了一个MigrateCommand类，可以注册到flask框架中。

首先要在虚拟环境中安装Flask-Migrate。

```bash
pip install flask-migrate
```

官网地址：https://flask-migrate.readthedocs.io/en/latest/

# Flask-Migrate 的主要用途

1. 跟踪数据库结构的变化
2. 自动生成迁移脚本
3. 升级（upgrade）或降级（downgrade）数据库结构
4. 配合 Flask-SQLAlchemy 使用效果最佳

# 基本使用

## 配置文件准备

在项目根目录创建一个`.flaskenv`文件用来存放flask的`使用自动环境变量加载`信息

.flaskenv 的使用方式叫做 Flask 的 python-dotenv 环境变量自动加载机制。

如果不使用该文件存放下面信息就需要每次运行flask命令都要指定设置，而且每个终端的方式还不同

- 安装依赖

```shell
pip install python-dotenv
```

- .flaskenv文件内容，值为你的全栈入口文件

```
FLASK_APP=app.py
```

## 1.确保你已经定义好模型（models）

```python
# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
```

## 2.设置 Flask 项目和数据库配置

```python
# app.py
from flask import Flask
from flask_migrate import Migrate
from models import db  # 引入你的模型实例化对象

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myapp.db'  # 或 MySQL/PostgreSQL，需要更换为你新的数据库名字
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

migrate = Migrate(app, db)  # 实例化migrate，里面传入app对象和db对象，生产环境放在这也无妨
```

## 3.初始化迁移环境

只需做一次，这一步会生成一个 migrations/ 文件夹，它用来存储 Alembic 的配置和迁移脚本。

```shell
flask db init
```

## 4.创建初始迁移脚本

这一步根据你定义的模型自动生成迁移脚本，记录数据库表结构（但不直接创建数据库）。

这时候会生成一个数据库表`alembic_version`用来存放当前数据库的表结构版本

```shell
# 字符串表示描述本次事件操作(可选)
flask db migrate -m "Initial migration"
```

## 5.执行迁移（创建或更新数据库结构）

这一步会自动创建数据库（如果你用的是 SQLite 且 .db 文件还不存在）并创建所有表。
如果你用的是 MySQL/PostgreSQL 等，数据库本身需要你提前手动创建好空数据库，但表结构是 upgrade 自动建的。

```shell
# 默认不写版本号就是最新的
flask db upgrade

# 0fdfa4d5681f 是一个版本号
flask db upgrade 0fdfa4d5681f
```

## 回滚迁移

```shell
# 默认不写版本号只是回滚了上一个版本
flask db downgrade

# 0fdfa4d5681f 是一个版本号
flask db downgrade 0fdfa4d5681f
```

## 查看版本号

可以点击进去py文件里面最上面注释有一个id，这就是版本号

```shell
# 查看所有版本号
flask db history
```

# 数据迁移介绍

开发中可以先初始化一个版本，flask就使用这个数据库，然后再继续构建字段和模型等，后续可以使用flask-migrate来进行版本管理

这里只是数据表结构进行了重构，如果你的模型有删减字段会导致数据丢失

