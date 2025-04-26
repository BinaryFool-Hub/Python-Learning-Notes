"""
在字符串中任意位置查找数据, 有且仅查找一次, 查找不到就返回None
"""

import re

string = '  PythonahsdgjasghP ythonasdjajsk'

# 找到就返回对象
res = re.search('Python', string)
print(res)
print(res.group())

# 找不到就返回None
res = re.search('aython', string)
print(res)
