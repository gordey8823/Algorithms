"""
Задание 2.
Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.
Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.
Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
"""Вывод: Профилирование рекурсии удобно выполнять когда она находится 
внутри другой функции"""

from memory_profiler import profile


@profile()
def recursion(n):
    def my_function(user_number, start_num=1, result_sum=0):
        if user_number == 0:
            return result_sum
        else:
            user_number -= 1
            result_sum += start_num
            start_num /= -2
            return my_function(user_number, start_num, result_sum)
    return my_function(n)


print(recursion(12))


@profile()
def recursion2(n):
    def reversed_number(user_number, reverse_num=''):
        if user_number == 0:
            return reverse_num
        else:
            reverse_num += str(user_number % 10)
            user_number = user_number // 10
            return reversed_number(user_number, reverse_num)
    return reversed_number(n)


print(recursion2(1234))
