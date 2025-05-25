# Площа прямокутника
# Умова:
# Створи функцію rectangle_area(width, height), яка обчислює площу прямокутника за формулою:
# S = ширина × висота
from domain.part4.loops_task import total


def rect_area(width, height):
    area = width * height
    # print(area)
    return area


# Середнє арифметичне трьох чисел
# Умова:
# Створи функцію average(a, b, c), яка повертає середнє арифметичне.
#
# Формула:
# (a + b + c) / 3

def average(a, b, c):
    return (a + b + c) / 3


def average_variative(*args):
    total = 0
    for arg in args:
        total = total + arg

    counter = len(args)
    return total / counter


average_variative(10, 20, 30, 40, 50, 100, 200)


# Периметр трикутника
# Умова:
# Створи функцію triangle_perimeter(a, b, c), яка обчислює периметр трикутника.
#
# Формула:
# P = a + b + c

def triangle_perimeter(a, b, c):
    return a + b + c


#  Створи функцію, яка приймає список чисел і повертає їхню суму.
# Наприклад, для [1, 2, 3] має повернути 6.

def suma(list_number):
    total = 0
    for number in list_number:
        total = total + number
    return total


# Створи функцію, яка приймає список слів і повертає кількість слів, довших за 5 символів.
# Наприклад, для ['яблуко', 'груша', 'банан', 'кіт'] має повернути 2.

def counter_words_longer_than_5(words):
    counter = 0

    for word in words:
        if len(word) > 5:
            counter = counter + 1

    return counter


print(counter_words_longer_than_5(['яблуко', 'груша', 'банан', 'кіт']))


# Створи функцію, яка приймає список чисел і повертає новий список лише з парних чисел.
# Наприклад, для [1, 4, 5, 8] має повернути [4, 8].

def filter_numbers(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)

    return  result
print(filter_numbers([1, 2, 3, 4, 5,6,66,777]))
