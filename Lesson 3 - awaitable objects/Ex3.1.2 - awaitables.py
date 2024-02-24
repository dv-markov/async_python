import asyncio


# Определение корутины
async def my_coroutine():
    print("Запуск корутины")
    await asyncio.sleep(1)  # Приостановка корутины на 1 секунду
    print("Завершение корутины")


# Создание задачи из корутины
async def main():
    task = asyncio.create_task(my_coroutine())
    await task


# Запуск event loop
asyncio.run(main())


# Определение асинхронной функции (корутины) cook_dish(n), которая имитирует повара, готовящего блюдо. Используется
# корутина для того, чтобы конкурентно запускать несколько "поваров" и использовать время ожидания (приготовление)
# эффективно.
async def cook_dish(n):
    print(f"Повар {n} начинает готовить")       # Повар n начинает готовить
    await asyncio.sleep(n)                      # Повар готовит блюдо n секунд. asyncio.sleep(n) используется для
    # имитации задержки, которая требуется для приготовления блюда.
    print(f"Повар {n} закончил готовить")       # Повар n закончил готовить
    return f"Блюдо от повара {n}"               # Возвращает строку, указывающую, что блюдо от повара n готово.


# Создание задач из корутин, которые представляют собой приготовление блюда каждым поваром.
async def main():
    print("Function `main` started to work")
    # Создаются задачи для каждого повара (от 1 до
    # 3). Используется create_task для запуска корутины.
    tasks = [asyncio.create_task(cook_dish(n)) for n in range(1, 5)]
    print("Tasks created")

    # Ожидает завершения всех задач, затем выводит результат.
    # asyncio.gather используется для ожидания всех корутин, затем собирает их результаты в список.
    print(await asyncio.gather(*tasks))


# Запуск главной корутины
asyncio.run(main())
