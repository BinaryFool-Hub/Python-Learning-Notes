import multiprocessing
import time


def work(n):
    # 模拟执行的任务时间
    time.sleep(3)
    print(f"{n}子进程work执行完成")


if __name__ == '__main__':
    work_mu = multiprocessing.Process(target=work, kwargs={'n': 'work_th'})
    work_mu.start()

    """判断是否在运行"""
    result = work_mu.is_alive()
    print(result)
