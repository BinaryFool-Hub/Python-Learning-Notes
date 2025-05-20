# https://github.com/sml2h3/ddddocr
# 针对缺口图片和滑块，可以结合 图片4方坐标绘制显示.py 来绘画出区域
import ddddocr

det = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)
"""注解
ocr=False --> 关闭ocr功能
det=False --> 关闭目标检测功能
show_ad=False --> 关闭广告
"""

with open('images/滑块.png', 'rb') as f:
    target_bytes = f.read()

with open('images/多重缺口.png', 'rb') as f:
    background_bytes = f.read()

res = det.slide_match(target_bytes, background_bytes, simple_target=False)
"""注解
simple_target=False 
-- 默认为False，由于滑块图可能存在透明边框的问题，导致计算结果不一定准确，需要自行估算滑块图透明边框的宽度用于修正得出的bbox
-- 如果滑块无过多背景部分，则可以添加simple_target参数为True， 通常为jpg或者bmp格式的图片

slide_match(target_bytes, background_bytes) 
-- 是一个滑块检测函数，里面接受两个二进制图片数据(第一个是滑块，第二个是滑块背景)，然后返回识别出的坐标
"""

print(res)
