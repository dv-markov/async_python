import asyncio
import random


async def main():
    print('Начинаем')
    await asyncio.sleep(1)  # приостановка выполнения на 1 секунду
    print('Закончили')

# Запускаем асинхронную функцию
asyncio.run(main())


# Несколько асинхронных функций
# Асинхронная функция, имитирующая чтение данных из файла
async def read_data_from_file(filename):
    print(f"Начинаем чтение из файла {filename}")

    # Имитация задержки для чтения файла
    await asyncio.sleep(2)  # Предположим, чтение занимает 2 секунды
    print(f"Чтение из файла {filename} завершено")
    return f"данные из {filename}"


# Асинхронная функция, имитирующая отправку данных в интернет
async def send_data_to_internet(data):
    print("Начинаем отправку данных в интернет")

    # Имитация задержки для отправки данных
    await asyncio.sleep(3)  # Предположим, отправка занимает 3 секунды
    print("Отправка данных в интернет завершена")


# Главная асинхронная функция, которая управляет выполнением программы
async def main():
    filename = "example.txt"

    # Чтение данных из файла
    file_data = await read_data_from_file(filename)

    # Отправка прочитанных данных в интернет
    await send_data_to_internet(file_data)


# Запуск асинхронной программы
asyncio.run(main())


async def boil_water(time: int):
    print('Ставим чайник с водой на плиту...')
    await asyncio.sleep(time)                               # Передаем управление плите
    print('Чайник закипел!')


async def chop_vegetables():
    print('Начинаем нарезать овощи...')
    await asyncio.sleep(random.randint(2, 4))               # Передаем управление нарезке овощей
    print('Овощи нарезаны!')


async def prepare_dinner():
    await asyncio.gather(boil_water(5), chop_vegetables())   # Запускаем задачи параллельно


asyncio.run(prepare_dinner())
