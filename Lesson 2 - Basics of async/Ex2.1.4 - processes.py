# Процессы

# import time
# import os
#
# print(f'Программа запущена в процессе PID {os.getpid()}')
# print('Программа спит')
# time.sleep(20)
# print('Программа завершена')


# Для создания процессов используем модуль multiprocessing
import os
from multiprocessing import Process
import time

# Глобальная переменная-счетчик
counter = 0


# Функция, экземпляры которой будут запускаться в созданных процессах.
def fn(n):
    global counter
    print(f'fn {n} запущена в PID {os.getpid()}')
    time.sleep(2)
    # Изменяем значение счетчика
    counter += 1
    # Печатаем его значение
    print(f'fn #{n} PID: {os.getpid()} {counter=}')


if __name__ == '__main__':
    procs = []
    start = time.time()
    # Печатаем PID основного процесса.
    print(f'PID основного процесса: {os.getpid()}')
    # Создаем три процесса
    for i in range(1, 4):
        process = Process(target=fn, args=(i,))
        procs.append(process)
        process.start()
    # Ожидание завершения всех процессов.
    # Вариант, когда основной поток завершится последним.
    # Чтобы отследить изменение counter и измерить общее время.
# --- Разблокировать для варианта 2 -----
    for proc in procs:
        proc.join()
    # Выводим сообщение о завершении основной программы
    print(f'Программа в PID {os.getpid()} завершена')
    print(f'{counter=}, time = {time.time() - start}')

