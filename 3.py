# Создать набор классов. Фигуры

class ClassA:
    'Класс окружность'

    def setName(self, n):
        self.name = n

    def gatName(self):
        try:
            return self.name
        except:
            print('No Name')

    pass


class ClassB(object):
    'Класс треугольник'
    pass


class ClassC(object):
    'Класс квадрат'
    pass


class ClassD(object):
    'Класс трапеция'
    pass


list = (ClassA(), ClassB(), ClassC(), ClassD())
for i in list:
    print(i.__doc__)
# print('-----')
# print(list[0].__doc__)
