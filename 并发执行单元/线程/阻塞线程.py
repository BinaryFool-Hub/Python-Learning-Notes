"""让子线程执行完毕，再继续运行主线程"""
import time
import threading


def fun():
    """因为使用了阻塞线程，所以需要等待该线程执行完成再继续执行主线程"""
    print("子线程开始执行")
    time.sleep(3)
    print("子线程执行完毕")


print("主线程开始执行")

th_fun = threading.Thread(target=fun)

th_fun.start()

th_fun.join()  # 阻塞线程，放在开始执行子线程之后

print("主线程执行完毕")
