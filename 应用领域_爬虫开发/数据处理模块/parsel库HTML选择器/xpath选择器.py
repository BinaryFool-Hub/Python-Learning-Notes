# 基本语法
import parsel

"""
get是获取第一个数据，getall是获取所有数据返回为列表
下面选择方式都可以嵌套使用，有返回值，记得赋值输出
"""

html = """
<body>
<h1 class="red" id="red" data_v="selector" href="https://www.baidu.com">内容</h1>
<h1>内容1gggg</h1>
<p>p内容</p>
<h1>内容211111</h1>
<p>p内容</p>
<h1>内容3</h1>
<ul>
<li><a href="#">内容dddd</a></li>
<li>内容dffdf</li>
<li>内容dfdfsfaf</li>
<li>内容vvvvv</li>
</ul>
</body>
"""

selector = parsel.Selector(text=html)  # 转换为对象

# 层级选择
# /
selector.xpath('/html/body/h1').getall()  # 一层一层选择，根元素是html

# 跨节点选择
# //
# 会找到所有的ul，确保是唯一或你需要的数据
selector.xpath('//ul//a').getall()

# 二次选择
# .// ./
result = selector.xpath('//ul')  # 先选择ul
result.xpath('./li').getall()  # 再选择li

# 父节点选择
# ..
result1 = selector.xpath('//a')  # 先选择a
result1.xpath('..').getall()  # 再选择a的父级单元素

# 属性选择
# [@href="https://www.baidu.com"]
selector.xpath('//h1[@href="https://www.baidu.com"]').getall()  # 选择指定h1的属性和值

# 属性值提取
# @href
selector.xpath('//h1/@href').getall()  # 提取属性值

# 文本获取
# text()
selector.xpath('//h1/text()').getall()  # 获取文本内容

# 位置选择
# []
selector.xpath('//h1[2]').getall()  # 选择第二个h1标签

# 多条件选择
# | 是 or 的意思
selector.xpath('//h1/@class|//a/text()').getall()  # 会返回多个条件匹配到的值，如果匹配不到则不返回
