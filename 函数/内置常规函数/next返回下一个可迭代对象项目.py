# 结合iter() 函数一起使用

data = [1, 8, 9, 0]
data = iter(data)

# 运行一次就取下一个值
print(next(data))
print(next(data))
print(next(data))
print(next(data))
# 超出取值会报错StopIteration
# print(next(data))
