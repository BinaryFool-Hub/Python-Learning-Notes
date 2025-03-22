# 基本语法

"""
get是获取第一个数据，getall是获取所有数据返回为列表
下面的选择方式都可以嵌套使用，都有返回值，记得输出
"""

import parsel

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

# 标签选择
selector.css('body h1').getall()  # 选中body 下面所有 h1标签
selector.css('body>h1').getall()  # 选中body 下的子级 h1标签

# css样式选择
selector.css('body>h1.red').getall()  # 选中body下面子级h1 class="red" 的标签
selector.css('body>.red').getall()  # 选中body下面子级 class="red" 的标签

# id选择
selector.css('body>h1#red').getall()  # 选中body下面子级 h1 id="red" 的标签
selector.css('body>#red').getall()  # 选中body下面子级 id="red" 的标签

# 属性选择
selector.css('body>h1[data_v="selector"]').getall()  # 选中body下面子级h1属性是 data_v="selector" 的标签

# 获取文本
# ::text
selector.css('body>h1::text').getall()  # 选中body 下的子级 h1标签 并且获取文本

# 获取属性值
# ::atttr(href)
selector.css('body>h1::attr(href)').getall()  # 选中body 下的子级 h1标签 并且获取属性值

# 伪类选择
selector.css('body>:nth-child(3)').getall()  # 选择第三个标签
selector.css('body>:nth-last-child(3)').getall()  # 选择倒数第三个标签
selector.css('body>h1:nth-of-type(3)').getall()  # 选择第三个h1标签
selector.css('body>h1:nth-last-of-type(3)').getall()  # 选择倒数第三个h1标签

# 属性值包含选择
# 选取所有href属性中包含www.baidu的h1元素
selector.css('h1[href*="www.baidu"]').getall()

# 属性前缀选择
# 选取所有href属性值中以http开头的h1元素
selector.css("h1[href^='http']").getall()

# 属性直接选择
# 直接选中h1含有href属性的元素
selector.css("h1[href]").getall()
