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
- 支持链式调用方法，当使用all()等方法返回实际数据后才不支持了

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

## filter查询过滤器(条件限定)

过滤器需要结合all(),first()等方法结合使用，因为过滤器生成的是SQL语句

传入多参数就是多参数每个条件都需要满足的数据才会被返回，任何一个不满足都不行，否则需要使用逻辑运算方法

### filter_by和filter区别

| 特性	    | filter_by()	                          | filter()                                                            |
|--------|---------------------------------------|---------------------------------------------------------------------|
| 语法	    | 直接写字段名（name="小明"）                     | 	需写模型类.字段名（Student.age > 18）                                        |
| 条件类型	  | 仅支持 =	                                | 支持所有 SQL 条件（>, <, LIKE 等）                                           |
| 多表查询	  | 不支持	                                  | 支持 （需结合 join()）                                                     |
| 适用场景   | 	简单等值查询                               | 	复杂查询                                                               |
| 简单语法示例 | Student.query.filter_by(age=19).all() | Student.query.filter(Student.age >= 19, Student.name == '小明').all() |

### 模糊查询

包含，开头，结尾

```
result = Student.query.filter(Student.id >= 1, Student.name.contains("小")).all()  # id大于等于1的，包含`小`字的
# result = Student.query.filter(Student.name.startswith("小")).all()  # 以`小`字开头的
# result = Student.query.filter(Student.name.endswith("小")).all()  # 以`小`字结尾的
```

### and_/or_/!/not_/in_/is_/isnot逻辑查询

and_,or_,not_: 需要导入sqlalchemy里面的运算逻辑方法，因为flask_sqlalchemy本身就是优化了部分语法

结合filter过滤器来嵌套逻辑查询即可，都可以互相嵌套使用

#### and_

```
"""and_ 方法等价于在filter里面写多个参数一样的"""
# result = Student.query.filter(Student.age == 19, Student.name == '小明').all()
result = Student.query.filter(and_(Student.age == 19, Student.name == '小明')).all()  # and_只是一个标识方法，和传入多个参数一样的效果
```

#### or_

```
"""or_ 只需要在filter过滤器里面嵌套即可，满足任意一个条件即可。如果还需要结合and运算可以使用and_或者直接在后面or_方法后添加即可"""
# result = Student.query.filter(or_(Student.age == 19, Student.name == '小明'), Student.id == 1).all()  # 满足age==19 or name =='小明' 并且id==1
result = Student.query.filter(and_(or_(Student.age == 19, Student.name == '小明'), Student.id == 1)).all()  # 满足age==19 or name =='小明' 并且id==1
```

#### not_

not_ 相当于取反，直接在你需要取反的数据中加一个not_即可

需要导入not_: from sqlalchemy import or_

```
result = Student.query.filter(not_(Student.id != 1)).all()  # not_(id不等于1的全部数据) --> id等于1的全部数据
```

#### !

直接==变为!=即可

```
result = Student.query.filter(Student.id != 1).all()  # id不等于1的全部数据
```

#### in_

in_范围查询,在模型中key直接操作限制即可

```
result = Student.query.filter(Student.id.in_([1, 3])).all()  # 返回in_([])中枚举的数据
```

#### is_

is_判断值查询

```
# 这两句是等效的，只不过推荐使用is_，会python基础的人都会选择is_,因为就是这是orm，会直接转换
# result = Student.query.filter(Student.age == None).all()
result = Student.query.filter(Student.age.is_(None)).all()
```

#### isnot

相当于is_取反的操作

```
# 这两句是等效的，是不过推荐使用isnot
# result = Student.query.filter(Student.age != None).all()
result = Student.query.filter(Student.age.isnot(None)).all()
```

## all()查询所有满足条件的对象

all()返回查询到的所有对象，返回结果是列表包裹实例对象

结合filter()来实现条件查询

```
# result = Student.query.all()  # 不限制条件会返回所有数据
result = Student.query.filter(Student.id == 1).all()  # 限制条件查询返回所有数据
```

## first()查询第一个满足条件的对象

