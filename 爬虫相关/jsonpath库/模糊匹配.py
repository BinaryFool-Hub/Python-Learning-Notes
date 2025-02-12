import jsonpath

tsts_dict = {
    '你好': 23434,
    '你是': {
        '你好': '年后',
        '测试': {
            '你好787': '值'
        }
    }
}

# 模糊匹配
result = jsonpath.jsonpath(tsts_dict, "$..你好")  # 直接取出字典键为 你好 的值
print(result)
