data1 = 'Some data1'
data2 = 111
data3 = [111, 22]

"""位置映射"""
# 可以是任意数据类型，但是返回的结果整体都是字符型
result = "{} {} {}".format(data1, data2, data3)
print(result)
print(type(result))

"""索引映射"""
# 把format里面的内容自己排序好第几个需要在哪个占位符
result = "{2} {1} {0}".format(data1, data2, data3)
print(result)
print(type(result))

"""关键字映射"""
result = "{data1} {data3} {data2}".format(data1=data1, data2=data2, data3=data3)
print(result)
print(type(result))

"""格式化说明符"""
s = "字符串"
# 基本顺序规则：填充符 对其方向 总长度 千分位填充符
# 不能改变顺序，0表示格式化的第几个参数，默认顺序进行配对，可以不写

# : 格式化说明符的开始符号
# * 填充字符
# < 字符串居左显示
# ^ 字符串居中显示
# > 字符串居右显示
# 30 总长度为30
print("{0:*^30}".format(s))
print("{:b}".format(10))  # 二进制输出
print("{:o}".format(10))  # 八进制输出
print("{:x}".format(10))  # 十六进制输出 x 是小写 X 是大写