first()返回查询到的第一个对象【first的结果只有一个模型对象】

结合filter()来实现条件限制

```
# result = Student.query.first()  # 没有条件限制就返回数据表中第一个数据
result = Student.query.filter(Student.id >= 1).first()  # 限制返回查询到的第一个数据
```

## count()查询满足条件结果数量

如果不设置过滤条件，则默认统计全表记录的数量

```
# result = Student.query.count()  # 没有条件限制就返回所有数据的总数
result = Student.query.filter(Student.id > 1).count()  # 限制返回查询到的数据总数
```

## order_by排序

```
"""
直接在字段后面使用方法即可，如果入两个值则第一个优先排序，如果一样则排序第二个
desc是倒序，asc是正序(默认的，可以选择不写)

下面两个方法完全等价，只是通过.的方式更倾向与面向对象。方法的方式更倾向于sqlalchemy的语法风格，但是需要导入方法
"""
# from sqlalchemy import desc
# result = Student.query.order_by(desc(Student.id), desc(Student.age)).all()
result = Student.query.order_by(Student.id.asc(), Student.age.desc()).all()
```

## limit()/offset() 限制返回的记录数

limit(n)作用：只返回查询结果的前 n 条记录。

offset(n)作用：跳过前 n 条记录，返回后续的记录（通常与 limit() 结合使用，实现分页）。

不推荐使用python的\[1:2]切片来处理，因为使用.all()方法已经返回所有的数据了，会导致数据过于冗长难以处理

```
"""
limit()：用于限制返回条数
offset():用于忽略指定条数前面数据
"""
# result = Student.query.limit(2).all()  # 返回前两条数据
# result = Student.query.offset(3).all()  # 除了前3条数据都返回
result = Student.query.offset(3).limit(6).all()  # 返回第4条数据开始后取6条
print(result)
```

## exists判断是否存在，scalar获取结果

| 方法       | 返回值        | 适用场景             | 性能特点        |
|----------|------------|------------------|-------------|
| scalar() | 单字段值       | 获取聚合结果、第一条记录的字段值 | 需执行完整查询     |
| exists() | True/False | 仅判断是否存在记录（不取数据）  | 数据库优化，找到即停止 |

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
        sql = Student.query.filter(Student.id == 1, Student.name == '小红').exists()  # exists判断值是否存在，如果传入多个则两个都必须在同一行才行
        result = db.session.query(sql).scalar()  # scalar获取结果
        print(result)

    app.run()
```

## 聚合查询(类似MySQL的函数方法)/分组操作

需要使用scalar()方法来获取结果

```python
from sqlalchemy import func
```

| 函数名        | 说明   |      
|------------|------|
| func.count | 统计总数 |      
| func.avg   | 平均值  |      
| func.min   | 最小值  |      
| func.max   | 最大值  |      
| func.sum   | 求和   |     

```python
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import func

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
    sex = db.Column(db.Integer, comment='性别')


if __name__ == '__main__':
    with app.app_context():  # 为了方便测试写的，实际开发中可以结合路由
        """
        scalar()用于从查询结果中提取第一行第一列的值，并作为单个值返回
        """

        """func.sum求和"""
        data = db.session.query(func.sum(Student.age)).scalar()
        print("求和：", data)

        """func.count总数"""
        data = db.session.query(func.count(Student.name)).scalar()
        print("总数：", data)

        """func.avg平均值"""
        data = db.session.query(func.avg(Student.age)).scalar()
        print("平均值：", data)

        """func.max最大值"""
        data = db.session.query(func.max(Student.age)).scalar()
        print("最大值：", data)

        """func.min最小值"""
        data = db.session.query(func.min(Student.age)).scalar()
        print("最小值：", data)

        """分组操作
        使用性别分组，年龄来求平均，
        label是别名，方便遍历后取值，因为聚合返回的字段名不确定，所以使用别名来代替
        分组的字段可以是多个
        """
        data = db.session.query(Student.sex, func.avg(Student.age).label('avg_res')).group_by(Student.sex).all()
        # 遍历结果, all()已经获取到所有结果了，如果想要更好看和进一步处理遍历即可
        for item in data:
            print(item.sex, item.avg_res)

    app.run()
