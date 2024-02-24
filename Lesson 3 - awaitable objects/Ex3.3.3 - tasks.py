# Task 1
import asyncio


async def task1():
    await asyncio.sleep(2)
    print("Привет из корутины task1")


async def task2():
    await asyncio.sleep(1)
    print("Привет из корутины task2")


async def main():
    # без конкурентности
    await asyncio.create_task(task1())
    await asyncio.create_task(task2())
    # с конкурентностью
    # await asyncio.gather(task1(), task2())

asyncio.run(main())


# Task 2
async def task1():
    print("Начинаем задачу 1")
    await asyncio.sleep(1)
    print("Привет из корутины task1")
    await asyncio.sleep(1)
    print("Задача 1 завершилась")


async def task2():
    print("Начинаем задачу 2")
    await asyncio.sleep(2)
    print("Привет из корутины task2")
    await asyncio.sleep(2)
    print("Задача 2 завершилась")


async def task3():
    print("Начинаем задачу 3")
    await asyncio.sleep(3)
    print("Привет из корутины task3")
    await asyncio.sleep(3)
    print("Задача 3 завершилась")


async def main():
    task_1 = asyncio.create_task(task1())
    task_2 = asyncio.create_task(task2())
    task_3 = asyncio.create_task(task3())

    print("Решение через await asyncio.gather")
    await asyncio.gather(task_1, task_2, task_3)


asyncio.run(main())


## Version 2
import asyncio

async def task1():
    print("Начинаем задачу 1")
    await asyncio.sleep(1)
    print("Привет из корутины task1")
    await asyncio.sleep(1)
    print("Задача 1 завершилась")

async def task2():
    print("Начинаем задачу 2")
    await asyncio.sleep(2)
    print("Привет из корутины task2")
    await asyncio.sleep(2)
    print("Задача 2 завершилась")

async def task3():
    print("Начинаем задачу 3")
    await asyncio.sleep(3)
    print("Привет из корутины task3")
    await asyncio.sleep(3)
    print("Задача 3 завершилась")

async def main():
    task_1 = asyncio.create_task(task1())
    task_2 = asyncio.create_task(task2())
    task_3 = asyncio.create_task(task3())

    # Когда авэйтим таски, они конкурируют
    print("Решение через await тасков")
    await task_1
    await task_2
    await task_3

    # Если напрямую авэйтить корутины, они не конкурируют
    print("Решение через await корутин")
    await task1()
    await task2()
    await task3()

asyncio.run(main())


# Task 3
async def compute_square(x):
    print(f"Вычисляем квадрат числа: {x}")
    await asyncio.sleep(1)  # Имитация длительной операции
    return x * x


async def main():
    results = [asyncio.create_task(compute_square(i)) for i in range(10)]
    completed, pending = await asyncio.wait(results)
    for task in completed:
        print(f"Результат: {task.result()}")


asyncio.run(main())
