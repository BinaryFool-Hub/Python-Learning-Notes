"""小写转大写"""
text = "hello"
uppercase_text = text.upper()
print(uppercase_text)  # 输出: HELLO

"""大写转小写"""
text = "HELLO"
lowercase_text = text.lower()
print(lowercase_text)  # 输出: hello

"""混合大小写互换"""
text = "Hello World"
swapped_text = text.swapcase()
print(swapped_text)  # 输出: hELLO wORLD

"""标题字体"""
# 单词首字母大写
text = "hello world"
text = text.title()
print(text)

"""整条句子第一个单词首字母大写"""
text = "hello world"
text = text.capitalize()
print(text)
