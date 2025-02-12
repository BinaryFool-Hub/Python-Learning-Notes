import re

str1 = "540775360@qq.com"
str2 = "python = 9999， c = 7890， c++ = 12345"
str3 = "python = 997"

# re.compile 将正则表达式编译成一个对象
# 手动编译的好处:
# 1. 如果编译好的正则需要多次匹配不同的字符串, 可以直接引用
# 2. 如果匹配的次数很多, 那么使用已编译好的对象去匹配, 效率更加高

pattern = re.compile('\d+')
print(pattern)

print(re.findall(pattern, str1))
print(re.findall(pattern, str2))
print(re.findall(pattern, str3))

"""分组提取"""
pattern = re.compile(r'(\d{4})(\d{4})(\d)')

print(re.sub(pattern, '\\1------\\3-----\\2', str1))
