"""
官网：https://pypi.org/project/pyfiglet/
pip install pyfiglet
这个库提供了和多参数和艺术字体
"""

import pyfiglet

text = pyfiglet.figlet_format("Hello Python!", font="Small")
print(text)
