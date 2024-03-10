import asyncio


# Task 1
async def main():
    fut = asyncio.Future()
    fut.set_result('Привет, мир!')
    fut.cancel()

    print(fut.result())

asyncio.run(main())


# Task 2
async def set_after(fut, delay, value):
    await asyncio.sleep(delay)
    fut.set_result(value)


async def main():
    future = asyncio.Future()
    asyncio.ensure_future(set_after(future, 0.05, 'done'))
    result = await future
    print(result)

asyncio.run(main())


# Task 3
