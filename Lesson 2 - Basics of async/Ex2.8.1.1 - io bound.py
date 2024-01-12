# # 1 Чтение и запись файлов
# Чтение файла
with open('file.txt', 'r') as f:
    data = f.read()
    print(data)

# Запись в файл
with open('file.txt', 'w') as f:
    f.write('Hello, World!')

# Чтение файла
with open('file.txt', 'r') as f:
    data = f.read()
    print(data)

# # 2 Сетевые операции, взаимодействие с API
import requests

# Отправка GET запроса
response1 = requests.get('http://www.python.org')
print(response1)

# Отправка POST запроса
response2 = requests.post('http://www.python.org', data={'hello': 'world'})
print(response2)

# # 3 Взаимодействие с пользователем
# # Чтение ввода с клавиатуры
# name = input('Введите ваше имя: ')
#
# # Вывод информации на экран
# print(f'Привет, {name}!')

# # 4 Взаимодействие с операционной системой
import os
from pprint import pprint

# Получение списка файлов в директории
files = os.listdir('./')
pprint(files)

# Запуск системной команды
os.system('ls -l')

# # 5 Взаимодействие с базами данных
import sqlite3

# Подключение к базе данных
con = sqlite3.connect('example.db')

# Создание курсора
cur = con.cursor()

# cur.execute("CREATE TABLE lang(name, first_appeared)")
# cur.execute("INSERT INTO lang VALUES (?, ?)", ("C", 1972))
con.commit()

# Выполнение SQL-запроса
res = cur.execute("select * from lang")
output = res.fetchall()

print(output)
con.close()

# # 6 Взаимодействие с внешними устройствами
# import serial
#
# # Открытие последовательного порта
# ser = serial.Serial('/dev/ttyUSB0')
#
# # Чтение данных из порта
# data = ser.read(100)


# # 7 Взаимодействие с веб-браузером
from selenium import webdriver

# Открытие веб-браузера
driver = webdriver.Firefox()

# Переход на веб-сайт
driver.get('http://www.python.org')
