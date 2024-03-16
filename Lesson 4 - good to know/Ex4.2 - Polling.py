import asyncio
import random


# Example 1
async def process_data(data):
    print(f"Полученные данные: {data}")

    # Может включать в себя любую другую логику, которую вы хотите выполнить с полученными данными,
    # например, сохранение в базу данных, отправку уведомлений или обновление интерфейса пользователя.


# Асинхронная функция для опроса сетевого устройства
async def polling_network_device():
    while True:
        data = random.randint(0, 1000000)  #
        await process_data(data)

        # Здесь мы можем выполнить какие-то действия,
        # такие как отправку запроса к устройству и получение ответа

        # Ожидание 5 секунд перед следующим опросом
        await asyncio.sleep(5)


async def main():
    task = asyncio.create_task(polling_network_device())
    await task

# asyncio.run(main())


# Example 2
async def print_message():
    while True:
        print("Имитация работы функции")
        await asyncio.sleep(1)


async def interrupt_handler(interrupt_flag):
    while True:
        # Если interrupt_flag установлен Выводим сообщение о прерывании
        await asyncio.sleep(0.5)
        if interrupt_flag.is_set():
            print("Произошло прерывание!, в этом месте может быть установлен любой обработчик")

            # Очищаем interrupt_flag
            interrupt_flag.clear()
            break


async def main():
    # Создаем флаг interrupt_flag с помощью asyncio.Event
    interrupt_flag = asyncio.Event()

    # Создаем задачу исполняющую функцию print_message
    # asyncio.create_task(print_message())   # Создаем задачу task1 исполняющую функцию print_message
    asyncio.ensure_future(print_message())  # Создаем задачу task1 исполняющую функцию print_message
    task2 = asyncio.create_task(interrupt_handler(interrupt_flag))
    while True:
        await asyncio.sleep(3)
        # Устанавливаем interrupt_flag
        interrupt_flag.set()
        await task2
        task2 = asyncio.create_task(interrupt_handler(interrupt_flag))

asyncio.run(main())
