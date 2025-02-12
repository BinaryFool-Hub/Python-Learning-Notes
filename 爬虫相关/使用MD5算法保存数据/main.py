import hashlib  # 内置模块
import json

# 摘要前是一个字典对象
d1 = {"name": '张三', 'age': 18}

# 创建一个 MD5 哈希对象，这个对象将用于计算输入文本的 MD5 摘要。
md5_obj = hashlib.md5()

# 将输入的文本先使用 UTF-8 编码转换为字节流（因为哈希算法处理的是字节数据）
# sort_keys 默认是False，因为字典不是有序的，所有加密摘要的可能数据不会相同，使用它来指定是否排序，这样才能让相同的数据加密摘要为相同的数据
byte_data = json.dumps(d1, sort_keys=True).encode('utf-8')

# 将这些字节数据提供给 MD5 哈希对象，以便它逐步计算哈希值。
md5_obj.update(byte_data)

# 通过 hexdigest 方法获取最终的 MD5 摘要，并以十六进制字符串的形式返回。
print(md5_obj.hexdigest())

# 一步到位
print(hashlib.md5(json.dumps(d1).encode('utf-8')).hexdigest())
