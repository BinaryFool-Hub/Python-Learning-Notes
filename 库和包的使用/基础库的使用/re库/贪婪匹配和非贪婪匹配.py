import re

text = """
回复(2)4楼2018-07-04 11:48

哥哥口袋有糖
初识物联1
346504108@qq.com

收起回复5楼2018-07-04 14:10

Super劫Zed: 540775360@qq.com
Super劫Zed: 775203618@qq.com
Super劫Zed: 456123987@qq.com

2018-8-8 16:00回复
我也说一句
"""

"""
贪婪模式: 是正则表达式的默认匹配模式, 在符合规则的前提下, 会尽可能多的匹配数据结果返回

?   要么符合正则规则, 返回一次结果
    要么不符合规则, 没有结果返回
    最多匹配只能匹配一次
.*?
.+?
"""

# 贪婪匹配
result = re.findall('Super劫Zed: .*@qq.com', text, re.S)
print(result)

# 非贪婪匹配
result = re.findall('Super劫Zed: .*?@qq.com', text, re.S)
print(result)
