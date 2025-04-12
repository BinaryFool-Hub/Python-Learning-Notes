import re

text = """
数据：info.sdfsfasfsd
"""

# 加上括号就是返回占位符匹配的结果，不加就是返回整体
result = re.findall(r'数据：(.*?)\.sdf', text)

print(result)