```

# 数据表数据修改

先查询后修改，使用查询返回的实例对象直接修改即可，然后提交

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
    sex = db.Column(db.Integer, comment='性别')


if __name__ == '__main__':
    with app.app_context():  # 为了方便测试写的，实际开发中可以结合路由
        """修改一条"""
        result = Student.query.filter(Student.name == '小明').first()  # 先获取返回一个
        if result:  # 查询到了才修改
            # 展示原数据
            print(result.name)
            # 修改数据
            result.name = '小白'
            # 改后需要提交，否则一直在内存
            db.session.commit()

        """修改多条"""
        result = Student.query.filter(Student.age < 30).all()  # 返回列表包裹对象
        if result:  # 查询到了才修改
            for item in result:
                item.age = 29
                item.name = '小明'

            # 修改完成后提交
            db.session.commit()

        """修改一条和多条方法"""
        # 会修改查询到的所有信息,返回值为查询且修改了多少条数据
        row = Student.query.filter(Student.age < 30).update({
            Student.age: Student.age + 1,
            Student.name: '小白'
        })
        print("修改了：", row)
        db.session.commit()

    app.run()
```

# 数据表数据删除

和修改一样的性质，先查询后修改

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
    sex = db.Column(db.Integer, comment='性别')


if __name__ == '__main__':
    with app.app_context():  # 为了方便测试写的，实际开发中可以结合路由
        """删除一条数据"""
        student_obj = Student.query.filter(Student.id == 1).first()  # 返回一个对象
        if student_obj:  # 查询到才删除
            # 删除数据，直接传入对象即可
            db.session.delete(student_obj)
            # 删除后提交
            db.session.commit()

        """删除多条数据"""
        student_objs = Student.query.filter(Student.id <= 3).all()  # 返回列表包裹对象
        if student_objs:  # 查询到才删除
            for obj in student_objs:
                db.session.delete(obj)  # 删除数据
            # 删除后提交
            db.session.commit()

        """一条和多条数据删除，返回值为删除了多少条数据"""
        row = Student.query.filter(Student.id <= 8).delete()
        # 提交删除
        db.session.commit()
        print(row)
    app.run()
```

# Pagination分页器

SQLAlchemy 提供了一个称为 `Pagination`（分页器）的工具，用于处理数据库查询的分页操作。使用分页器，你可以轻松地实现在大数据集中分页浏览数据的功能

简单理解就是把数据进行了分页的返回，相当于limit和offset

结合路由来实现数据的查询返回给前端

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
    sex = db.Column(db.Integer, comment='性别')


if __name__ == '__main__':
    with app.app_context():  # 为了方便测试写的，实际开发中可以结合路由
        """
        分页器对象 = 模型.query.filter(过滤条件).paginate(page=页码, per_page=单页数据量,max_per_page=最大单页数据量，默认100, error_out=超出报错，默认True)
        过滤条件可以不写，就是返回全部：模型.query.paginate()
        
        max_per_page（最大每页条数）:限制用户可请求的最大 per_page 值，防止恶意请求过大分页（如 per_page=10000 导致性能问题）。
        max_per_page一般来限制per_page的值，如果per_page大于max_per_page就使用max_per_page的值
        
        error_out=False表示出数据超出范围不报错，返回空列表，可以使用来处理对应的操作
        """

        # 页码和量一般都是接收前端传递的
        paginate = Student.query.filter(Student.id > 13).paginate(page=4, per_page=2, max_per_page=40, error_out=False)
        # print(paginate.__dict__)  # 展示对象结构
        print(paginate.total)  # 全部查询到的数据总数
        print(paginate.items)  # 当前页展示的数据列表
        # print(paginate.pages)  # 分页后的总页码，一般都需要返回给前端

        if not paginate.items:
            print("数据空了")

        # print(paginate.has_prev)  # 是否有上一页
        # print(paginate.prev_num)  # 上一页的页码
        # print(paginate.prev())  # 上一页的分页器对象
        # print(paginate.prev().items)  # 上一页展示的数据列表，和当前分页对象一样的使用即可

        # print(paginate.has_next)  # 是否有下一页
        # print(paginate.next_num)  # 下一页的页码
        # print(paginate.next())  # 下一页的分页器对象
        # print(paginate.next().items)  # 下一页展示的数据列表，和当前分页对象一样的使用即可

    app.run()
```

