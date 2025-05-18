"""
md5是不可逆的，只有加密没有解密
"""

import hashlib

# md5 摘要的内容是一样的,值就会是一样的
password = "你好"

# 1. 创建一个 md5 的对象
md5 = hashlib.md5()

#  更新到对象里面去
md5.update(password.encode())

# 获取
print(md5.hexdigest())
