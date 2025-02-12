from PIL import Image, ImageDraw

# 加载图片
image_path = 'images/多重缺口.png'
image = Image.open(image_path)

# 指定坐标
coordinates = [215, 45, 260, 91]

# 创建一个可用于绘制的对象
draw = ImageDraw.Draw(image)

# 绘制红色矩形框
draw.rectangle(coordinates, outline='red', width=3)

# 保存修改后的图片
output_image_path = 'output_image.jpg'
image.save(output_image_path)

print(f"图片已保存为 {output_image_path}")
