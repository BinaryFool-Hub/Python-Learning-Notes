import re

text = """
你好，测试数据



"""

# 原本匹配不到换行符的，但是加上re.S模式匹配就可以

result = re.findall('你.......', text, flags=re.S)
print(result)
