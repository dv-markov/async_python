import asyncio
import time


# Coroutines
async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')

asyncio.run(main())


# Sequence
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())


# Объявление корутинной функции(используется "async def")
async def coro(num, seconds):
    print(f"coro{num} начала свое выполнение")
    await asyncio.sleep(seconds)
    print(f"coro{num} выполнена за {seconds} секунду(ы)")


async def main():
    # Создание объектов корутин путем вызова корутинной функции.
    coro1 = coro(1, 2)
    coro2 = coro(2, 1)
    # Запуск и ожидание выполнения объектов корутин.
    await coro2
    await coro1

start = time.time()
asyncio.run(main())
print(f'Программа выполнена за {time.time()-start:.3f} секунд(ы)')


# Tasks
async def main2():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main2())


# TaskGroup
async def main3():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(
            say_after(1, 'hello'))

        task2 = tg.create_task(
            say_after(2, 'world'))

        print(f"started at {time.strftime('%X')}")

    # The await is implicit when the context manager exits.
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main3())


# Очередность завершения задач
async def coro(num, seconds):
    print(f"Задача{num} начала свое выполнение")
    await asyncio.sleep(seconds)
    print(f"Задача{num} выполнена за {seconds} секунду(ы)")


async def main():
    # Создание задач из корутины.
    task1 = asyncio.create_task(coro(1, 2))
    task2 = asyncio.create_task(coro(2, 1))
    # Происходит асинхронный запуск и ожидание выполнения задач.
    await task2
    await task1

start = time.time()
asyncio.run(main())
print(f'Программа выполнена за {time.time()-start:.3f} секунд(ы)')
