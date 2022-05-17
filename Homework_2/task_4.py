"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""


def my_function(user_number, start_num=1, result_sum=0):
    if user_number == 0:
        return result_sum
    else:
        user_number -= 1
        result_sum += start_num
        start_num /= -2
        return my_function(user_number, start_num, result_sum)


if __name__ == "__main__":
    try:
        user_num = int(input("Введите натуральное число: "))
        print(f"Сумма n элементов следующего ряда чисел:\n1-0.5 0.25 -0.125 ... n равна:"
              f" {my_function(user_num)}")
    except ValueError:
        print("Вы вместо числа ввели строку. Исправьтесь")
