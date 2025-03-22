import re

text = """
回复(2)4楼2018-07-04 11:48

哥哥口袋有糖
初识物联1
346504108@qq.com

收起回复5楼2018-07-04 14:10

Super劫Zed: 540775360@qq.com
Super劫Zed: 086153131@qq.com
Super劫Zed: 745613513@qq.com
Super劫Zed: 056145678@qq.com

2018-8-8 16:00回复
我也说一句
"""

# 使用 - 代表开始到结束
# 每一个字符都是分开的，不需要使用什么隔开
# 一个[]代表一个占位符，可以结合其他正则符号来使用实现不同效果

result = re.findall('[A-Z0-9]', text)  # 匹配A-Z和0-9
print(result)

result = re.findall('[AZC90]', text)  # 匹配AZC90中任意字符
print(result)

result = re.findall('Super劫Zed: [0-9]*@qq.com', text)  # 匹配0-9开头的
print(result)