# 表数据关联(模型关系)

在 SQLAlchemy 中，关联查询是一种强大的数据库查询技术，用于在不同模型之间建立关联，以便在查询时能够方便地获取相关联的数据。在关联查询中，常见的一些关键字和参数用于配置关联关系，下面是一些常用的参数和它们的描述：

| 选项名       | 说明                                                                                                                                               |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| backref   | 在关系的另一模型中添加**反向引用**，用于设置外键名称,在1查多的                                                                                                               |
| lazy      | 指定如何加载关联模型数据的方式，用于1对1或1对多链表中。参数值:<br>select（立即加载，查询所有相关数据显示，相当于lazy=True，默认为select）<br>subquery（立即加载，但使用子查询）<br>dynamic（不立即加载，但提供加载记录的查询对象）      |
| uselist   | 指定1对1或1对多连表时，返回的数据结果是模型对象还是模型列表，如果为False，不使用列表，而使用模型对象。<br>1对1或多对1关系中，需要设置relationship中的uselist=Flase，1对多或多对多关系中，需要设置relationshio中的uselist=True。 |
| secondary | 指定多对多关系中关系表的名字。<br>多对多关系中，需建立关系表，设置 secondary=关系表                                                                                                |

## 模型之间的关联

模型之间的联系就是一种概念，通过少量的代码实现多表之间的联系，实现操作一个表同时操作其他表

简单点理解：relationship的属性backref是给子表调用主表的，而relationship的接收变量是给主表调用子表的

**relationship级联属性：**

- `'save-update'`: 当父对象被添加到会话（session）中或更新时，子对象也应该被添加到会话或更新。
- `'delete'`: 当父对象被删除时，相关的子对象也应该被删除。
- `'all'`: 包括所有的 `'save-update'` 和 `'delete'` 操作。
- `'merge'`: 当父对象被合并到会话中时，子对象也应该被合并。
- `'expunge'`: 当父对象被从会话中移除时，子对象也应该被从会话中移除。
- `'refresh-expire'`: 当父对象被刷新或过期时，子对象也应该被刷新或过期。
- `'refresh'`: 当父对象被刷新时，子对象也应该被刷新。
- `'save-update, merge'`: 同时包括保存更新和合并的级联。

### 一对一关系 (One-to-One)

- 一对一关系表示一个模型的一个实例只关联另一个模型的一个实例。
- 使用uselist=False表示一对一关系
- 双向通信的核心思想：
    - 主模型（如 User）
        - 可以通过自己的属性（如 .profile）主动获取子模型（Profile）的对象。
        - 相当于："我是用户，我要查我的资料！"
    - 子模型（如 Profile）
        - 通过 backref 自动获得的反向属性（如 .user）反向获取主模型（User）的对象。
        - 相当于："我是资料，我要知道我的主人是谁！"
- 谁是主/子模型？
    - 外键定义在谁那里，谁就是子模型
    - 定义 relationship 的一方是主模型
- backref 是通信的桥梁
    - 它自动在子模型中创建反向属性，无需手动在子模型里写 relationship。
- 通信是双向的，但不对称
    - 主模型用 直接关系
    - 子模型用 backref 生成的反向关系

流程代码：

```
# 定义模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profile = db.relationship('Profile', backref='user', uselist=False)  # 主模型主动发声

class Profile(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 子模型默默记录关联ID

# 实际使用时的双向对话
user = User.query.first()
profile = user.profile  # 主模型 → 子模型 ("我的资料呢？")

profile = Profile.query.first()
owner = profile.user    # 子模型 → 主模型 ("我的主人是谁？")
```

实践代码：

