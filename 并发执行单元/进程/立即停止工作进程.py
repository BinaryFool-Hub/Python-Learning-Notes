import multiprocessing
import time


def work(n):
    # 模拟执行的任务时间
    time.sleep(3)
    print(f"{n}子进程work执行完成")


if __name__ == '__main__':
    work_mu = multiprocessing.Process(target=work, kwargs={'n': 'work_th'})
    work_mu.start()

    """不管任务是否完成，立即停止工作进程"""
    work_mu.terminate()

    print("运行完成")
