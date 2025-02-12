"""可以看到运行的时候会抢占资源，导致运行报错或结果不正确"""

import threading

with open('测试文件.txt', mode='w', encoding='utf-8') as f:
    f.write('0')


def job():
    for i in range(5):
        with open('测试文件.txt', mode='r', encoding='utf-8') as f:
            number = f.read()

        number = int(number) + 1

        with open('测试文件.txt', mode='w', encoding='utf-8') as f:
            f.write(str(number))


th_job = threading.Thread(target=job)
th1_job = threading.Thread(target=job)
th_job.start()
th1_job.start()

while len(threading.enumerate()) > 1:  # 线程数量：本身线程和子线程
    pass
print("执行完成")
