import multiprocessing
import os
import time


# 复用进程的Process类
class ReuseProcess(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.daemon = True
        self.queue = queue

    def run(self):
        while True:
            func, args, kwargs = self.queue.get()
            print("Hoo1 进程名：%s" % (os.getpid()))
            func(*args, **kwargs)
            self.queue.task_done()

    def add_new_task(self, func, *args, **kwargs):
        print("Hook2 进程名：%s" % (os.getpid()))
        self.queue.put((func, args, kwargs))

    def join(self):
        print("Hook3 进程名：%s" % (os.getpid()))
        self.queue.join()


# 测试用的函数
def func(name):
    print("Hoo4 进程名：%s" % (os.getpid()))
    time.sleep(1)
    print(name)


if __name__ == "__main__":
    print("Hoo5 进程名：%s" % (os.getpid()))
    queue = multiprocessing.Manager().Queue()
    process = ReuseProcess(queue)  # 新建可复用的进程
    process.start()
    process.add_new_task(func, "任务1")  # 给进程添加任务并执行
    process.add_new_task(func, "任务2")
    process.join()
    process.kill()
