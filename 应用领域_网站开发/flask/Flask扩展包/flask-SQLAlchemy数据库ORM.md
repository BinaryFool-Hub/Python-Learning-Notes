# 认识ORM

**ORM** 全拼`Object-Relation Mapping`，中文意为 **对象-关系映射**。主要实现模型对象到关系数据库数据的映射。

ORM提供了一种面向对象操作数据库的方式给开发者。不需要编写原生SQL语句也能操作数据库，实现了业务代码与底层数据的解耦。

特点：

- 只需要面向对象编程, 不需要面向数据库编写SQL
    - 对数据库的操作都转化成对类/对象的属性和方法的操作
    - 不用编写各种数据库的`原生sql语句`，当然也可以编写原生SQL语句
- 实现了数据模型代码与数据库数据的解耦, 屏蔽了不同数据库操作上的差异
    - 不再需要关注当前项目使用的是哪种数据库
    - 通过简单的配置就可以轻松更换数据库, 而不需要修改业务代码

# Flask-SQLAlchemy扩展介绍

flask默认不提供数据库操作，也并没有提供ORM，所以一般开发的时候我们会采用flask-SQLAlchemy模块来实现ORM操作。

SQLAlchemy是一个python语言编写的高性能的关系型数据库ORM框架，它提供了高层的 ORM 和底层的原生数据库的操作。

我们使用sqlalchemy 不需要调用sqlalchemy 本身这个模块，而是采用flask-sqlalchemy ，这是一个简化了 SQLAlchemy 操作的flask扩展模块。（主要是简化了sqlalchemy初始化代码和分页操作等）

```shell
pip install flask-sqlalchemy

# 如果sqlalchemy连接的是 mysql 数据库，则需要安装 mysqldb 驱动
pip install flask-mysqldb
```

# 数据库连接配置和初始化

数据库连接格式：数据库://用户名:密码@地址端口/数据库名称?编码(可选)

设置完成后需要去MySQL中创建数据库并指定charset

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 在app实例化Flask对象添加连接配置信息
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:123@127.0.0.1:3306/flaskdemo?charset=utf8mb4"

# 是否追踪数据库对象的修改并发送信号， 通常建议设置为 False，开发中可以设置True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

# 操作数据库时会显示原始SQL语句，生产环境中建议关闭，默认为Flask
app.config["SQLALCHEMY_ECHO"] = True

# 实例化SQLAlchemy
db = SQLAlchemy()

