import threading

"""导入锁的模块"""
lock = threading.Lock()

with open('测试文件.txt', mode='w', encoding='utf-8') as f:
    f.write('0')


def job():
    for i in range(5):
        """进行上锁的保护"""
        lock.acquire()

        with open('测试文件.txt', mode='r', encoding='utf-8') as f:
            number = f.read()

        number = int(number) + 1

        with open('测试文件.txt', mode='w', encoding='utf-8') as f:
            f.write(str(number))

        """释放锁,上了锁就一定是要释放,不然会造成死锁,卡死在循环里面"""
        lock.release()


th_job = threading.Thread(target=job)
th1_job = threading.Thread(target=job)
th_job.start()
th1_job.start()

while len(threading.enumerate()) > 1:  # 线程数量：本身线程和子线程
    pass

print("执行完成")
