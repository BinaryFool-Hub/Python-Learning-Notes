# https://github.com/sml2h3/ddddocr
# 针对于单一缺口图片和完整背景
import ddddocr

slide = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)
"""注解
ocr=False --> 关闭ocr功能
det=False --> 关闭目标检测功能
show_ad=False --> 关闭广告
"""

with open('images/缺口图片.jpg', 'rb') as f:
    target_bytes = f.read()

with open('images/完整背景.jpg', 'rb') as f:
    background_bytes = f.read()

res = slide.slide_comparison(target_bytes, background_bytes)
"""注解
slide_comparison(target_bytes, background_bytes) 
-- 是一个滑块检测函数，里面接受两个二进制图片数据(第一个是滑块，第二个是滑块背景)，然后返回识别出的坐标
-- 然后返回x,y轴相对于左侧的距离，也就是滑动距离
"""

print(res)
