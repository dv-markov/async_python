import asyncio
import aiohttp


# Ожидание завершения выполнения одной операции
async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    data = await fetch_data('http://python.org')
    print(data[:15])

asyncio.run(main())


# Ожидание завершения выполнения нескольких операций
async def cook_pasta():
    print("Начинаем готовить пасту")
    await asyncio.sleep(5)
    print("Паста готова")


async def cook_sauce():
    print("Начинаем готовить соус")
    await asyncio.sleep(3)
    print("Соус "
          "готов")


async def main():
    # Используем asyncio.gather для запуска двух корутин одновременно и ожидания их завершения.
    # Await приостанавливает выполнение функции до тех пор, пока не будут завершены обе корутины
    await asyncio.gather(cook_pasta(), cook_sauce())


asyncio.run(main())
