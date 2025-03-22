"""
这是封装的类，直接传入字体文件路径即可，会返回映射好的字体关系
使用方法：在下面有示例调用
"""

from io import BytesIO  # 二进制数据对对象
import ddddocr
from PIL import Image, ImageDraw, ImageFont  # 图片对象<二进制>, 画图对象, 字体图片对象
from fontTools.ttLib import TTFont


class FontFileMappingRelationship(object):
    def __init__(self):
        self.img_size = 1024
        self.font_path = None
        self.font = None

    def convert(self, font_path):
        """
        初始化调用
        :param font_path: 字体文件地址
        :return: {'字': ASCII, 字体名称}
        """
        self.font_path = font_path
        self.font = ImageFont.truetype(font_path, int(self.img_size * 0.7))  # 字体绘图对象

        return self.identify_word(self.font_path)

    def font_to_img(self, _code):
        """
        ASCII值转换为图片
        :param _code: ASCII值
        :return: 二进制图片
        """
        img = Image.new('1', (self.img_size, self.img_size), 255)
        draw = ImageDraw.Draw(img)  # 创建画图对象
        txt = chr(_code)  # 转化码点值
        bbox = draw.textbbox((0, 0), txt, font=self.font)  # 构建一个字体图像画布,字画到画布上去
        x = bbox[2] - bbox[0]
        y = bbox[3] - bbox[1]
        draw.text(((self.img_size - x) // 2, (self.img_size - y) // 7), txt, font=self.font, fill=0)
        return img

    def identify_word(self, font_path):
        """
        字体映射规则
        :param font_path: 字体文件路径
        :return: {'字': ASCII, 字体名称}
        """
        font = TTFont(font_path)
        ocr = ddddocr.DdddOcr(beta=True, ocr=True, show_ad=False)
        font_mapping = {}

        for cmap_code, glyph_name in font.getBestCmap().items():
            bytes_io = BytesIO()  # 字节缓冲区
            pil = self.font_to_img(cmap_code)
            pil.save(bytes_io, format="PNG")
            word = ocr.classification(bytes_io.getvalue())  # 识别字体

            # 构建字体印射规则
            if word:
                font_mapping[word] = [cmap_code, glyph_name]  # 可以自定义返回的映射关系

        return font_mapping


if __name__ == '__main__':
    obj = FontFileMappingRelationship()  # 只需要调用一次即可
    print(obj.convert(r"测试字体.woff"))  # 多次调用
    print(obj.convert(r"测试字体.woff"))  # 多次调用
