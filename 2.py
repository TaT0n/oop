from math import sqrt


class Circle:  # создание класса
    def cross(self, c):  # метод,определяющий, пересекаются окружности или нет
        x1 = self.x;
        y1 = self.y;
        r1 = self.r
        x2 = c.x;
        y2 = c.y;
        r2 = c.r
        cen_dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        print('Расстояние между центрами ', cen_dist)
        print('--------')
        if cen_dist == 0:
            if r1 == r2:
                print('Окружности совпадают')
            else:
                print("Центры совпадают, радиусы разные")
        elif cen_dist == r1 + r2 or cen_dist == abs(r1 - r2):
            print('Окружности соприкасаются')
        elif cen_dist > r1 + r2:
            print('Окружности не пересекаются')
        else:
            print('Окружности пересекаются')
        print('Конец!')

    def __init__(self, n, x, y, r):  # автоматический метод после создания класса
        self.name = n;
        self.x = x;
        self.y = y;
        self.r = r
        print(self.name, 'центр в точке x=', self.x, 'y=', self.y)
        print('радиус ', self.r)


circ1 = Circle('Первая окружность', -10, 0,
               2)  # создание экземпляра класса (название,координата X, координата Y, радиус)
circ2 = Circle('Вторая окружность', 3, 0, 3)
circ1.cross(circ2)  # вызов метода первого экземпляра  с атрибутом второго экземпляра

