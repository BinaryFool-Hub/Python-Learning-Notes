def unicode_to_str(unicode_str):
    """unicode转字符串"""
    return unicode_str.encode().decode('unicode_escape')  # unicode_escape  是Unicode解码形式


def str_to_unicode(string):
    """字符串转Unicode"""
    new_str = ''
    for ch in string:  # 遍历每个字符
        # unicode编码中文存在的范围
        if '\u4e00' <= ch <= '\u9fff':  # 英文 / 符号不会转化 只针对中文
            # ord()  返回一个字符的码点
            # hex() 转16进制
            new_str += hex(ord(ch))
            new_str = new_str.replace('0x', '\\u')
        else:  # 如果不是中文拼接在结果的后面
            new_str += ch
    return new_str


if __name__ == '__main__':
    str1 = '你好python'
    res = str_to_unicode(str1)  # 将数据进行unicode编码
    print(res)

    print('解码之后的结果:', unicode_to_str(res))  # 解码
