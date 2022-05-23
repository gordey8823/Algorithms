"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры
ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
from timeit import timeit


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return


def func_2(nums):
    new_arr2 = [i for i in range(len(nums)) if not nums[i] % 2]
    return new_arr2


print(timeit('func_1(my_list)', globals=globals(), number=100000))
print(timeit('func_2(my_list)', globals=globals(), number=100000))


"""Вторая функция оказалась более производительной
так как list comprehension быстрее циклов for которых они заменяют"""
