import re

# 在字符串中任意位置查找数据, 有且仅查找一次, 查找不到就返回None

string = 'ahsdgjasghPythonasdjajsk'
result = re.search('Python', string)

print(result)
if result:
    print(result.group())