```python
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__, template_folder="templates")

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@127.0.0.1:3306/flaskdemo?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy()
db.init_app(app)


class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True, comment="学号")
    name = db.Column(db.String(15), comment="姓名")
    age = db.Column(db.Integer, comment='年龄')
    sex = db.Column(db.Integer, comment='性别')

    """
    association变量：关系属性，不会被视为字段在数据库中建立，只是绑定两个模型之间的通讯，给flask调用数据而已，在该模型中使用可以操作子模型
    Info：关联的模型名称
    uselist=False：表示一对一关系，默认True
    backref='obj': 创建反向引用，里面的值被视为子模型调用父模型数据的属性
    
    relationship：建立关系
    """
    association = db.relationship('Info', uselist=False, backref='father_obj')


class Info(db.Model):
    __tabname__ = 'info'
    id = db.Column(db.Integer, primary_key=True, comment='主键')
    address = db.Column(db.String(25), comment='地址')

    """设置外键字段，让两个表有关联
    ForeignKey里面参照的是表字段，参照字段必须有唯一属性(主键或唯一键)
    """
    foreign_key_sid = db.Column(db.Integer, db.ForeignKey('student.id'))


if __name__ == '__main__':
    with app.app_context():
        """
        记得创建好数据库表
        使用方法和基本的模型差不多(增删改查)，只不过可以同时操控有关系的其他模型
        """

        """父模型操作数据"""
        # 添加数据
        data_obj = Student(
            name='小明',
            age=19,
            association=Info(address='地址……')  # 使用该变量可以一并添加子表的数据
        )
        db.session.add(data_obj)
        db.session.commit()

        # 如果添加数据的时候子表没有添加，通过查询后直接再操作对象即可
        data_obj = Student(name='小白', age=19)  # 没有操作子表的数据
        db.session.add(data_obj)
        db.session.commit()  # 先添加了主表的数据
        # 把对象查询出来
        find_obj = Student.query.filter(Student.name == '小白', Student.age == 19).first()  # 取第一个数据出来，如果要操作多个使用update等方式更新数据即可
        find_obj.association = Info(address='小白的地址1')  # 就相当于修改数据了
        db.session.commit()  # 修改完成数据后记得提交

        """子模型操作数据"""
        son_mod_obj = Info.query.filter(Info.foreign_key_sid == 3).first()  # 只取一个来示例
        print(son_mod_obj.father_obj.__dict__)  # 这样就返回了父模型的对象数据了，可以直接操作对象里面的数据，记得提交数据

    app.run()
```

### 一对多关系 (One-to-Many)

一对多关系表示一个模型的实例可以关联多个另一个模型的实例。

一对多是一个主模型实例关联多个同类型的子模型实例

外键定义在"多"的一方（Book表）

relationship()定义在"一"的一方（Author表）

思维和一对一一样的，把uselist=True即可，但是默认就是True，可以不写。操作对象返回可以是多个了

```python
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__, template_folder="templates")

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@127.0.0.1:3306/flaskdemo?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy()
db.init_app(app)


class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True, comment="学号")
    name = db.Column(db.String(15), comment="姓名")
    age = db.Column(db.Integer, comment='年龄')
    sex = db.Column(db.Integer, comment='性别')

    # 关系键
    association = db.relationship('Info', uselist=True, backref='father_obj')


class Info(db.Model):
    __tabname__ = 'info'
    id = db.Column(db.Integer, primary_key=True, comment='主键')
    address = db.Column(db.String(25), comment='地址')

    # 外键
    foreign_key_sid = db.Column(db.Integer, db.ForeignKey('student.id'))


if __name__ == '__main__':
    with app.app_context():
        """添加数据
        把主表的uselist=True，这里就支持传入列表包裹对象了
        """
        obj = Student(name='小黑', association=[
            Info(address='地址1'),
            Info(address='地址2'),
            Info(address='地址3')
        ])
        db.session.add(obj)
        db.session.commit()

        """查询数据
        """
        # 主表查询子表
        obj = Student.query.filter(Student.name == '小黑').first()  # 只查询主表的一条数据返回一个对象
        print(obj.association)  # 返回名字是小黑的有多少个地址对象
        # 子表查询主表
        obj = Info.query.filter(Info.address == '地址1').first()  # 只用一个来示例
        print(obj.father_obj)  # 返回主表中的数据对象

    app.run()
```

