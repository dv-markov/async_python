import asyncio


# Task 1 - если задача создана, и ее не запустить явно, она начнет выполняться при ближайшем await
async def my_task():
    print("Task started")
    await asyncio.sleep(1)
    print("Task finished")


async def main():
    asyncio.create_task(my_task())
    await asyncio.sleep(2)

asyncio.run(main())


# Task 2 - await возвращает None
async def example_task():
    print("Задача выполнена")


async def main():
    task = asyncio.create_task(example_task())
    return await task

print(asyncio.run(main()))


# Task 3
async def coro_1():
    print("Coroutine 1 is done")


async def coro_2():
    print("Coroutine 2 is done")


async def coro_3():
    print("Coroutine 3 is done")


# Вызов функции по имени / call function by a string name
# Через eval()
async def main():
    tasks = [asyncio.create_task(eval("coro_" + str(x) + "()")) for x in range(1, 4)]
    await asyncio.gather(*tasks)


# Version 2
# Вызов функции по имени / call function by a string name
# Через globals()
# async def main():
#     for num in range(1, 4):
#         method_name = f'coro_{num}'
#         method = globals().get(method_name)
#         await asyncio.create_task(method())

asyncio.run(main())
print(globals())


# Task 4
async def print_with_delay(nr):
    await asyncio.sleep(1)
    print(f"Coroutine {nr} is done")


async def main():
    tasks = [asyncio.create_task(print_with_delay(x)) for x in range(10)]
    for task in tasks:
        await task

    # Вариант Хошева - ожидание выполнения каждой задачи
    # Задержка 1 сек после каждого вывода - отстой
    # [await asyncio.create_task(print_with_delay(x)) for x in range(10)]

asyncio.run(main())


# Task 5 - Async counters
max_counts = {
    "Counter 1": 13,
    "Counter 2": 7
}

counters = {
    "Counter 1": 0,
    "Counter 2": 0,
}

# print(list(counters)[0])
#
# for key in counters:
#     print(key)


async def counter(counter_name, delay):
    max_counter_value = max_counts[counter_name]
    while counters[counter_name] < max_counter_value:
        counters[counter_name] += 1
        await asyncio.sleep(delay)
        print(f"{counter_name}: {counters[counter_name]}")


async def main():
    tasks = [asyncio.create_task(counter(c_name, 0.1)) for c_name in counters]
    await asyncio.gather(*tasks)

asyncio.run(main())


# Task 6 - Advanced counters
max_counts = {
    "Counter 1": 13,
    "Counter 2": 7,
    "Counter 3": 15,
}

delays = {
    "Counter 1": 1,
    "Counter 2": 2,
    "Counter 3": 0.5,
}

counters = {
    "Counter 1": 0,
    "Counter 2": 0,
    "Counter 3": 0,
}


async def counter(counter_name, delay):
    while counters[counter_name] < max_counts[counter_name]:
        counters[counter_name] += 1
        await asyncio.sleep(delay)
        print(f"{counter_name}: {counters[counter_name]}")


async def main():
    tasks = [asyncio.create_task(counter(c_name, delays[c_name])) for c_name in counters]
    await asyncio.gather(*tasks)

asyncio.run(main())



