import asyncio


async def fetch_data():
    print("Начинаем загрузку данных")
    await asyncio.sleep(2)  # Имитация асинхронной операции ввода-вывода
    print("Данные загружены")
    return {'data': 123}


async def main():
    # Создаем список из 500 асинхронных задач, используя функцию fetch_data
    tasks = [fetch_data() for _ in range(500)]
    # Используем asyncio.gather для одновременного запуска всех задач
    results = await asyncio.gather(*tasks)
    # Для упрощения вывода в консоль покажем количество успешно выполненных задач
    print(f"Загружено {len(results)} задач")


asyncio.run(main())
