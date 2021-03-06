import random
import numpy as np
# ВАРИАНТ 1

#ЗАДАНИЕ 4
# Написать функцию, которая генерирует несколько массивов случайных чисел и возвращает тот,
# в ко-тором сумма элементов наибольшая. Для генерации случайных чисел используйте функцию random 
# из модуля random. Модуль random необходимо предварительно подключить с помощью команды import random.
# Для вычисления суммы элементов массива используйте встроенную функцию sum. 
# Функция принимает 2 параметра: количество генерируемых массивов и количество элементов в мас-сиве, 
# и возвращает массив с наибольшей суммой элементов.

print("\nЗАДАНИЕ 4")

def arrayWithMaxElementsSum(*arrays):
	return arrays[max(enumerate(arrays), key=lambda pair: sum(pair[1]))[0]]

n = input("Кол-во массивов: ")
len = input("Кол-во элементов: ")
arrays = np.random.randint(0, 10, size = (int(n), int(len)))
print(arrays)
print()
print(arrayWithMaxElementsSum(*arrays))

#ЗАДАНИЕ 8
# Написать функцию, которая получает 3-значное число и возвращает строку, 
# содержащее это число, описанное словами. Например, для числа 195 функция
# должна выдать строку «сто девяносто пять». Функция должна корректно отрабатывать 
# ситуацию, когда вводят 2-значные числа и цифры или когда в позиции десятков и единиц нули, 
# например, 101, 220. Ситуацию, когда в числе количество десятков равно 1, например, 218, 
# обрабатывать не нужно.

print("\nЗАДАНИЕ 8")

hund = {0: '', 1: 'сто', 2: 'двести', 3: 'триста', 4: 'четыреста',
 5: 'пятьсот', 6: 'шестьсот', 7: 'семьсот', 8: 'восемьсот', 9: 'девятьсот'}

dec = {0: '', 1: 'десять', 2: 'двадцать', 3: 'тридцать', 4: 'сорок',
 5: 'пятьдесят', 6: 'шестьдесят', 7: 'семьдесят', 8: 'восемьдесят', 9: 'девяносто'}

one = {0: '', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре',
 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}

def wordNum(number):
    h = number[0]
    d = number[1]
    o = number[2]
    return ('%s %s %s' % (hund[int(h)], dec[int(d)], one[int(o)]))

number = list(''.join(input('Введите число: ')))
print(wordNum(number))




# ЗАДАНИЕ 9
# Написать функцию, проверяющую у пользователя знание таблицы умножения. 
# Функция спрашивает у пользователя два целых числа, а затем спрашивает 
# результат их перемножения. Если пользователь ответил верно, 
# функция должна напечатать слово «Верно», иначе «Ошибка. 
# Верный ответ <число>». Для ввода значений используйте встроенную функцию input, 
# для преобразования строки к целому числу – функцию int.

print("\nЗАДАНИЕ 9")

def multiplyCheck():
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    c = input("Введите результат перемножения: ")
    res = int(a) * int(b)
    if res == int(c):
        print("ВЕРНО")
    if res != int(c):
        print("ОШИБКА!, Верный ответ: ", res)


multiplyCheck()