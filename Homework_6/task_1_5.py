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
Это файл для пятого скрипта
"""

"""Использование filter"""
"""task_1 in Homework_4"""
"""Вывод: В данном скрипте для оптимизации использовался filter  
это привело к сокрашению памяти в 6 раз"""

from pympler.asizeof import asizeof

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

"""Версия из task_1 in Homework_4"""


def func(nums):
    new_arr = [i for i in range(len(nums)) if not nums[i] % 2]
    return new_arr


"""Оптимизированная версия"""


def func_2(nums):
    new_list = filter(lambda x: nums[x] % 2 == 0, range(len(nums)))
    return new_list


result1 = func(my_list)
result2 = func_2(my_list)
print(asizeof(result1))
print(asizeof(result2))