### 多对多关系 (Many-to-Many)

多对多关系需要中间关联表来实现。

需要创建单独的关联表

使用secondary参数指定关联表

双向关系可以使用backref

多对多关系表示两个模型之间存在复杂的多对多关联。一个典型的场景是学生和课程的关系，一个学生可以选修多门课程，而一门课程也可以被多名学生选修。或者是社交平台的用户之间关系，一个用户可以关注N个用户，N个用户也可以随意关注其他用户

操作逻辑都是一样的，使用面向对象思维就可以很快的理解

```python
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__, template_folder="templates")

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@127.0.0.1:3306/flaskdemo?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy()
db.init_app(app)

"""中间表定义
和普通的不一样定义方式
两个外键都是主键表示这两个键为一个整体，上下文的数据不能同时重复(1,1不是重复，后续再出现1,1才重复)
"""
student_connect_info = db.Table(
    'student_connect_info',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True, comment='学生信息id外键'),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'), primary_key=True, comment='课程信息id外键')
)


class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True, comment="学号")
    name = db.Column(db.String(15), comment="姓名")

    # 在任意一个模型中创建关系即可(Student和Course都可以)，因为都可以互相通讯的，然后使用secondary来指定中间表的实例化名称
    communication = db.relationship('Course', secondary=student_connect_info, backref='communication')


class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True, comment='主键')
    course_name = db.Column(db.String(25), comment='课程')


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()

        """因为有中间表，可以很好的操作他们，只需要操作一个你需要的表即可操作另一个表"""

        """添加学生同时添加课程"""
        obj = Student(name='张三', communication=[
            Course(course_name='python'),
            Course(course_name='C'),
            Course(course_name='java')
        ])
        db.session.add(obj)
        db.session.commit()

        """添加课程同时添加学生"""
        # 因为双向绑定了属性，所以可以直接使用backref里面的communication
        obj = Course(course_name='vue', communication=[
            Student(name='李四'),
            Student(name='王五'),
            Student(name='赵六')
        ])
        db.session.add(obj)
        db.session.commit()

        """查询学生同时查询课程"""
        obj = Student.query.filter(Student.name == '张三').first().communication
        for item in obj:
            print(item.__dict__)

        """查询课程同时查询学生"""
        obj = Course.query.filter(Course.course_name == 'vue').first().communication
        for item in obj:
            print(item.__dict__)

        """删除课程的时候同时中间表的映射关系"""
        # 删除课程
        obj = Course.query.filter(Course.course_name == 'python').first()
        db.session.delete(obj)
        db.session.commit()
        # 删除学生
        obj = Student.query.filter(Student.name == '张三').first()
        db.session.delete(obj)
        db.session.commit()

        """追加学生学习的课程"""
        obj = Student.query.filter(Student.name == '王五').first()
        obj.communication.append(Course(course_name='flask'))  # 直接使用属性追加即可，因为是列表，使用面向对象思维就行，不要纠结为什么
        db.session.commit()

        """删除指定学生的指定课程"""
        obj = Student.query.filter(Student.name == '王五').first()
        for item in obj.communication:
            if item.course_name == 'vue':
                db.session.delete(item)
        db.session.commit()
    app.run()
```

## join表连接查询

