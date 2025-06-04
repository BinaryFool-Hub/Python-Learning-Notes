# 介绍

包也可以成为库，但是开发者自己定义的一般称为包，因为是结合项目使用的包，让其代码更规范和容易维护

包就是在里面存放了一些方法和依赖，和普通的文件夹目录一样，只不过多了一个`__init__.py`文件初始化包的

包里面还可以存放其他的依赖py文件

# __init__.py作用

当py文件导入包的时候这里面的文件会被自动执行

```python
# method/__init__.py
print('hello python')
```

```python
# 调用python的包
import method

"""即使没有输出语句，只是单纯的调用也会运行，因为有__init__.py文件让这个包初始化的代码"""
```

# 循环导入问题

这里的循环导入指的不是导入多次包,即使导入多次包也只会执行一次__init__.py

- Python解释器会陷入无限循环(下面代码循环导入)：
    - 先加载module_a.py，发现需要导入module_b.func_b
    - 开始加载module_b.py，发现需要导入module_a.func_a
    - 但module_a.py还没有完成加载，因为它在等module_b.py加载完成
    - 结果：ImportError: cannot import name 'func_a' from partially initialized module...
- 循环导入解决:
    - 按需导入即可,在需要调用执行该导入的方法函数里面导入即可
    - 如果你可以确保不会发生循环导入事件完全可以在头文件里面导入

```python
# method/__init__.py

print('hello python')
```

```python
# method/module_a

from .module_b import func_b  # 导入module_b的内容


def func_a():
    # from .module_b import func_b  # 导入module_b的内容

    print("Function A")
    func_b()  # 调用module_b的函数
```

```python
# method/module_b

from .module_a import func_a  # 导入module_a的内容


def func_b():
    # from .module_a import func_a  # 导入module_a的内容

    print("Function B")
    func_a()  # 调用module_a的函数
```

```python
# 调用包的py文件
from method.module_a import func_a
from method.module_b import func_b

# ImportError: cannot import name 'func_a' from partially initialized module 'method.module_a' (most likely due to a circular import) (D:\BinaryFool\python\Python-Learning-Notes\库和包\包的使用\method\module_a.py)
# 因为上面包里面嵌套循环导入了,所以会导致这个错误
```