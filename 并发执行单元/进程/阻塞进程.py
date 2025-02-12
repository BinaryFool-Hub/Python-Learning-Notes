"""让子进程执行完毕，再继续运行主进程"""
import time
import multiprocessing


def fun():
    """因为使用了阻塞进程，所以需要等待该进程执行完成再继续执行主进程"""
    print("子进程开始执行")
    time.sleep(3)
    print("子进程执行完毕")


if __name__ == '__main__':
    print("主进程开始执行")

    th_fun = multiprocessing.Process(target=fun)

    th_fun.start()

    th_fun.join()  # 阻塞进程，放在开始执行子进程之后

    print("主进程执行完毕")
