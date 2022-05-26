"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях




Сравнение:____________________________________________________________________
В ряде вычислений выявлено, что Orderdict уступает обычному словарю,
но если нужна сторогость в очередности елементов(например- сравнение словарей),
то Orderdict имеет смысл использовать, в остальном не имеет смысла
"""


from collections import OrderedDict
from timeit import timeit


d1 = dict()
d2 = dict()
od1 = OrderedDict()
od2 = OrderedDict()
"""add__________________________________________________________________________"""


def add_dict(my_dict: dict, rev=1):
    """
    :param
    If rev= '-1' - dict add= revers
    """
    start = 1
    stop = 10 ** 5
    if rev == 1:
        for i in range(start, stop):
            my_dict[i] = i
    else:
        for i in range(stop - 1, start - 1, -1):
            my_dict[i] = i


def add_orderdikt(my_orderdict: dict, rev=1):
    """
    :param
    If rev='-1' - orderdict add=revers
    """
    start = 1
    stop = 10 ** 5
    if rev == 1:
        for i in range(start, stop):
            my_orderdict[i] = i
    else:
        for i in range(stop - 1, start - 1, -1):
            my_orderdict[i] = i


# print(timeit('add_dict(d1)', globals=globals(), number=100))
# print(timeit('add_orderdikt(od1)', globals=globals(), number=100))
# 0.7144829999997455
# 0.9290627999998833
"""Очевидно OrderedDict Заполняется на 10-15% медленнее обычного словаря"""

add_dict(d1)
add_dict(d2, rev=-1)
add_orderdikt(od1)
add_orderdikt(od2, rev=-1)

"""Перебор елементов____________________________________________________________"""


def check_dict(my_dict):
    for i in range(50, 10 ** 4):
        my_dict[i] += 1


def check_orderdict(my_orderdict):
    for i in range(50, 10 ** 4):
        my_orderdict[i] += 1


# print(timeit('check_dict(d1)', globals=globals(), number=1000))
# print(timeit('check_orderdict(od1)', globals=globals(), number=1000))
# 1.583699800001341
# 1.6343364999993355
"""В переборе и замене элементов словаря особых различий не выявлено"""

"""Удаление элементов___________________________________________________________"""


def del_dict(my_dikt):
    for i in range(1, 10 ** 4):
        del my_dikt[i]


def del_orderdict(my_orderdict):
    for i in range(1, 10 ** 4):
        del my_orderdict[i]


print(timeit('del_dict(d1.copy())', globals=globals(), number=100))
print(timeit('del_orderdict(od1.copy())', globals=globals(), number=100))
# 3.1421040999994148
# 16.263043299997662
"""Orderdict опять терпит поражение"""

print(d1 == d2)
print(od1 == od2)
