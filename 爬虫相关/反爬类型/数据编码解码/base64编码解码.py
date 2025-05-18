import base64

# 编码
a = base64.b64encode(b"hello world")
print(a)  # b'aGVsbG8gd29ybGQ='

# 解码
b = base64.b64decode(a).decode()  # 解码之后 bytes 类型 可以decode解码成字符串
print(b)
