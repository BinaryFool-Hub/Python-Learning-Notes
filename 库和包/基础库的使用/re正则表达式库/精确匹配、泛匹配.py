"""
()      表示精确匹配, 首先会根据正则规则匹配到数据, 然后提取 () 部分的内容，精确匹配的结果不会带约束字符
"""

import re

txt = """
这是一段字符，901233445455，this a string
"""

# 精确匹配，返回不含带约束字符，只返回括号里面匹配到的数据
result = re.findall('这是(.*?)string', txt, re.S)
print(result)

# 泛匹配，返回含带两边约束字符，并且括号里面匹配到的值也会一并返回
result = re.findall('这是.*?string', txt, re.S)
print(result)