# 初始化db对象
db.init_app(app)
```

# 数据表定义/创建/删除(模型类操作)

创建表的时候要确保数据库已经创建了，不然会报错，创建数据库的时候最好指定编码为utf8mb4

注意!：`db.drop_all()`会删除所有的数据表，谨慎使用

- **常用的SQLAlchemy字段类型**

| 模型字段类型名          | python中数据类型       | 说明                                       |
|:-----------------|:------------------|:-----------------------------------------|
| **Integer**      | int               | 普通整数，一般是32位                              |
| **SmallInteger** | int               | 取值范围小的整数，一般是16位                          |
| BigInteger       | int               | 不限制精度的整数                                 |
| Float            | float             | 浮点数                                      |
| **Numeric**      | decimal.Decimal   | 普通数值，一般是32位                              |
| **String**       | str               | 变长字符串                                    |
| **Text**         | str               | 变长字符串，对较长或不限长度的字符串做了优化                   |
| Unicode          | unicode           | 变长Unicode字符串                             |
| UnicodeText      | unicode           | 变长Unicode字符串，对较长或不限长度的字符串做了优化            |
| **Boolean**      | bool              | 布尔值                                      |
| **DateTime**     | datetime.datetime | 日期和时间                                    |
| Date             | datetime.date     | 日期                                       |
| Time             | datetime.time     | 时间                                       |
| LargeBinary      | bytes             | 二进制文件内容                                  |
| **Enum**         | enum.Enum         | 枚举类型，相当于django的choices，但是功能没有choices那么强大 |

- **常用的SQLAlchemy列约束选项**

| 选项名             | 说明                              |
|:----------------|:--------------------------------|
| **primary_key** | 如果为True，代表当前数据表的主键              |
| **unique**      | 如果为True，为这列创建唯一索引，代表这列不允许出现重复的值 |
| **index**       | 如果为True，为这列创建普通索引，提高查询效率        |
| **nullable**    | 如果为True，允许有空值，如果为False，不允许有空值   |
| **default**     | 为这列定义默认值                        |

- **python代码和原生SQL对比**

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:123@127.0.0.1:3306/flaskdemo?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy()
db.init_app(app)


# 继承的是初始化数据库的对象Model，也就是SQLAlchemy的实例化变量里面的Model
class Student(db.Model):
    """数据表定义"""
    """
    MySQL原生语法创建:
    CREATE TABLE tb_student (
        id INTEGER NOT NULL COMMENT '主键' AUTO_INCREMENT, 
        name VARCHAR(15) COMMENT '姓名', 
        age INT COMMENT '学号'
    )
    """

    """
    ORM语法创建：
    __tablename__：数据表名称，不能改变量名称，只能改值
    name = db.Column(): 列的字段约束，变量即为字段。参数一为类型，其他的可选
    """
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True, comment="主键")  # primary_key是否为主键，comment备注
    name = db.Column(db.String(15), comment="姓名")
    age = db.Column(db.Integer, comment="学号")


if __name__ == '__main__':
    # 如果数据库中已经声明了有数据表，则不会继续生成
    # 创建模型需要在应用程序上下文之外工作
    with app.app_context():
        """数据表创建"""
        db.create_all()  # 只要继承了db.Model都会识别为模型，都会被创建，如果已经创建了不会继续生成

        """数据表删除"""
        # 执行流程是: 先找本项目中的所有模型，再去MySQL比对，找到则删除
        # db.drop_all()  # 只要继承了db.Model都会识别为模型，都会被删除，会删除所有数据表，谨慎使用

    app.run(debug=True)
```

# 数据表数据添加

实例化数据模型对象后使用SQLAlchemy的实例化变量来进行数据的添加，强烈推家使用关键字传参，除非有特定需求否则不建议使用init方法

```python
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__, template_folder="templates")

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@127.0.0.1:3306/flaskdemo?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy()
db.init_app(app)


class Student(db.Model):
    """确保这个表被创建了，否则报错"""

    __tablename__ = "tb_student"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(15), comment="姓名")
    age = db.Column(db.Integer, comment='年龄')

    def __init__(self, id, name, age, **kwargs):
        """只有在你需要自定义特殊逻辑时才考虑这个方法，否则不建议使用，这样你就可以位置传参了"""
        super().__init__(**kwargs)  # 保留对 **kwargs 的支持
        self.id = id
        self.name = name
        self.age = age


@app.route('/')
def index():
    # 模拟前端传入的数据
    data = [
        {'id': 1, 'name': '小明', 'age': 19},
        {'id': 2, 'name': '小红', 'age': 19},
        {'id': 3, 'name': '小白', 'age': 19},
    ]

    """
    使用实例化SQLAlchemy对象的变量db里面的会话机制，添加实例化类对象到会话中(对象里面填你的数据)
    必须传入实例化对象,不推荐 自己手动写 __init__ 方法来实现位置传参，除非你有非常明确的需求。
    """
    # 添加一条数据
    db.session.add(Student(
        id=data[0]['id'],
        name=data[0]['name'],
        age=data[0]['age']
    ))
    # 添加多条数据
    db.session.add_all([
        Student(name=data[1]['name'], id=data[1]['id'], age=data[1]['age']),
        Student(name=data[2]['name'], id=data[2]['id'], age=data[2]['age'])
    ])

    """把追加到会话里面的实例化类对象提交到后台进行数据提交"""
    db.session.commit()

    return 'ok'


if __name__ == '__main__':
    app.run()
```

# 数据表数据查询

**SQLAlchemy常用的查询过滤器**

