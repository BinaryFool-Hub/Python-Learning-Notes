data = '[{"key": "value"}]'
# data = '{"key": "value"}'

print(type(data))  # str 类型

data = eval(data)  # 转换成正常的数据类型
print(type(data))  # list,dict
