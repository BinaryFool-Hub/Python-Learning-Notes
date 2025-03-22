from PIL import Image

result = Image.open('img/github.png')
print(result.size)  # (长, 宽)

print(result.format)  # 输出图像的格式 (如 JPEG, PNG)
print(result.mode)  # 输出图像的模式 (如 RGB, L)
