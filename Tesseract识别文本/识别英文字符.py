import pytesseract
from PIL import Image  # PIL 就是安装的 pillow 模块; 安装名字和导入名字不一样

# 指定引擎的路径位置
pytesseract.pytesseract.tesseract_cmd = r'E:\tesseract\tesseract.exe'

# 打开图像
img = Image.open('test_english.png')

# image_to_string(图像对象)  识别图像中的字符
result = pytesseract.image_to_string(img)
print(result)
