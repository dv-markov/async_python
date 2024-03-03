import asyncio


# Асинхронность - Кооперативная многозадачность (Cooperative Multitasking)
async def fetch_data():
    await asyncio.sleep(3)
    return "Результат выполнения корутины fetch_data"


async def main():  # Первая запускаемая корутина, из неё можно запускать остальные и возвращать результат для удобства
    print("Получение данных...")
    data = await fetch_data()
    print("Данные:", data)


asyncio.run(main())  # Точка входа


# Question 10
async def slow_operation():
    return "Slow operation result"


async def main():
    result = slow_operation()
    print(result)


asyncio.run(main())
