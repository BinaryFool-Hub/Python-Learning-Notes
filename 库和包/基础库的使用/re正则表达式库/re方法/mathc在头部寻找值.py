"""
re.match  匹配字符串中第一个内容, 如果字符串的最前面没有你要查找的内容就会返回None, 只会找头部
"""

import re

string = 'PythonahsdgjasghPythonasdjajsk'
string1 = ' PythonahsdgjasghPythonasdjajsk'  # 头部有空格

# 从头部开始寻找数据，找到了就返回对象，没找到就返回None
result = re.match('Python', string)
if result:
    print(result.group())  # 查看结果字符

# 因为头部有空格，寻找不到数据
result = re.match('Pyhton', string)
if result is None:
    print("从头部查找不到数据")
