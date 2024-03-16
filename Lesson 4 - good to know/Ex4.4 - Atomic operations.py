import asyncio


# # Example 1 - Race condition
# Общий ресурс, который будет обновляться
shared_resource = 0


async def update_resource():

    # Используем глобальную переменную shared_resource
    global shared_resource
    print('Начинаем обновление shared_resource')

    # Сохраняем текущее значение shared_resource во временную переменную
    temp = shared_resource

    # Имитация операции ввода-вывода
    await asyncio.sleep(0.1)

    # Увеличиваем значение shared_resource на 1
    shared_resource = temp + 1
    print('Обновление shared_resource завершено')


async def main():
    print("---------- Race condition ----------")
    await asyncio.gather(update_resource(), update_resource())
    print(f'shared_resource: {shared_resource}')

asyncio.run(main())


# # Example 2 - Avoiding race conditions using atomic operations concept with asyncio.Lock()
shared_resource = 0

# Создаем асинхронный замок для обеспечения безопасности при обновлении shared_resource
lock = asyncio.Lock()


async def update_resource():

    # Используем глобальную переменную shared_resource
    global shared_resource
    print('Начинаем обновление shared_resource')

    # Используем асинхронный замок для обеспечения безопасности при обновлении shared_resource
    async with lock:

        # Сохраняем текущее значение shared_resource во временную переменную
        temp = shared_resource
        await asyncio.sleep(0.1)

        # Увеличиваем значение shared_resource на 1
        shared_resource = temp + 1
    print('Обновление shared_resource завершено')


async def main():
    print("---------- Atomic requests ----------")
    await asyncio.gather(update_resource(), update_resource())
    print(f'shared_resource: {shared_resource}')

asyncio.run(main())


# # Example 3 - Is asyncio.Lock() truly atomic?
shared_resource_1 = 0
shared_resource_2 = 0

# Создаем асинхронный замок для обеспечения безопасности при обновлении shared_resource
lock = asyncio.Lock()


async def update_resource(n):

    # Используем глобальную переменную shared_resource
    global shared_resource_1, shared_resource_2
    print(f'Начинаем обновление shared_resource корутиной {n}')

    # Используем асинхронный замок для обеспечения безопасности при обновлении shared_resource
    try:
        async with lock:
            # Сохраняем текущее значение shared_resource во временную переменную
            shared_resource_1 += 1
            await asyncio.sleep(1)
            if n == 2:
                raise Exception('Atomic exception!')
            # Увеличиваем значение shared_resource на 1
            shared_resource_2 += 1
    except Exception as e:
        print('Возникло исключение:', e)
    print('Обновление shared_resource завершено')


async def main():
    print("---------- Is asyncio.Lock() truly atomic? ----------")
    await asyncio.gather(update_resource(1), update_resource(2))
    print(f"{shared_resource_1=} \n{shared_resource_2=}")

asyncio.run(main())

