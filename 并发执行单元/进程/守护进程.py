"""只要主进程执行完成，子进程就会强制退出"""
import time
import multiprocessing


def fun():
    """因为主进程运行比子进程快，所以该进程被强制退出了"""
    time.sleep(3)
    print("子进程打印结果")


if __name__ == '__main__':
    th_fun = multiprocessing.Process(target=fun)

    th_fun.daemon = True  # 守护进程，放在启动之前

    th_fun.start()

    print("运行结束")
