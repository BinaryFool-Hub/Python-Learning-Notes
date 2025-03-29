""" any """
# 里面没有任何数据就为False
info = []
print(any(info))

# 只要里面有数据就为True
info1 = [1, 2, 3, 0, False]
print(any(info1))

""" all """
# 只要里面的数据都为 True 时才会返回 True
data = [0, 2, 3, 4, None, False]  # 0，None，False 等都视为 False
print(all(data))

# 里面的数据都为 True 才会返回 True
data = [1, 2, 3, 4, 45, 1]
print(all(data))
