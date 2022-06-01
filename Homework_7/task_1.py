"""
Задание 1.
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
Обязательно доработайте алгоритм (сделайте его умнее)!
Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.
Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.





Вывод: Идея доработки была в том, что бы поставить флаг в значение False,
если за всю итерацию цикла for не произошло ни одной замены.

Это принесло свои плоды но лишь процентов на 15-20.
Например в списке [3, 4, 2, 1] произошла бы всего одна замена  (3<>4) [4, 3, 2, 1]
и последующая итерация замершилась бы с флагом False и цикл while прервется с количеством
итераций 2n.
Тогда как первый вариант выполнялся бы n*n операций.
"""

from timeit import timeit
from random import randint


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_v2(lst_obj):
    flag = True
    while flag:
        flag = False
        for i in range(len(lst_obj)-1):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                flag = True
    return lst_obj


orig_list = [randint(-100, 100) for _ in range(100)]
print(orig_list)
print(f'Первый вариант сортировки: {bubble_sort(orig_list[:])}')
print(f'Первый вариант сортировки: {bubble_sort_v2(orig_list[:])}')
print('Первая сортировка заняла время:')
print(timeit("bubble_sort(orig_list[:])", globals=globals(), number=10))
print(timeit("bubble_sort(orig_list[:])", globals=globals(), number=100))
print(timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000))
print('Вторая сортировка заняла время:')
print(timeit("bubble_sort_v2(orig_list[:])", globals=globals(), number=10))
print(timeit("bubble_sort_v2(orig_list[:])", globals=globals(), number=100))
print(timeit("bubble_sort_v2(orig_list[:])", globals=globals(), number=1000))
