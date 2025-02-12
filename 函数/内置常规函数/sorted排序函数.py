data = [1, 7, 9, 0, 5, 4, 3]

# 针对可迭代对象进行排序，默认升序reverse=False
data_1 = sorted(data)
print(data_1)

# 利用 key 进行排序
data_2 = sorted(data, key=lambda x: x * - 1)
print(data_2)

# 排序方向
data_3 = sorted(data, reverse=True)
print(data_3)
