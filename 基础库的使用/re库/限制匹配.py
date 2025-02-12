import re

text = """
134343434@qqco
45454545454444444@qqco
554@qqco
45645645645645@qqco
ggdf434@qqco
"""

# 使用{}限制数量

result = re.findall(pattern=r'\d{4,}', string=text)  # 匹配4个数字开始的到无限
print(result)

result = re.findall(pattern=r'\d{,7}', string=text)  # 匹配最大7个数字，最小不限
print(result)

result = re.findall(pattern=r'\d{1,7}', string=text)  # 匹配最大7个数字，最小1
print(result)

result = re.findall(pattern=r'\d{4}', string=text)  # 匹配4个数字
print(result)
