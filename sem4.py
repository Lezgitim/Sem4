# Задача 1. Задайте натуральное число N. Напишите программу, которая составит список
# простых множителей числа N. 60 -> 2, 2, 3, 5

def Prost_mnozh():
    n = int(input('Введите число: '))
    list = []

    if n <= 0:
        print('Вы ввели не натуральное число!')
        exit()

    for i in range(2, n):
        while n % i == 0:
            n = n//i
            list.append(i)
    print(list)


# Задача 2. В первой строке файла находится информация об ассортименте мороженного,
# во второй - информация о том, какое мороженное есть на складе.
# Выведите названия того товара, который закончился.
# 1. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2. «Сливочное», «Вафелька», «Сладкоежка»
# Закончилось: «Бурёнка»

def Morozhennoe():
    with open('morozhennoe.txt', 'r', encoding='utf-8') as data:
        num = data.readlines()

    a = num[0].split()
    b = num[1].split()

    for i in range(len(a)):
        Kount = b.count(a[i])
        if Kount == 0:
            v = (a[i])
            print('Закончилось:', v[:-1])


# Задача 3. Выведите число π с заданной точностью.
# Точность вводится пользователем в виде натурального числа.3 -> 3.142
# 5 -> 3.14159

def Pi():
    import math
    n = int(input('Задайте точнсть Пи: '))
    print(round(math.pi, n))


# Задача 4*. Даны два файла, в каждом из которых находится запись многочлена.
# Найдите сумму данных многочленов.
# 1. 5x^2 + 3x2. 3x^2 + x + 8Результат: 8x^2 + 4x + 8

def sum():
    with open('1.txt', 'r', encoding='utf-8') as data:
        num = data.read()

    with open('2.txt', 'r', encoding='utf-8') as data:
        num1 = data.read()

    a = int(num[0])
    b = int(num1[0])
    c = int(num[5])
    d = int(num1[5])
    f = int(num[8])
    g = int(num1[8])

    a = a+b
    b = c+d
    c = -f+g

    print(num)
    print(num1)
    print(a,'x^2+', b, 'x', c, sep='')
