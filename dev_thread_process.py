import os  # 获取进程号
import threading  # 获取线程号
import time
from concurrent.futures import ThreadPoolExecutor  # 线程池
from multiprocessing import Pool
from unicodedata import name  # 进程池

thread_workers = 2  # 线程池的线程数量，每个进程有自己的线程池。
thread_executor = ThreadPoolExecutor(max_workers=thread_workers)


# 定义线程要执行的函数，线程阻塞1秒然后打印
def thread_action(task_id, start_time):
    time.sleep(1)
    end_time = time.time()
    print(
        "进程号: %s\t线程号: %s\t任务号: %d\t完成时间: %d"
        % (
            os.getpid(),
            threading.current_thread().name,
            task_id,
            end_time - float(start_time),
        )
    )


# 定义进程要执行的函数，其实就是调用线程
def process_action(task_id, start_time):
    time.sleep(0.001)
    thread_executor.submit(
        thread_action, task_id, start_time
    )  # 让线程池中的线程执行函数


if __name__ == "__main__":
    pool = Pool(processes=2)  # 额外开启2个进程
    start_time = time.time()
    for i in range(8):  # 将8次任务分配在2个进程上
        pool.apply_async(func=process_action, args=(i, start_time))
    pool.close()  # 进程池不再接收新任务，只等旧任务都完成后就会关闭
    pool.join()  # 让主进程等待进程池
