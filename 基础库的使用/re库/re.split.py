import re

string = 'Pythonasdkjasd 464654 adhuiaghsdk 564654 akjsdhkashdkja'

"""参数传递
pattern     正则规则
string      需要匹配的字符
maxsplit    最大分割次数
flags       匹配模式
"""
result = re.split('\d+', string)
print(result)

# 只切割一次
result = re.split('\d+', string, maxsplit=1)
print(result)
