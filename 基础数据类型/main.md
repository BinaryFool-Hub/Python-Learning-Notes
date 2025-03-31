# dict, list 传入函数或类不需要重新接收

这两个数据类型传入函数或类并且进行操作或者更改值不需要重新接收，会在内存中自动更改

**下面只举例了dict，list也类似**

- 函数

```python
data = {"a": 2, "b": 3}


def fun(data_info):
    data_info["a"] = 9999


print(data)
fun(data_info=data)
print(data)
```

- 类

```python
data = {"a": 2, "b": 3}


class Item:
    def __init__(self, data_info):
        self.data_info = data_info

    def fun(self):
        self.data_info["a"] = 999


obj = Item(data_info=data)

print(data)
obj.fun()
print(data)

```