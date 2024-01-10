import asyncio

async def task1():
    await asyncio.sleep(1)
    print("Задача 1 завершена")

async def task2():
    await asyncio.sleep(2)
    print("Задача 2 завершена")

async def main():
    tasks = [task1(), task2()]
    await asyncio.gather(*tasks)

asyncio.run(main())