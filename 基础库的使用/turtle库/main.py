import turtle

# 创建一个画布（窗口）
window = turtle.Screen()

# 创建一个海龟对象
t = turtle.Turtle()

# 填充颜色对象
t.color("red", "yellow")

# 开始填充颜色
t.begin_fill()

# 画出五角星
for i in range(1, 6):
    t.seth(-144 * i)
    t.fd(100)

# 结束填充颜色
t.end_fill()

# 抬起画笔
t.penup()
# 移动99位置
t.fd(99)

window.mainloop()  # 保持窗口打开
