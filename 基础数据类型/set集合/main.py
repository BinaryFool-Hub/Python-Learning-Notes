"""
！！！集合是无序的
如果有重复会被自动处理删除只会保留一个
虽然无序，但你可以用 for 循环遍历
"""

set1 = {1, 6, 'sss', 1}
set2 = {6, 7, 'dddd', 'sss'}

# 当声明一个空集合需要使用关键字set()
set3 = set()
print(type(set3))

# 重复的会被删除
print(set1)

# 差级
print(set1 - set2)

# 并集
print(set1 | set2)

# 交集
print(set1 & set2)

# 集合中不同时存在的元素
print(set1 ^ set2)
