"""
Задание 2.
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections
default-dict(list)
int(, 16)
reduce
2) через ООП
вспомните про перегрузку методов
__mul__
__add__
"""
from collections import defaultdict


class Calculate:
    def __init__(self, num1):
        self.number1 = defaultdict(list)
        self.number1[num1] = list(num1)

    def __str__(self):
        return str(list(self.number1.values())[0])

    def __add__(self, other):
        num1 = list(self.number1.keys())[0]
        num2 = list(other.number1.keys())[0]
        return list(hex(int(num1, 16) + int(num2, 16))[2:].upper())

    def __mul__(self, other):
        num1 = list(self.number1.keys())[0]
        num2 = list(other.number1.keys())[0]
        return list(hex(int(num1, 16) * int(num2, 16))[2:].upper())


a = Calculate(input('Введите первое число: '))
b = Calculate(input('Введите первое число: '))

print(f"""Вы ввели 2 числа: {a} и {b}
их сумма равна {a + b}
a произведение {a * b}""")
