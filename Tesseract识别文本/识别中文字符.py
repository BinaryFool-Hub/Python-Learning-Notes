import pytesseract
from PIL import Image

# 识别中文需要下载模型放到 文件目录\tessdata路径下
img = Image.open('test_chinese.png')
pytesseract.pytesseract.tesseract_cmd = r'E:\tesseract\tesseract.exe'

#  lang='chi_sim  指定中文语言模型做识别, 需要将语言模型放到模型文件路径中去
result = pytesseract.image_to_string(img, lang='chi_sim')

print(result)
