import asyncio


# Эмуляция комнаты с замком
class Room:
    def __init__(self):
        self.lock = asyncio.Lock()

    async def use(self, name):
        # Захват мьютекса - ждет, пока не освободиться mutex
        await self.lock.acquire()
        try:
            print(f"{name} вошел в комнату.")
            # Имитация выполнения работы внутри комнаты
            await asyncio.sleep(1)
            print(f"{name} вышел из комнаты.")
        finally:
            # Освобождение мьютекса
            self.lock.release()
            # pass


async def person(name, room):
    # Человек (задача) пытается использовать комнату
    print(f"{name} хочет войти в комнату.")
    await room.use(name)


async def main():
    room = Room()  # Инициализация комнаты с замком

    print("---------- Mutex - lock/acquire ----------")
    # Создание задач для нескольких людей, пытающихся войти в комнату
    await asyncio.gather(
        person("Алексей", room),
        person("Мария", room),
        person("Иван", room)
    )

asyncio.run(main())


# Вариант с контекстным менеджером with
class Room:
    def __init__(self):
        self.lock = asyncio.Lock()

    async def use(self, name):
        # Использование менеджера контекста для работы с замком
        async with self.lock:
            print(f"{name} вошел в комнату.")
            # Имитация выполнения работы внутри комнаты
            await asyncio.sleep(1)
            print(f"{name} вышел из комнаты.")


async def person(name, room):
    # Человек (задача) пытается использовать комнату
    print(f"{name} хочет войти в комнату.")
    await room.use(name)


async def main():
    room = Room()  # Инициализация комнаты с замком

    print("---------- Mutex - context manager \"with\" ----------")
    # Создание задач для нескольких людей, пытающихся войти в комнату
    await asyncio.gather(
        person("Алексей", room),
        person("Мария", room),
        person("Иван", room)
    )

asyncio.run(main())


# Task 1
async def task(lock, name):
    print(f"{name} пытается захватить мьютекс.")
    async with lock:
        print(f"{name} начал выполнение.")
        await asyncio.sleep(1)
    print(f"{name} завершил выполнение.")


async def main():
    lock = asyncio.Lock()
    tasks = [task(lock, f"Task {i}") for i in range(1, 4)]
    await asyncio.gather(*tasks)

asyncio.run(main())


# Task 2 - Mutex и try/finally
async def task(lock, name):
    try:
        await lock.acquire()
        print(f"{name} захватил мьютекс.")
        await asyncio.sleep(1)
        if name == "Task 1":
            raise Exception("Ошибка в задаче 1")
    finally:
        lock.release()
        print(f"{name} освободил мьютекс.")


async def main():
    lock = asyncio.Lock()
    await asyncio.gather(task(lock, "Task 1"), task(lock, "Task 2"), return_exceptions=True)

asyncio.run(main())

