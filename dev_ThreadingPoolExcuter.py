import concurrent.futures
import threading
import time
from concurrent.futures import ThreadPoolExecutor

WORKERS = 2
thread_pool = ThreadPoolExecutor(
    max_workers=WORKERS
)  # max_workers指定了复用线程的最大数量


# 延时打印id的任务
def thread_action(task_identifier, start_time):
    time.sleep(1)
    end_time = time.time()
    print(
        "任务id: %d\t线程: %s\t完成时间: %d"
        % (
            task_identifier,
            threading.current_thread().name,
            end_time - float(start_time),
        )
    )
    return task_identifier


task_num = 4  # 任务数量
future_list = []  # 放置submit()得到的Future对象
start_time = time.time()

# submit()提交任务
for task_id in range(task_num):
    future = thread_pool.submit(thread_action, task_id, start_time)
    future_list.append(future)

# 获取函数return的结果
for future in concurrent.futures.as_completed(future_list):
    # for future in future_list:
    print("返回的任务名: %d" % future.result())
