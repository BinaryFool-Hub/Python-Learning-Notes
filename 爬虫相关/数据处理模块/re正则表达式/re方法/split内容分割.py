import re

string = 'Pythonasdkjasd 464654 adhuiaghsdk 564654 akjsdhkashdkja'

"""参数
pattern     正则规则
string      需要匹配的字符
maxsplit    最大分割次数
flags       匹配模式
"""

# 用数字进行分割，返回列表
res = re.split(pattern=r'\d+', string=string)
print(res)

# 用数字进行风格，返回列表，只分割一次
res = re.split(r'\d+', string, maxsplit=1)
print(res)
