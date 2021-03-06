"""
Задание 5. На закрепление навыков работы со стеком
Реализуйте собственный класс-структуру "стопка тарелок".
Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.
Структура должна предусматривать наличие нескольких стопок.
Создание новой стопки происходит при достижении предыдущим
стеком порогового значения.
После реализации структуры, проверьте ее работу на различных сценариях.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стопки можно реализовать добавлением нового пустого массива
в массив стопок (lst = [[1,2,3,4,5], [], [], [],....]).
"""


class StackClass:
    def __init__(self):
        self.elems = [[]]
        self.idx = 0

    def add_stack(self):
        self.elems.append(list())
        self.idx += 1

    def push_in(self, el):
        if len(self.elems[self.idx]) == 5:
            print('Текущая стопка заполнена, добавьте новую командой add_stack')
        else:
            self.elems[self.idx].append(el)

    def stack_size(self):
        print(self.elems)
        return len(self.elems)

    def del_plate(self):
        if len(self.elems[self.idx]) == 0:
            self.elems.pop()
            self.idx -= 1
            self.elems[self.idx].pop()
        else:
            self.elems[self.idx].pop()


if __name__ == '__main__':

    SC_OBJ = StackClass()
    SC_OBJ.push_in(1)
    SC_OBJ.push_in(2)
    SC_OBJ.push_in(3)
    SC_OBJ.push_in(4)
    SC_OBJ.push_in(5)
    SC_OBJ.add_stack()
    SC_OBJ.push_in(6)
    SC_OBJ.push_in(7)
    SC_OBJ.push_in(8)
    SC_OBJ.push_in(9)
    SC_OBJ.stack_size()
    SC_OBJ.del_plate()
    SC_OBJ.stack_size()
    SC_OBJ.del_plate()
    SC_OBJ.stack_size()
    SC_OBJ.del_plate()
    SC_OBJ.stack_size()
    SC_OBJ.del_plate()
    SC_OBJ.stack_size()
    SC_OBJ.del_plate()
    SC_OBJ.stack_size()

"""Насколько я понял необходимо реализовать долько добавление."""
