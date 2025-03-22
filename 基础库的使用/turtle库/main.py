import turtle

# 创建一个画布（窗口）
window = turtle.Screen()

# 创建一个海龟对象
t = turtle.Turtle()

# 画出五角星
for i in range(1, 6):
    t.seth(-144 * i)
    t.fd(100)

# 抬起画笔
t.penup()
# 移动99位置
t.fd(99)

window.mainloop()  # 保持窗口打开
