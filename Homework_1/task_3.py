"""
Задание 3.
Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


def three_max_profits(my_dict):
    """
    1 Вариант. Сложность: O(n^2)
    """

    while len(my_dict) > 3:                  # O(1)
        for k, v in my_dict.items():         # O(n)
            if v == min(my_dict.values()):   # O(n)
                del my_dict[k]               # O(1)
                break                        # O(1)
    print(my_dict)                           # O(n)


def three_max_profits2(my_dict):
    """
    2 вариант. Сложность: O(n)
    """
    names = list(my_dict.keys())            # O(n)
    profits = list(my_dict.values())        # O(n)
    i = 0                                   # O(1)
    while i != 3:                           # O(1)
        idx = profits.index(max(profits))   # O(n)
        print(names[idx], profits[idx])     # O(1)
        names.pop(idx)                      # O(n)
        profits.pop(idx)                    # O(n)
        i += 1                              # O(1)
"""Первый вариант будет более долгим так как есть вложенный цикл.
PS я не уверен"""

if __name__ == "__main__":
    companies = {'Adidas': 3400,
                 'Nike': 2600,
                 'Asus': 4500,
                 'BENQ': 5600,
                 'Redmi': 4300
                 }
    print(len(companies))
    # three_max_profits(companies)
    three_max_profits2(companies)
