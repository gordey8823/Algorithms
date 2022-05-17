"""
Задание 6. На закрепление навыков работы с очередью
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Реализуйте класс-структуру "доска задач".
Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку
После реализации структуры, проверьте ее работу на различных сценариях
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


class QueueClass:
    def __init__(self):
        self.start_elems = []  # Список базовых задач
        self.mod_elems = []  # Список на доработку
        self.end_elems = []  # Решенный задачи

    def tasks_start(self):  # Список задач на доработку или в решенные
        return self.start_elems

    def tasks_mod(self):  # Список задач на доработке
        return self.mod_elems

    def tasks_end(self):  # Решенные задачи
        return self.end_elems

    def task_to_start(self, task):  # Заполняем задачи для решения
        self.start_elems.insert(0, task)

    def from_start_to_mod(self):  # Базовае задачи отправляем на доработку
        task = self.start_elems.pop()
        self.mod_elems.insert(0, task)

    def from_start_to_end(self):  # Базовае задачи отправляем в завершенные
        task = self.start_elems.pop()
        self.end_elems.insert(0, task)

    def from_mod_to_end(self):  # Базовае задачи отправляем на доработку
        task = self.mod_elems.pop()
        self.end_elems.insert(0, task)


if __name__ == '__main__':
    tasks = QueueClass()
    tasks.task_to_start('Урок 1')
    tasks.task_to_start('Урок 2')
    tasks.task_to_start('Урок 3')
    tasks.task_to_start('Урок 4')
    tasks.task_to_start('Урок 5')
    tasks.task_to_start('Урок 6')
    print('Начальные задачи', tasks.tasks_start())
    tasks.from_start_to_mod()
    tasks.from_start_to_mod()
    tasks.from_start_to_mod()
    print('Задачи добавленные на доработку', tasks.tasks_mod())
    tasks.from_mod_to_end()
    tasks.from_start_to_end()
    print('После всех операций итоговые списки')
    print('Начальные задачи', tasks.tasks_start())
    print('На доработке', tasks.tasks_mod())
    print('Завершенные', tasks.tasks_end())
