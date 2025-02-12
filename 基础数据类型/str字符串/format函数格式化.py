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

