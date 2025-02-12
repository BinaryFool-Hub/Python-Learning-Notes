# 只能去除头尾的字符

data = '-=%python 3*()'

# 默认是去除空字符
print(data.strip())

# 去除一个字符
print(data.strip('-'))

# 去除多个字符
print(data.strip('-+%*()='))
