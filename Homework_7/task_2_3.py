"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
3) с помощью встроенной функции поиска медианы
сделайте замеры на массивах длиной 10, 100, 1000 элементов
В конце сделайте аналитику какой из трех способов оказался эффективнее

1 способ:
0.0015571000003546942
0.11782659999880707
14.12340580000091

2 способ:
0.0003391999998711981
0.010895399998844368
0.9133199000007153

3 способ:
0.002691799998501665
0.003590000000258442
0.013267599999380764

Вывод: Самым медленным оказался 1 способ- поиск с помощью гномьей сортировки.
На небольшом массиве более быстрым был 2 способ- удаление максимального и
минимального элементов покак не останется медиана.
И наконец, на бОльших массивах лучшее время показал поиск с помощью библиотеки numpy.median
"""
from random import randint
from timeit import timeit
from numpy import median


def search_median(lst):
    return median(lst)


orig_list = [randint(-100, 100) for _ in range(11)]
print(timeit("search_median(orig_list[:])", globals=globals(), number=100))
orig_list2 = [randint(-100, 100) for _ in range(101)]
print(timeit("search_median(orig_list2[:])", globals=globals(), number=100))
orig_list3 = [randint(-100, 100) for _ in range(1001)]
print(timeit("search_median(orig_list3[:])", globals=globals(), number=100))