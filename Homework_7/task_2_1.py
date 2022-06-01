"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)
сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randint
from timeit import timeit


def search_median(lst):
    i = 1
    while i < len(lst):
        if lst[i - 1] <= lst[i]:
            i += 1
        else:
            tmp = lst[i]
            lst[i] = lst[i - 1]
            lst[i - 1] = tmp
            i -= 1
            if i == 0:
                i = 1
    return lst[len(lst)//2]


orig_list = [randint(-100, 100) for _ in range(11)]
print(timeit("search_median(orig_list[:])", globals=globals(), number=100))
orig_list2 = [randint(-100, 100) for _ in range(101)]
print(timeit("search_median(orig_list2[:])", globals=globals(), number=100))
orig_list3 = [randint(-100, 100) for _ in range(1001)]
print(timeit("search_median(orig_list3[:])", globals=globals(), number=100))

