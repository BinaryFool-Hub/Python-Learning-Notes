"""
编码  encode()
默认的编码就是utf-8, 可以省略
主要有两种编码 utf-8 和 gbk,目前最常用的是utf-8
不同编码结果不同
用什么形式编码, 就要用什么形式解码
"""

str1 = '你好 世界 !'

result = str1.encode()
print('编码的结果:', result)
print('编码结果类型', type(result))

result1 = str1.encode('gbk')
print('编码的结果:', result1)
print('编码结果类型', type(result1))

print('------------------------')
result3 = result.decode()
print("解码：", result3)

result4 = result1.decode('gbk')
print("解码：", result4)