| 过滤器            | 说明                                 |
|:---------------|:-----------------------------------|
| **filter()**   | 把过滤器添加到原查询上，返回一个新查询                |
| filter_by()    | 把等值过滤器添加到原查询上，返回一个新查询              |
| **limit()**    | 使用指定的值限定原查询返回的**结果数量**             |
| **offset()**   | 设置结果范围的**开始位置**，偏移原查询返回的结果，返回一个新查询 |
| **order_by()** | 根据指定条件对原查询结果进行**排序**，返回一个新查询       |
| **group_by()** | 根据指定条件对原查询结果进行**分组**，返回一个新查询       |

**SQLAlchemy常用的查询结果方法**

| 方法             | 说明                                                    |
|:---------------|:------------------------------------------------------|
| **all()**      | 以**列表形式**返回查询的所有结果                                    |
| **first()**    | 返回查询结果的第一个结果，**模型对象**，如果未查到，返回**None**                |
| first_or_404() | 返回查询的第一个结果，**模型对象**，如果未查到，通过 abort抛出404异常             |
| **get()**      | 可以设置查询主键参数，返回**指定主键**对应的**模型对象**，如不存在，返回None          |
| get_or_404()   | 可以设置查询主键参数，返回**指定主键**对应的**模型对象**，如不存在，通过 abort抛出404异常 |
| **count()**    | 返回查询结果的**数量**                                         |
| **paginate()** | 返回一个Paginate**分页器对象**，它包含指定范围内的结果                     |
| **having()**   | 返回分组结果中符合条件的数据，**必须跟在group by后面**，其他地方无法使用。           |

- 查询返回的数据结果是一个模型的对象实例/列表包裹实例，可以通过模型类内部封装方法来实现返回json或者自己封装一个函数来实现，在`query.get()主键查询`提到过

## query.get()主键查询

根据主键查询数据，如果主键不存在返回None

```python
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy.inspection import inspect  # model_to_dict方法的依赖

app = Flask(__name__, template_folder="templates")

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@127.0.0.1:3306/flaskdemo?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy()
db.init_app(app)


class Student(db.Model):
    __tablename__ = "tb_student"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(15), comment="姓名")
    age = db.Column(db.Integer, comment='年龄')

    def to_dict(self):
        """内部封装的方法，方便返回数据"""
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age
        }


def model_to_dict(obj):
    return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}


if __name__ == '__main__':
    with app.app_context():  # 为了方便测试写的，实际开发中可以结合路由
        """查询数据"""
        # result = Student.query.get(1)  # SQLAlchemy 2.0 中被弃用的老方法，不建议使用了
        result = db.session.get(Student, 1)  # 新写法(推荐)

        """取值数据，返回的是一个模型的对象实例"""
        print(result.name)  # 一个一个取值
        print(result.to_dict())  # 通过内部封装的方法来获取值
        print(model_to_dict(result))  # 通过其其他函数来辅助取值(通用方案)

    app.run()
```

## filter系列查询过滤器(条件限定)

过滤器需要结合all(),first()等方法结合使用，因为过滤器生成的是SQL语句

传入多参数就是多参数每个条件都需要满足的数据才会被返回，任何一个不满足都不行

### filter条件查询

支持各种运算符和查询方法或者模糊查询方法。

```python
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__, template_folder="templates")

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@127.0.0.1:3306/flaskdemo?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy()
db.init_app(app)


class Student(db.Model):
    __tablename__ = "tb_student"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(15), comment="姓名")
    age = db.Column(db.Integer, comment='年龄')

    def to_dict(self):
        """内部封装的方法，方便返回数据"""
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age
        }


if __name__ == '__main__':
    with app.app_context():  # 为了方便测试写的，实际开发中可以结合路由
        """查询数据"""
        result = Student.query.filter(Student.id >= 1, Student.name.contains("小")).all()  # id大于等于1的，包含`小`字的
        # result = Student.query.filter(Student.name.startswith("小")).all()  # 以`小`字开头的
        # result = Student.query.filter(Student.name.endswith("小")).all()  # 以`小`字结尾的
        print(result)

        """取值数据，返回列表包裹实例"""
        for item in result:
            print(item.to_dict())  # 通过内部封装的方法来获取值

    app.run()
```

