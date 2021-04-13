import random
# ВАРИАНТ 1

#ЗАДАНИЕ 4
print("\nЗАДАНИЕ 4")
def checkMax(n, len):
    max = 0
    arraym = [0]
    for k in range(n):
        array = [0]*len
        for i in range(len):
            array[i] = random.randint(0, 20)
        print("МАССИВ " + str(k + 1) + ": ", array, "СУММА ЭЛЕМЕНТОВ: ", sum(array))
        if sum(array) > max:
            max = sum(array)
            arraymax = array

    print("\nМАССИВ С НАИБОЛЬШЕЙ СУММОЙ ЭЛЕМЕНТОВ: ", arraymax, "СУММА ЭЛЕМЕНТОВ: " + str(max))


res = checkMax(5, 10)




#ЗАДАНИЕ 8
print("\nЗАДАНИЕ 8")

hund = {0: '', 1: 'сто', 2: 'двести', 3: 'триста', 4: 'четыреста',
 5: 'пятьсот', 6: 'шестьсот', 7: 'семьсот', 8: 'восемьсот', 9: 'девятьсот'}

dec = {0: '', 1: 'десять', 2: 'двадцать', 3: 'тридцать', 4: 'сорок',
 5: 'пятьдесят', 6: 'шестьдесят', 7: 'семьдесят', 8: 'восемьдесят', 9: 'девяносто'}

one = {0: '', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре',
 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}

def wordNum():
    number = list(''.join(input('Введите число: ')))

    h = number[0]
    d = number[1]
    o = number[2]

    print('%s %s %s' % (hund[int(h)], dec[int(d)], one[int(o)]))

wordNum()




# ЗАДАНИЕ 9
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