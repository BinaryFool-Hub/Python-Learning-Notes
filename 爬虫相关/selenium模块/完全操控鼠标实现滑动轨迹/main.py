import pyautogui
import random
import time


def move_slide1(offset_x, offset_y, len_info):
    """
    输入的坐标是针对于整个屏幕的
    :param offset_x: x轴坐标
    :param offset_y: y轴坐标
    :param len_info: 需要移动的距离, 从左往右
    :return:
    """

    # moveTo屏幕坐标移动到指定为止, duration参数是消耗时间
    pyautogui.moveTo(
        offset_x,
        offset_y,
        duration=0.1 + random.uniform(0, 0.1 + random.randint(1, 100) / 100))

    # mouseDown()  按下鼠标, 保持按下的动作
    pyautogui.mouseDown()

    offset_y += random.randint(9, 19)
    # moveTo 移动鼠标;  offset_x 横向移动的距离; offset_y 纵向移动的距离  在y轴上移动为了更像人
    pyautogui.moveTo(
        offset_x + int(len_info * random.randint(15, 25) / 20),
        offset_y,
        duration=0.28)

    offset_y += random.randint(-9, 0)
    pyautogui.moveTo(
        offset_x + int(len_info * random.randint(18, 22) / 20),
        offset_y,
        duration=random.randint(19, 31) / 100)

    offset_y += random.randint(0, 8)
    pyautogui.moveTo(
        offset_x + int(len_info * random.randint(19, 21) / 20),
        offset_y,
        duration=random.randint(20, 40) / 100)

    offset_y += random.randint(-3, 3)
    pyautogui.moveTo(
        len_info + offset_x + random.randint(-3, 3),
        offset_y,
        duration=0.5 + random.randint(-10, 10) / 100)

    offset_y += random.randint(-2, 2)
    pyautogui.moveTo(
        len_info + offset_x + random.randint(-2, 2),
        offset_y,
        duration=0.5 + random.randint(-3, 3) / 100)

    # mouseUp()  松开鼠标
    pyautogui.mouseUp()
    time.sleep(3)
