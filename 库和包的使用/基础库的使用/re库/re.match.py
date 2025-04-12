import re

# re.match  匹配字符串中第一个内容, 如果字符串的最前面没有你要查找的内容就会返回None, 只会找头部
# string = 'ahsdgjasghPythonasdjajsk'
string = 'PythonahsdgjasghPythonasdjajsk'
result = re.match('Python', string)

print(result)
if result:
    print(result.group())  # 提取数据
