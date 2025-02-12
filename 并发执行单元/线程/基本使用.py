import threading
import time


def work(n):
    # 模拟执行的任务时间
    time.sleep(3)
    print(f"{n}子线程work执行完成")


def work1(n):
    # 模拟执行的任务时间
    time.sleep(6)
    print(f"{n}子线程work1执行完成")


print("任务开始执行")

"""主线程依次往下执行，然后分配给子线程执行，主线程继续执行下面代码
可以使用 kwargs(字典类型) 和 args(元组类型) 传入参数
"""
work_th = threading.Thread(target=work, kwargs={'n': 'work_th'})  # 创建子线程对象
work_th.start()  # 执行子线程对象，不会等待执行完成

work1_th = threading.Thread(target=work1, args=('work1_th',))  # 创建子线程对象
work1_th.start()  # 执行子线程对象，不会等待执行完成

print("主线程执行完成")
