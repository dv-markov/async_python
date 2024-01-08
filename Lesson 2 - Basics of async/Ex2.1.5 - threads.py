# Threads

import time
import threading
from threading import Thread
import os


# IO-bound операции
def io_func():
    """Функция имитирует выполнение I/O операции"""
    # Выводим идентификатор потока и PID процесса в котором этот поток существует.
    print(f'Это поток {threading.get_ident()} из процесса {os.getpid()}')
    # Имитация долгой I/O операции.
    time.sleep(1)


# --------------1 вариант последовательная обработка---------------------------------
start = time.time()
io_func()
io_func()
io_func()
print(f'Всего затрачено времени: {time.time() - start}')


# --------------2 вариант используем потоки---------------------------------
# Создание объектов Thread очень похоже на создание Process.
start = time.time()
threads = [Thread(target=io_func) for _ in range(3)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(f'Всего затрачено времени: {time.time() - start}')


# CPU-bound операции
def cpu_func(n):
    """Функция выполняняет CPU bound операцию"""
    start = time.time()
    # Выводим номер потока и номер процесса в котором этот поток существует.
    print(f'Вычисление {n} в потоке {threading.get_ident()} из процесса {os.getpid()}')
    # Вычисления.
    res = sum(a**a for a in range(5000))
    # Время вычислений индивидуально для каждой машины, смотрим сколько t уйдет на одну функцию.
    print(f'Вычисление {n} завершено за {time.time() - start}')


# --------------1 вариант последовательная обработка---------------------------------
start = time.time()
cpu_func(1)
cpu_func(2)
cpu_func(3)
print(f'Всего затрачено времени: {time.time() - start}')


def cpu_func2():
    """Функция выполняняет CPU bound операцию"""
    start = time.time()
    # Выводим номер потока и номер процесса в котором этот поток существует.
    print(f'Вычисление в потоке {threading.get_ident()} из процесса {os.getpid()}')
    # Вычисления.
    res = sum(a**a for a in range(5000))
    # Время вычислений индивидуально для каждой машины, смотрим сколько t уйдет на одну функцию.
    print(f'Вычисление в потоке {threading.get_ident()} завершено за {time.time() - start}')


# --------------2 вариант используем потоки---------------------------------
# Создание объектов Thread очень похоже на создание Process.
start = time.time()
threads = [Thread(target=cpu_func2) for _ in range(3)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(f'Всего затрачено времени: {time.time() - start}')
