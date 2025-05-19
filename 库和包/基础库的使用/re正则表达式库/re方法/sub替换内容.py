"""
re.sub() --> 替换方法

替换的结果需要重新接收，没有直接改变字符串内容

参数：
    pattern     正则规则
    repl        正则匹配到的规则需要替换成什么字符; 可以指定函数对象作为替换结果
    string      匹配的字符串
    count       替换的次数
    flags       匹配模式
"""

import re

string = 'Pythonasdkjasd Java adhuiaghsdk Java akjsdhkashdkja'

"""基本的替换"""
result = re.sub('Java', 'python', string)  # 把Java替换为python
print(result)
result = re.sub('Java', 'python', string, count=1)  # 把Java替换为python，只替换一次
print(result)

"""使用函数进行操作"""
# 匿名函数会被循环执行，每一次满足条件就会被执行一次
# 如果需要更复杂的操作可以使用自定义函数来完成，传入函数引用名即可

# 通过 Java 这个正则规则, 在 string 中匹配, 匹配到的结果会自动传入到匿名函数中处理
result = re.sub('Java', lambda x: x.group() + "111", string)
print(result)
