"""
Задание 1.
Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python
На каждый скрипт нужно два решения - исходное и оптимизированное.
Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler
Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler
Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.
ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.
Это файл для четвертого скрипта
"""
"""Использование кортежей"""
"""task_2_v2 in Homework_5"""
"""Вывод: В данном скрипте для оптимизации использовались кортежи 
это привело к небольшому сокрашению используемой памяти """


from collections import defaultdict
from pympler import asizeof


"""Версия из task_2_v2 in Homework_5"""


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


"""Оптимизированная версия"""


class Calculate2:
    def __init__(self, num1):
        self.number1 = (num1, list(num1))

    def __str__(self):
        return str(self.number1[1])

    def __add__(self, other):
        num1 = self.number1[0]
        num2 = other.number1[0]
        return list(hex(int(num1, 16) + int(num2, 16))[2:].upper())

    def __mul__(self, other):
        num1 = self.number1[0]
        num2 = other.number1[0]
        return list(hex(int(num1, 16) * int(num2, 16))[2:].upper())


a = Calculate('A2')
b = Calculate2('A2')


print(asizeof.asizeof(a))
print(asizeof.asizeof(b))
