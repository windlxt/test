import queue
import threading


class ReuseThread(threading.Thread):
    def __init__(self):
        super().__init__()  # 使用父类Thread的初始化函数
        self.queue = queue.Queue()  # 用队列queue新增其他函数
        self.daemon = True  # 设置父类的全局变量daemon为true，说明该线程为守护线程
        # 如果进程中只有守护线程在运行，那么进程会结束，所有守护线程也会关闭

    def run(self):  # 线程一旦被处理器运行，会自动调用run()方法
        while True:  # 让该线程执行的函数不停止，即让调用栈不为空，从而线程不被销毁
            func, args, kwargs = self.queue.get()  # 获取函数、参数来执行
            print(
                "Hook 1: %s" % threading.current_thread().name
            )  # 看是哪个线程在执行该行代码
            func(*args, **kwargs)
            self.queue.task_done()  # 告知队列取出的任务已完成
            # self.queue.task_done() 用于告诉self.queue.join()该任务已完成

    def add_new_task(
        self, func, *args, **kwargs
    ):  # 外界线程访问这个函数为执行run方法的线程新增函数
        print(
            "Hook 2: %s" % threading.current_thread().name
        )  # 看是哪个线程在执行该行代码
        self.queue.put((func, args, kwargs))  # 在队列queue里新增函数、参数

    # 外界线程通过这个函数让外界线程阻塞，等待queue的任务都完成后，外界线程才能被处理器执行。
    def join(self):
        print(
            "Hook 3: %s" % threading.current_thread().name
        )  # 看是哪个线程在执行该行代码
        self.queue.join()  # 由self.queue.task_done()告诉self.queue.join()是不是所有入队的任务都完成了。


# 要给可复用的线程新增的函数
def func(name):
    print("Hook 4: %s" % threading.current_thread().name)  # 看是哪个线程在执行该行代码
    print(name)


if __name__ == "__main__":
    print("Hook 5: %s" % threading.current_thread().name)  # 看是哪个线程在执行该行代码
    t = ReuseThread()
    t.start()
    t.add_new_task(func, "任务 1")
    t.add_new_task(func, "任务 2")
    t.join()
