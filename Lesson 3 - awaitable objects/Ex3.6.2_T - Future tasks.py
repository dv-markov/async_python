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
# # Version 1 - with Future object
async def set_future_result(value, delay):
    print(f"Задача начата. Установка результата '{value}' через {delay} секунд.")
    await asyncio.sleep(delay)
    print("Результат установлен.")
    return value


async def create_and_use_future(future):
    future_result = asyncio.ensure_future(set_future_result("Успех", 0.2))
    # print(f"Состояние Future до выполнения: {future.done()}")
    print(f"Состояние Future до выполнения: {get_future_status(future)}")
    print("Задача запущена, ожидаем завершения...")
    future.set_result(await future_result)
    # print(f"Состояние Future после выполнения: {future.done()}")
    print(f"Состояние Future после выполнения: {get_future_status(future)}")
    return future.result()


def get_future_status(future):
    return "Завершено" if future.done() else "Ожидание"


async def main():
    future_1 = asyncio.Future()
    result = await create_and_use_future(future_1)
    print("Результат из Future:", result)

asyncio.run(main())


# # Version 2 - Future object is created with `ensure_future`
async def set_future_result(value, delay):
    print(f"Задача начата. Установка результата '{value}' через {delay} секунд.")
    await asyncio.sleep(delay)
    print("Результат установлен.")
    return value


async def create_and_use_future():
    # future = asyncio.ensure_future(set_future_result("Успех", 0.2))
    # ensure_future is identical to create_task for coroutines
    future = asyncio.create_task(set_future_result("Успех", 0.2))
    print(type(future))
    print(f"Состояние Future до выполнения: {future.done()}")
    print(f"Состояние Future до выполнения: {get_future_status(future)}")
    print("Задача запущена, ожидаем завершения...")
    await future
    print(f"Состояние Future после выполнения: {future.done()}")
    print(f"Состояние Future после выполнения: {get_future_status(future)}")
    return future.result()


def get_future_status(future):
    return "Завершено" if future.done() else "Ожидание"


async def main():
    result = await create_and_use_future()
    print("Результат из Future:", result)

asyncio.run(main())


# Task 3
async def async_operation():
    print("Начало асинхронной операции.")
    try:
        await asyncio.sleep(2)
    except asyncio.CancelledError:
        print("Асинхронная операция была отменена в процессе выполнения.")
        raise
    print("Асинхронная операция успешно завершилась.")


async def main():
    print("Главная корутина запущена.")
    future = asyncio.ensure_future(async_operation())
    await asyncio.sleep(0.1)
    print("Попытка отмены Future.")
    future.cancel()
    try:
        result = await future
        print("Результат Future:", result)
    except asyncio.CancelledError:
        print("Обработка исключения: Future был отменен.")
    if future.cancelled():
        print("Проверка: Future был отменен.")
    else:
        print("Проверка: Future не был отменен.")
    print("Главная корутина завершена.")


asyncio.run(main())


# Task 4
async def first_function(x):
    print(f"Выполняется первая функция с аргументом {x}")
    await asyncio.sleep(1)
    result = x + 1
    print(f"Первая функция завершилась с результатом {result}")
    return result


async def second_function(x):
    print(f"Выполняется вторая функция с аргументом {x}")
    await asyncio.sleep(1)
    result = x * 2
    print(f"Вторая функция завершилась с результатом {result}")
    return result


async def third_function(x):
    print(f"Выполняется третья функция с аргументом {x}")
    await asyncio.sleep(1)
    result = x + 3
    print(f"Третья функция завершилась с результатом {result}")
    return result


async def fourth_function(x):
    print(f"Выполняется четвертая функция с аргументом {x}")
    await asyncio.sleep(1)
    result = x ** 2
    print(f"Четвертая функция завершилась с результатом {result}")
    return result


async def main():
    print("Начало цепочки асинхронных вызовов")
    res_1 = await asyncio.ensure_future(first_function(1))
    res_2 = await asyncio.ensure_future(second_function(res_1))
    res_3 = await asyncio.ensure_future(third_function(res_2))
    res_4 = await asyncio.ensure_future(fourth_function(res_3))
    print(f"Конечный результат цепочки вызовов: {res_4}")

asyncio.run(main())