```python
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__, template_folder="templates")

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@127.0.0.1:3306/flaskdemo?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy()
db.init_app(app)


class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True, comment="学号")
    name = db.Column(db.String(15), comment="姓名")

    communication = db.relationship('Course', uselist=False, backref='communication')


class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True, comment='主键')
    course_name = db.Column(db.String(25), comment='课程')

    foreign_key_sid = db.Column(db.Integer, db.ForeignKey('student.id'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        """
        使用 `join` 进行多表关联查询（默认 INNER JOIN）：
        1. 先通过 `Student.query.join(Course)` 将 Student 和 Course 表关联（基于外键关系）
        2. `filter()` 可以同时使用两个表的字段进行筛选
        3. 返回的是 `Student` 查询对象，但能访问关联表字段
        4. 必须调用 `.all()`/`.first()` 等才会真正执行查询
        """
        obj = Student.query.join(Course).filter(
            Course.course_name == 'vue',
            Student.name == '小黑'
        )
        print(obj)  # 输出的是未执行的查询对象（SQL 语句）
        result = obj.all()  # 执行查询，返回符合条件的 Student 对象列表
        print(result)
        for item in result:
            print(item.communication)  # 输出关联的之表对象

    app.run()
```

## with_entities指定返回的字段

不止单个表支持返回指定字段，多个表也可以，根据情况而定是否需要返回指定字段

```python
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__, template_folder="templates")

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@127.0.0.1:3306/flaskdemo?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy()
db.init_app(app)


class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True, comment="学号")
    name = db.Column(db.String(15), comment="姓名")
    age = db.Column(db.Integer, comment="年龄")


if __name__ == '__main__':
    with app.app_context():
        """with_entities指定返回指定字段，直接返回的值了，而不是对象"""
        result = Student.query.with_entities(Student.name, Student.age).filter(Student.name == '小黑').all()
        print(result)

    app.run()
```

## options加载策略

joinedload:通过 JOIN 一次性加载主模型（User）和关联模型（Profile）的数据，避免多次查询数据库。

```
SELECT user.*, profile.* 
FROM user 
LEFT OUTER JOIN profile ON user.id = profile.user_id
```

```python
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy.orm import joinedload

app = Flask(__name__, template_folder="templates")

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@127.0.0.1:3306/flaskdemo?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy()
db.init_app(app)


class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True, comment="学号")
    name = db.Column(db.String(15), comment="姓名")
    age = db.Column(db.Integer, comment="年龄")

    communication = db.relationship('Course', uselist=False, backref='communication')


class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(15))

    foreign_key_sid = db.Column(db.Integer, db.ForeignKey('student.id'))


if __name__ == '__main__':
    with app.app_context():
        # 数据会通过 JOIN 提前加载，而非延迟加载。一次性提出来
        result = Student.query.options(joinedload(Student.communication)).all()
        for item in result:
            print(item.communication.id)  # 可以看见没有额外的sql语句了

    app.run()
```

## 关系选项总结

1. `backref`：在关联的另一个模型中自动创建反向引用。例如，`backref='posts'`将在关联的模型中创建一个名为`posts`的属性。
2. `lazy`：指定关系的加载方式。常用的选项有`'select'`（默认值，延迟加载）、`'joined'`（立即加载，使用JOIN操作）和`'subquery'`（立即加载，使用子查询）。
3. `cascade`：指定关系操作的级联行为。例如，`'delete'`表示删除主模型时级联删除相关联的子模型。
4. `primaryjoin`：指定关系的主键连接条件。用于在关联模型之间定义自定义连接条件。
5. `secondary`：指定多对多关系中的关联表。
6. `secondaryjoin`：指定多对多关系的第二个连接条件。用于在多对多关系中定义自定义的第二个连接条件。
7. `uselist`：指定关系是否使用列表来存储结果。默认情况下，关系使用列表，可以通过设置为`False`来使用单个对象。

**多对多关系**：

在多对多关系中，中间表（即关联表）起着重要的作用。这个中间表通常包含两个外键，分别关联到两个相关的表

由于多对多关系涉及到中间表，传递整个对象的列表是为了让 ORM 框架能够正确地在中间表中创建关联。这样可以确保正确的外键关系被建立，以及中间表的数据能够正确地映射到相关的对象

**一对多关系**：

在一对多关系中，通常是外键存在于多的一方。因此，当您将一的一方的实例插入到多的一方时，只需要传递外键值即可，因为这个外键值能够直接关联到多的一方

# 数据迁移/字段更改(追加，减少)

使用到了另一个模块，flask-migrate，前往阅读即可
