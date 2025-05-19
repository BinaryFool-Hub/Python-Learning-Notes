"""
^ 匹配以什么开头,放于指定数据前
$ 匹配以什么结尾,放于指定数据结尾
"""

import re

texts = ["xiaoming@gmail.com", "32434@gmail.com"]

for txt in texts:
    result = re.findall("^[a-z].*com$", txt)  # 必须要满足字母开头有要满足com结尾
    print(result)
