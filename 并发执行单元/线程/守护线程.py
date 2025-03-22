"""只要主线程执行完成，子线程就会强制退出"""
import time
import threading


def fun():
    """因为主线程运行比子线程快，所以该线程被强制退出了"""
    time.sleep(3)
    print("子线程打印结果")


th_fun = threading.Thread(target=fun)

th_fun.daemon = True  # 守护线程，放在启动之前

th_fun.start()

print("运行结束")
