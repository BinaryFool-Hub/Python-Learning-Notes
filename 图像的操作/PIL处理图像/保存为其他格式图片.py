from PIL import Image

# 打开图像
image = Image.open('img/github.png')

# 保存图像
image.save("output.png")
