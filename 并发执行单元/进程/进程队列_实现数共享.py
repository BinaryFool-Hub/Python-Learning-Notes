import multiprocessing

# 如果是用普通的列表或普通的队列对象则无效，数据不共享，所以需要使用进行队列
# 创建进程队列，实现数据共享，直接传入到函数的参数即可，会自动进行数据处理
process = multiprocessing.Queue(maxsize=10)


def job(arr):
    arr.put(1)
    arr.put(2)
    arr.put(3)


if __name__ == '__main__':
    work = multiprocessing.Process(target=job, args=(process,))
    work.start()

    while work.is_alive():
        pass

    print(process.qsize())
