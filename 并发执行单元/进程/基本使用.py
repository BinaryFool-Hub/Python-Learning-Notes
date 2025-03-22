import multiprocessing
import time


def work(n):
    # 模拟执行的任务时间
    time.sleep(3)
    print(f"{n}子进程work执行完成")


def work1(n):
    # 模拟执行的任务时间
    time.sleep(6)
    print(f"{n}子进程work1执行完成")


if __name__ == '__main__':
    """!!!一定要放入入口函数中才能运行，是不能被冻结程序"""
    print("任务开始执行")

    """主进程依次往下执行，然后分配给子进程执行，主进程继续执行下面代码
    可以使用 kwargs(字典类型) 和 args(元组类型) 传入参数
    """
    work_mu = multiprocessing.Process(target=work, kwargs={'n': 'work_th'})  # 创建子进程对象
    work_mu.start()  # 执行子进程对象，不会等待执行完成

    work1_mu = multiprocessing.Process(target=work1, args=('work1_th',))  # 创建子进程对象
    work1_mu.start()  # 执行子进程对象，不会等待执行完成

    print("执行完成")
