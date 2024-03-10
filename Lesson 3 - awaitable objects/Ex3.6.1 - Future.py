import asyncio


# Ex 1
async def simulate_long_running_task(name, delay, future: asyncio.Future):
    """Асинхронная функция, имитирующая длительную задачу."""
    print(f"Задача '{name}' началась, будет выполнена за {delay} секунд.")
    await asyncio.sleep(delay)
    result = f"Результат задачи '{name}'"
    print(f"Задача '{name}' завершена.")
    if not future.done():
        future.set_result(result)  # Устанавливаем результат для Future объекта


async def main():
    # Создаем объект Future
    future = asyncio.Future()

    # Запускаем корутину, передаем Future объект в функцию
    await simulate_long_running_task("Задача1", 3, future)

    # Получаем результат выполнения задачи
    result = future.result()
    print(f"Результат Future: {result}")


asyncio.run(main())


# Ex 2
async def wait_for_materials(delivery_time, future: asyncio.Future):
    """
    Асинхронная функция, имитирующая ожидание доставки строительных материалов.
    delivery_time - время, необходимое для доставки материалов.
    """

    print(f"Ожидание доставки материалов. Доставка займет {delivery_time} секунд.")
    await asyncio.sleep(delivery_time)  # Имитация задержки доставки
    print("Материалы доставлены.")
    if not future.done():
        future.set_result("Доставка завершена")


async def manage_construction_project():
    """
    Менеджер строительного проекта, который ожидает поставку материалов,
    прежде чем продолжить работу над проектом.
    """

    # Создание Future объекта
    future_materials_delivery = asyncio.Future()

    # Инициирование ожидания доставки материалов
    asyncio.create_task(wait_for_materials(5, future_materials_delivery))

    # Вы можете здесь добавить другие задачи, которые могут выполняться параллельно

    # Ожидание результата Future
    await future_materials_delivery

    # Получение и вывод результата доставки
    delivery_result = future_materials_delivery.result()
    print(f"Результат доставки: {delivery_result}")

    # После доставки можно продолжить работы над проектом
    print("Продолжение строительных работ.")


asyncio.run(manage_construction_project())


# Ex 3
async def do_some_work_1(x, future: asyncio.Future):
    print(f"Выполняется работа 1: {x}")
    await asyncio.sleep(x)
    future.set_result(x * 2)


async def do_some_work_2(x, future: asyncio.Future):
    print(f"Выполняется работа 2: {x}")
    await asyncio.sleep(x)
    future.set_result(x + 2)


async def main():
    # Создаем объекты Future для каждой задачи
    future_1 = asyncio.Future()
    future_2 = asyncio.Future()

    # Запускаем первую задачу и передаем ей Future
    asyncio.create_task(do_some_work_1(2, future_1))

    # Дожидаемся завершения первой задачи
    await future_1
    result_1 = future_1.result()

    # Запускаем вторую задачу, передавая результат первой и объект Future
    asyncio.create_task(do_some_work_2(result_1, future_2))

    # Дожидаемся завершения второй задачи
    await future_2
    result_2 = future_2.result()

    print(f"Результат future_1: {result_1}")  # Выводим результат первой задачи
    print(f"Результат future_2: {result_2}")  # Выводим результат второй задачи


asyncio.run(main())


# Ex 4
async def my_coroutine(arg):
    # Имитация асинхронной операции с задержкой
    await asyncio.sleep(1)
    print(f'Корутина my_coroutine создана с помощью {arg}')

async def main():
    # Создаем объект Future вручную
    # Это редкая ситуация, так как обычно Future создаются автоматически асинхронными операциями
    pre_existing_future = asyncio.Future()

    # Пример использования ensure_future с уже существующим объектом Future
    # В этом случае ensure_future вернет переданный ему объект Future без изменений
    future_from_future = asyncio.ensure_future(pre_existing_future)
    print(f"ensure_future с объектом Future создаёт объект с типом {type(future_from_future)}")

    # Пример использования ensure_future с корутиной
    # В этом случае ensure_future создает объект Task
    future_from_coroutine = asyncio.ensure_future(my_coroutine('ensure_future'))
    print(f"ensure_future с корутиной создаёт объект с типом {type(future_from_coroutine)}")

    # Пример использования create_task с корутиной
    # create_task всегда создает объект Task
    task = asyncio.create_task(my_coroutine('create_task'))
    print(f"create_task создаёт объект с типом {type(task)}")

    # Здесь мы "завершаем" pre_existing_future, чтобы избежать предупреждения о незавершенном задании
    # В реальных сценариях Future обычно завершаются при выполнении асинхронной операции, которую они представляют
    pre_existing_future.set_result('Результат для демонстрации')

    # Ожидаем завершения задач
    await future_from_coroutine
    await task


async def my_coroutine(arg):
    # Имитация асинхронной операции с задержкой
    await asyncio.sleep(1)
    print(f'Корутина my_coroutine создана с помощью {arg}')

async def main():
    # Создаем объект Future вручную
    # Это редкая ситуация, так как обычно Future создаются автоматически асинхронными операциями
    pre_existing_future = asyncio.Future()

    # Пример использования ensure_future с уже существующим объектом Future
    # В этом случае ensure_future вернет переданный ему объект Future без изменений
    future_from_future = asyncio.ensure_future(pre_existing_future)
    print(f"ensure_future с объектом Future создаёт объект с типом {type(future_from_future)}")

    # Пример использования ensure_future с корутиной
    # В этом случае ensure_future создает объект Task
    future_from_coroutine = asyncio.ensure_future(my_coroutine('ensure_future'))
    print(f"ensure_future с корутиной создаёт объект с типом {type(future_from_coroutine)}")

    # Пример использования create_task с корутиной
    # create_task всегда создает объект Task
    task = asyncio.create_task(my_coroutine('create_task'))
    print(f"create_task создаёт объект с типом {type(task)}")

    # Здесь мы "завершаем" pre_existing_future, чтобы избежать предупреждения о незавершенном задании
    # В реальных сценариях Future обычно завершаются при выполнении асинхронной операции, которую они представляют
    pre_existing_future.set_result('Результат для демонстрации')

    # Ожидаем завершения задач
    await future_from_coroutine
    await task


asyncio.run(main())
