from io import BytesIO
import ddddocr
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont


# 返回字体文件的映射关系
class FontFileMappingRelationship(object):
    def __init__(self):
        self.img_size = 1024
        self.font_path = None
        self.font = None

    def convert(self, font_path):
        self.font_path = font_path
        self.font = ImageFont.truetype(font_path, int(self.img_size * 0.7))

        return self.identify_word(self.font_path)

    def font_to_img(self, _code):
        img = Image.new('1', (self.img_size, self.img_size), 255)
        draw = ImageDraw.Draw(img)
        txt = chr(_code)
        bbox = draw.textbbox((0, 0), txt, font=self.font)
        x = bbox[2] - bbox[0]
        y = bbox[3] - bbox[1]
        draw.text(((self.img_size - x) // 2, (self.img_size - y) // 7), txt, font=self.font, fill=0)
        return img

    def identify_word(self, font_path):
        font = TTFont(font_path)
        ocr = ddddocr.DdddOcr(beta=True, ocr=True, show_ad=False)
        font_mapping = {}

        for cmap_code, glyph_name in font.getBestCmap().items():
            bytes_io = BytesIO()
            pil = self.font_to_img(cmap_code)
            pil.save(bytes_io, format="PNG")
            word = ocr.classification(bytes_io.getvalue())

            if word:
                font_mapping[cmap_code] = word

        return font_mapping


data = '韱胒葫隐齖臚葫槽堭'  # 待解码数据
font_mapping_obj = FontFileMappingRelationship()
font_mapping = font_mapping_obj.convert('测试字体.woff')

text = ''
for i in data:
    ASCII = ord(i)  # 输出他的 ASCII 值
    # print(chr(ord(i)))
    text += font_mapping[ASCII]  # 提取映射关系

print(text)
