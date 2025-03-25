# 实例化画布

```python
import turtle

# 创建一个画布（窗口）
window = turtle.Screen()

# 创建一个海龟对象
t = turtle.Turtle()

window.mainloop()  # 保持窗口打开
```

# 设置画布属性

```python
import turtle

# 创建一个画布（窗口）
window = turtle.Screen()

window.bgcolor("black")  # 设置背景颜色
window.title("Turtle Graphics")  # 设置窗口标题

window.mainloop()  # 保持窗口打开
```

# 事件绑定

必须接收两个参数，不然报错

```python
import turtle

# 创建一个画布（窗口）
window = turtle.Screen()

# 创建一个海龟对象
t = turtle.Turtle()


# 定义事件处理函数
def move_forward(x, y):  # 接受 x 和 y 参数，不接受报错
    t.forward(100)  # 移动海龟向前100


# 绑定点击事件
window.onclick(move_forward)  # 点击屏幕时调用 move_forward

# 保持窗口打开
window.mainloop()

```

# 控制光标移动和绘图

都是使用实例化后的海龟对象

- 移动：
    - forward(distance)，fd(distance)：向前移动指定距离。
    - backward(distance)：向后移动指定距离。
- 转向：
    - right(angle)：向右转指定角度。
    - left(angle)：向左转指定角度。
    - seth(angle)：移动的绝对角度（自定义）。
- 画笔控制：
    - penup()：抬起画笔，移动时不绘制。
    - pendown()：放下画笔，移动时绘制。
    - pensize(width)：设置画笔宽度。
    - pencolor(color)：设置画笔颜色。
- 填充：
    - color("画笔描边色", "画笔填充色")
    - begin_fill(): 开始填充
    - end_fill(): 结束填充
- 画圆：
    - circle(radius)：绘制指定半径的圆。
        - 参数 steps 步长（分几步画完，可以得到多边形）
- 其他：
    - goto(x, y)：移动到指定坐标。
    - dot(size, color)：绘制一个点。
    - speed(speed)    设置海龟移动速度（1-10）
    - clear()    清空画布，但不改变海龟位置
    - reset()    清空画布并重置海龟位置
    - hideturtle()  # 隐藏海龟
    - showturtle()  # 显示海龟