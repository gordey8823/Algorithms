"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list
Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее
2) сравнить операции
append left, popleft, extend left дека и соответствующих им операций списка
и сделать выводы что и где быстрее
3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее
Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""
from collections import deque
from timeit import timeit


print("""
1) сравнить операции append, pop, extend списка и дека

метод append , extend и у списков и у деков работает примерно с одинаковым временем 
метод pop в деке работает медленнее

2) сравнить операции append left, popleft, extend left дека 

По операциям добавления и удаления в начале списка и дека во всем с большим отрывом
выигрывает дек

3) сравнить операции получения элемента списка и дека

Получение случайных елементов быстрее у списка
""")


print('-' * 80)


my_list = [i for i in range(10 ** 6)]
my_deque = deque([i for i in range(10 ** 6)])

"""метод append__________________________________________________________________"""


def append_list():
    for i in range(10 ** 5):
        my_list.append(i)


def append_deque():
    for i in range(10 ** 5):
        my_deque.append(i)


# print(timeit('append_list()', globals=globals(), number=100))
# print(timeit('append_deque()', globals=globals(), number=100))
# 0.7112807999999404
# 0.7131757999998172
"""метод pop_____________________________________________________________________"""


def pop_list(list1):
    for _ in range(10 ** 4):
        list1.pop()


def pop_deque(deque1):
    for _ in range(10 ** 4):
        deque1.pop()


# print(timeit('pop_list(my_list.copy())', globals=globals(), number=100))
# print(timeit('pop_deque(my_deque.copy())', globals=globals(), number=100))
# 0.955934999999954
# 1.9041287000000011
"""метод extend__________________________________________________________________"""


def extend_list():
    for _ in range(1000):
        my_list.extend([1, 2, 3, 4])


def extend_deque():
    for _ in range(1000):
        my_deque.extend([1, 2, 3, 4])


# print(timeit('extend_list()', globals=globals(), number=100))
# print(timeit('extend_deque()', globals=globals(), number=100))
# 0.01697879999937868
# 0.016098600000077568
"""метод appendleft______________________________________________________________"""


def appendleft_list():
    for i in range(10 ** 4):
        my_list.insert(0, i)


def appendleft_deque():
    for i in range(10 ** 4):
        my_deque.appendleft(i)


# print(timeit('appendleft_list()', globals=globals(), number=10))
# print(timeit('appendleft_deque()', globals=globals(), number=10))
# 64.28948740000033
# 0.0067139000002498506
"""метод popleft_________________________________________________________________"""


def popleft_list(list1):
    for i in range(10 ** 3):
        list1.pop(0)


def popleft_deque(deque1):
    for i in range(10 ** 3):
        deque1.popleft()


# print(timeit('popleft_list(my_list.copy())', globals=globals(), number=10))
# print(timeit('popleft_deque(my_deque.copy())', globals=globals(), number=10))
# 10.89663550000023
# 0.18212669999957143
"""метод extendleft______________________________________________________________"""


def extendleft_list(list1):
    for i in range(10 ** 3):
        list1.insert(0, [1, 2, 3, 4])


def extendleft_deque(deque1):
    for i in range(10 ** 3):
        deque1.extendleft([1, 2, 3, 4])


# print(timeit('extendleft_list(my_list.copy())', globals=globals(), number=10))
# print(timeit('extendleft_deque(my_deque.copy())', globals=globals(), number=10))
# 5.30686390000028
# 0.1881444000000556
"""Получение элементов___________________________________________________________"""


def chek_list():
    for i in range(100, 1000):
        my_list[i] = i


def chek_deque():
    for i in range(100, 1000):
        my_deque[i] = i


print(timeit('chek_list()', globals=globals(), number=10000))
print(timeit('chek_deque()', globals=globals(), number=10000))
