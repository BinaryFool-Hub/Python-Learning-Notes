import re

string = 'Pythonasdkjasd Java adhuiaghsdk Java akjsdhkashdkja'

"""参数传递
re.sub() --> 替换方法

    pattern     正则规则    
    repl        正则匹配到的规则需要替换成什么字符; 可以指定函数对象作为替换结果
    string      匹配的字符串
    count       替换的次数
    flags       匹配模式
"""
result = re.sub('Java', 'python', string)
print(result)

# 这是替换一次
result = re.sub('Java', 'python', string, count=1)
print(result)

"""
函数传递
"""


def func(x):
    print('传入的数据:', x)
    return x.group() + '111'  # 函数的返回值就是 sub 最终替换结果


# 通过 Java 这个正则规则, 在 string 中匹配, 匹配到的结果会自动传入到 func
result = re.sub('Java', func, string)
print(result)
