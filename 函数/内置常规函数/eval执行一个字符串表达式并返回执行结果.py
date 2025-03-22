data = "[1,1,2,23,3]"

# 字符串
print(type(data))

# 使用eval进行执行字符串，返回list。dict等都可以
data = eval(data)
print(type(data))
