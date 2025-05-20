import binascii

result = b'\xe4\xbd\xa0\xe5\xa5\xbd \xe4\xb8\x96\xe7\x95\x8c !'

# b2a_hex --> 2进制转化为16进制
res = binascii.b2a_hex(result)
print(res)

# a2b_hex --> 把16进制转化为二进制
res1 = binascii.a2b_hex(res)
print(res1)
