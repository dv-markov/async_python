import asyncio


# Task 1
async def main():
    print("Hello, Asyncio!")

asyncio.run(main())


# Task 2
async def coro_1():
    print("coro_1 says, hello coro_2!")


async def coro_2():
    print("coro_2 says, hello coro_1!")


async def main():
    await asyncio.gather(coro_1(), coro_2())


asyncio.run(main())


# Task 3
async def generate(number):
    print(f"Корутина generate с аргументом {number}")


async def main():
    tasks = [generate(x) for x in range(10)]
    await asyncio.gather(*tasks)


asyncio.run(main())


# Task 4
async def coro_1():
    print("Вызываю корутину 0")


async def coro_5():
    print("Вызываю корутину 3")
    await coro_3()


async def coro_3():
    print("Вызываю корутину 2")
    await coro_2()


async def coro_4():
    print("Вызываю корутину 1")
    await coro_1()


async def coro_2():
    print("Вызываю корутину 4")
    await coro_4()


asyncio.run(coro_5())
