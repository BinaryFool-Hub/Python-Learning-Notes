# https://github.com/sml2h3/ddddocr

import ddddocr

ocr = ddddocr.DdddOcr(beta=True, show_ad=False)
"""注解
先需要实例化对象
beta=True --> 切换为第二套ocr模型，默认不切换
show_ad=False --> 不显示广告，默认显示
"""

image = open("images/ocr识别验证码.png", "rb").read()

result = ocr.classification(image)
"""注解
classification(bytes) --> 是一个ocr识别函数，里面接受二进制图片数据，返回模型识别结果
"""

print(result)
