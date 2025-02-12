import threading
import time


def work(n):
    # 模拟执行的任务时间
    time.sleep(3)
    print(f"{n}子线程work执行完成")


work_mu = threading.Thread(target=work, kwargs={'n': 'work_th'})
work_mu.start()

"""判断是否在运行"""
result = work_mu.is_alive()
print(result)
