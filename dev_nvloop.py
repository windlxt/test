import asyncio

import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


async def main():
    loop = asyncio.get_running_loop()
    future = loop.create_future()
    loop.call_soon(future.set_result, lambda: print("Hello, Future!"))
    result = await future
    result()  # 调用结果函数

    # asyncio.run(main())

    # async def main():
    #     loop = asyncio.get_running_loop()
    #     loop.call_soon(lambda: print("Callback executed immediately"))
    loop.call_later(2, lambda: print("Callback executed after 2 seconds"))
    await asyncio.sleep(4)  # 等待足够的时间以触发回调


# asyncio.run(asyncio.Task(main()))
asyncio.run(main())
