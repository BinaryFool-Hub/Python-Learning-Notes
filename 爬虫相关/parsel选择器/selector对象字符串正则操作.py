import parsel

"""
我这里只是实例，完全可以结合不同的选择器来进行操作
"""

html = """
<body>
<h1 class="red" id="red" data_v="selector" href="https://www.baidu.com">内容</h1>
<h1>内容1gggg</h1>
<p>p内容</p>
<h1>内容211111</h1>
<p>p内容</p>
<h1>内容3</h1>
</body>
"""

selector = parsel.Selector(text=html)  # 转换为对象

# 进行正则匹配，只能使用部分正则语法
info = selector.css('body h1:nth-of-type(2)::text').re('内容(.*)')  # 获取文本后使用正则获取内容，返回一个列表
print(info)
