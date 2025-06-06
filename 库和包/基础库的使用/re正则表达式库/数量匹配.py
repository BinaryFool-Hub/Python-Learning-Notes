"""
数量匹配限定前一个数据类型出现的次数，如果不满足则匹配不到
{m} 匹配前一个字符类型出现m次
{m, n} 匹配前一个字符类型出现从m到n次,闭区间
"""

import re

text = """
这是一段文本内容： 12345用于个正则表达式提取内容使用
这是一段文本内容： 123456789012用于个正则表达式提取内容使用
"""

# 匹配前一个整形出现5-12次（闭区间），如果不能满足5-12次则匹配不到
result = re.findall(r'这是一段文本内容： (\d{3,10})用于个正则表达式提取内容使用', text)
print(result)

# 单独匹配一个数量的字符，如果前一个整形不出现5次则匹配不到
result = re.findall(r'这是一段文本内容： (\d{5})用于个正则表达式提取内容使用', text)
print(result)

# 设置最小匹配次数, 最大的次数不限制，必须满足整形出现5次或以上
result = re.findall(r'这是一段文本内容： (\d{5,})用于个正则表达式提取内容使用', text)
print(result)

# 最小的次数不限制, 最大匹配次数限制，必须满足整形出现最大12次或以下
result = re.findall(r'这是一段文本内容： (\d{,12})用于个正则表达式提取内容使用', text)
print(result)
