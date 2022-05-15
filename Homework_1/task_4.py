"""
Задание 4.
Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.
Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.
Приложение должно давать ответы на эти вопросы
 и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, применить словарь.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


def autetnification(login, password):
    """Сложность: O(n)"""
    database = {'petro132': ['nfthgfg', False],                      # O(1)
                'poil': ['uikiioi', True],
                'patrik434': ['hghgfg', False],
                'limon334': ['ftghtgh', False],
                'dominik': ['nfthgfg', True]
                }

    if login not in database.keys():                                 # O(n)
        print('Извините, такой учетной записи не существует')        # O(1)
    elif database[login][0] != password:                             # O(1)
        print('Извените вы ввели неверный пароль')                   # O(1)
    elif not database[login][1]:                                     # O(n)
        error = input('Ваша учетная запись не активирована, '        # O(1)
                      'хотите пройти активацию (y/n)? ')
        if error == 'y':                                             # O(1)
            print('Вы успешно активировали свою учетную запись')     # O(1)
            database[login][1] = True                                # O(1)
        else:                                                        # O(1)
            print('Очень жаль, попробуйте в другой раз')             # O(1)
    else:                                                            # O(1)
        print('Вход выполнен успешно')                               # O(1)


def autetnification2(login, password):
    """Сложность: O(n^3)"""
    logins = ['petro132', 'poil', 'patrik434', 'limon334', 'dominik']                       # O(1)
    passwords = ['fgfg', 'yujghnyg', 'fhnyumy', 'fgbty', 'oiioyu']                          # O(1)
    activations = [True, False, True, True, False]                                          # O(1)

    if login not in logins:                                                                 # O(n)
        print('Такой учетной записи не существует')                                         # O(1)
    else:                                                                                   # O(1)
        for i in range(len(logins)):                                                        # O(n)
            for k in range(len(passwords)):                                                 # O(n)
                for m in range(len(activations)):                                           # O(n)
                    if i == k and k == m:                                                   # O(n)
                        if passwords[i] == password and logins[i] == login:                 # O(1)
                            if activations[i]:                                              # O(1)
                                print('Вам доступ разрешен')                                # O(1)
                                break                                                       # O(1)
                            else:                                                           # O(1)
                                error = input('У вас не пройдена активация,'                # O(1)
                                              'желаете её пройти?(y/n): ')
                                if error == 'y':                                            # O(1)
                                    print('Вы успешно активировали свою учетную запись')    # O(1)
                                    activations[i] = True                                   # O(1)
                        break                                                               # O(1)
""" Второй вариант намного вложнее предыдущего так как двойная вложенность циклов,
и сложность в худшем случае всего алгоритма выше: количество операций- 2го О(n^3)> O(n)
 """

if __name__ == "__main__":
    # autetnification('petro132', 'nfthgfg')
    autetnification2('petro132', 'fgfg')
