"""
re.compile 将正则表达式编译成一个对象
如果没有手动编译, 底层匹配数据的时候也会编译
如果多处使用同一个正则表达式就没必要再次进行编译和重写，直接调用对象即可，效率也会更高
"""

import re

str1 = "123453534@qq.com"
str2 = "python9999c7890c++12345"
str3 = "python997"

pattern = re.compile(r'\d+')
pattern1 = re.compile(r'\D+')

print(pattern)

# 匹配数字
print(re.findall(pattern, str1))
print(re.findall(pattern, str2))
print(re.findall(pattern, str3))

print("--------------------")

# 匹配非数字
print(re.findall(pattern1, str1))
print(re.findall(pattern1, str2))
print(re.findall(pattern1, str3))
