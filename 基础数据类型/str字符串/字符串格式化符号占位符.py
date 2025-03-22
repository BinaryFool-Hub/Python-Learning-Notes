# 整形
# 因为是整型，所以使用%d
age = 18
print("age is %d" % age)

# 浮点型
# 因为是浮点型，所以使用%f，
# 因为浮点型输出了其他小数，我们可以使用.1来限制余数为一个小数
# 6.1中6表示的是总长度，如果不足在开头用空格补齐，如果小于则无视
height = 173.8
print("height is %.1f" % height)
print("height is %1.1f" % height)
print("height is %6.1f" % height)

# 字符型
# 直接补齐str_data里面的内容
str_data = 'joker'
print("my name is %s" % str_data)

# 多个格式化
info1 = 'a'
info2 = 'b'
print("info data is %s %s " % (info1, info2))