### filter_by精确条件查询

filter_by 只支持字段的**值是否相等**的情况，对于大于、小于、大于等于、等等其他条件是不支持的。

字段添加不需要附带模型类

```python
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__, template_folder="templates")

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@127.0.0.1:3306/flaskdemo?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy()
db.init_app(app)


class Student(db.Model):
    __tablename__ = "tb_student"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(15), comment="姓名")
    age = db.Column(db.Integer, comment='年龄')

    def to_dict(self):
        """内部封装的方法，方便返回数据"""
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age
        }


if __name__ == '__main__':
    with app.app_context():  # 为了方便测试写的，实际开发中可以结合路由
        """查询数据"""
        # 单条件格式：filter_by(字段=值)
        # 多条件格式：filter_by(字段=值, 字段=值, 字段=值...)
        result = Student.query.filter_by(age=19).all()  # 字段添加不需要附带模型类
        print(result)

        """取值数据，返回列表包裹实例"""
        for item in result:
            print(item.to_dict())  # 通过内部封装的方法来获取值

    app.run()
```

## all()查询所有满足条件的对象

all()返回查询到的所有对象，返回结果是列表包裹实例对象

结合filter()来实现条件查询

```python
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__, template_folder="templates")

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@127.0.0.1:3306/flaskdemo?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy()
db.init_app(app)


class Student(db.Model):
    __tablename__ = "tb_student"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(15), comment="姓名")
    age = db.Column(db.Integer, comment='年龄')

    def to_dict(self):
        """内部封装的方法，方便返回数据"""
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age
        }


if __name__ == '__main__':
    with app.app_context():  # 为了方便测试写的，实际开发中可以结合路由
        """查询数据"""
        # result = Student.query.all()  # 不限制条件会返回所有数据
        result = Student.query.filter(Student.id == 1).all()  # 限制条件查询返回所有数据

        """取值数据，返回列表包裹实例"""
        for item in result:
            print(item.to_dict())  # 通过内部封装的方法来获取值

    app.run()
```

## first()查询第一个满足条件的对象

first()返回查询到的第一个对象【first的结果只有一个模型对象】

结合filter()来实现条件限制

```python
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__, template_folder="templates")

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@127.0.0.1:3306/flaskdemo?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy()
db.init_app(app)


class Student(db.Model):
    __tablename__ = "tb_student"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(15), comment="姓名")
    age = db.Column(db.Integer, comment='年龄')

    def to_dict(self):
        """内部封装的方法，方便返回数据"""
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age
        }


if __name__ == '__main__':
    with app.app_context():  # 为了方便测试写的，实际开发中可以结合路由
        """查询数据"""
        # result = Student.query.first()  # 没有条件限制就返回数据表中第一个数据
        result = Student.query.filter(Student.id >= 1).first()  # 限制返回查询到的第一个数据
        print(result)

        """取值数据，返回列表包裹实例"""
        print(result.to_dict())  # 通过内部封装的方法来获取值

    app.run()
```

## count()查询满足条件结果数量

如果不设置过滤条件，则默认统计全表记录的数量

```python
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__, template_folder="templates")

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@127.0.0.1:3306/flaskdemo?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy()
db.init_app(app)


class Student(db.Model):
    __tablename__ = "tb_student"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(15), comment="姓名")
    age = db.Column(db.Integer, comment='年龄')


if __name__ == '__main__':
    with app.app_context():  # 为了方便测试写的，实际开发中可以结合路由
        """查询数据"""
        # result = Student.query.count()  # 没有条件限制就返回所有数据的总数
        result = Student.query.filter(Student.id > 1).count()  # 限制返回查询到的数据总数
        print(result)

    app.run()
```

## and_/or_/!/not_/in_/is_逻辑查询

> 待完善笔记
