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
Это файл для первого скрипта
"""
"""Ленивые вычисления"""
"""task_1 in Homework_4"""
"""Вывод: В данном скрипте для оптимизации использовались ленивые вычисления 
это привело к значительному сокрашению памяти """

from memory_profiler import memory_usage
from random import randint


def decor(func):
    def wrapper(*args):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff

    return wrapper


my_list = [randint(1, 100) for i in range(1000)]

"""Версия из task_1 in Homework_4"""


@decor
def func(nums):
    new_arr = [i for i in range(len(nums)) if not nums[i] % 2]
    return new_arr


@decor
def func2(nums):
    for num in range(len(nums)):
        if my_list[num] % 2 == 0:
            yield num


my_generator, mem_diff = func(my_list)
print(f"Выполнение заняло {mem_diff} Mib")

my_generator2, mem_diff2 = func2(my_list)
print(f"Выполнение заняло {mem_diff2} Mib")