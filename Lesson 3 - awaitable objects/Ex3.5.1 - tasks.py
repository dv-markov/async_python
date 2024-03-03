import asyncio
from random import random


async def my_coroutine():
    await asyncio.sleep(random())
    print("Задача выполнена")


async def main():
    task = asyncio.create_task(my_coroutine())   # Создаем задачу из корутины. Этот метод позволяет начать выполнение корутины и возвращает объект Task, который можно ожидать
    print(type(task))
    await task                                   # Ожидаем выполнения задачи. Благодаря этому код будет ждать выполнения задачи, прежде чем завершиться


asyncio.run(main())


# Список поваров.
chef_list = ['Франсуа', 'Жан', 'Марсель']


async def cook_order(order_number, dish):
    # Повар готовит блюдо
    print(f"Повар {chef_list[order_number - 1]} начинает готовить заказ №{order_number}: {dish}")
    await asyncio.sleep(random()*2)  # Имитация времени на готовку
    print(f"Заказ №{order_number}: {dish} готов!")
    return f"{dish} для заказа №{order_number}"


async def serve_order(order_number, dish):
    # Официант подает блюдо
    cooked_dish = await cook_order(order_number, dish)
    print(f"Официант подает {cooked_dish}")


async def manager():
    # Менеджер (событийный цикл) назначает задачи
    orders = [(1, 'Салат'), (2, 'Стейк'), (3, 'Суп')]
    tasks = [asyncio.create_task(serve_order(order_number, dish)) for order_number, dish in orders]

    # Ожидаем завершения всех задач
    await asyncio.gather(*tasks)


# Запуск событийного цикла
asyncio.run(manager())


# Пример плохого кода, создание задачи без ссылки на нее
async def my_background_task():
    await asyncio.sleep(1)
    print("Task completed")

    # Запускаем задачу без сохранения ссылки на нее
    # Эта задача может быть удалена сборщиком мусора до ее выполнения, потому что на нее нет ссылок
    asyncio.create_task(my_background_task())


asyncio.run(my_background_task())


# Пример создания задачи с сохранением ссылки на нее
async def my_task():
    print("Running my task")
    await asyncio.sleep(1)
    print("Task complete")


async def main():
    task = asyncio.create_task(my_task())
    await asyncio.sleep(2)

asyncio.run(main())


# Множественное создание задач в цикле
async def my_task(i):
    print(f"Запуск задачи {i}")
    await asyncio.sleep(random()*4)
    print(f"Задача {i} Завершена")


async def main():
    tasks = []
    for x in range(5):
        task = asyncio.create_task(my_task(x))
        tasks.append(task)
    await asyncio.gather(*tasks)


asyncio.run(main())
