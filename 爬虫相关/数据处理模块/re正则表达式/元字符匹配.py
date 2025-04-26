"""
常用的元字符匹配：
    []  匹配[]中列举的字符
    \d  匹配数字
    \D  匹配非数字
    \w  匹配单词字符，即a-z、A-Z、0-9、_、各个国家语言地区文字
    \W  匹配非单词字符
    \s  匹配空白字符（空格 换行 \r \n）
    \S  匹配非空白字符
量匹配：
    .   匹配任意1个字符（除了\n）
    *   匹配前一个字符零次或者多次 <前一个字符可以没有出现, 最小次数是0次>
    +   匹配前一个字符一次或者多次 <前一个字符最少要出现一次, 才可以被匹配到, 次数多一并匹配>
    ?   零次或1次
量匹配结合：
    .*  匹配零次或者多次任意字符串
    .+  匹配一次或者多次任意字符串
"""

import re

txt = """
这是一段字符，901233445455，
this a string
"""

# 匹配数字
result = re.findall(r'\d+', txt)
print(result)

# 匹配单词字符
result = re.findall(r'\w+', txt)
print(result)

# 匹配列举的数据，可以使用`-`来代替连续区间
# + 表必须出现一次或以上的数据才返回
# 添加列举匹配的字符不需要使用任何分隔符，直接添加即可，正则内部会自动分开
result = re.findall(r'[0-3]+', txt)  # 匹配0-3的数据
print(result)
result = re.findall(r'[a-z]+', txt)  # 匹配a-z的26个英文字母
print(result)
result = re.findall(r'[az9]+', txt)  # 只匹配a z 9这三个字符
print(result)
