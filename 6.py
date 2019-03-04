class Mercury:
    g = 3.7
    day = 58.6
    tMax = 427
    tMin = -193

    def f(self):
        print(self.__class__.__name__)
        print('УСП', self.g, '\nсутки за', self.day, \
              'дней', '\nтемпература от', self.tMin, 'до', \
              self.tMax, )


class Venus:
    g = 8.87
    day = 243
    tAvg = 462

    def f(self):
        print(self.__class__.__name__)
        print('УСП', self.g, '\nсутки за', self.day, \
              'дней', '\nсредняя температура', self.tAvg)


class Earth:
    g = 9.8
    day = 1
    tMax = 56.7
    tMin = -89.2

    def f(self):
        print(self.__class__.__name__)
        print('УСП', self.g, '\nсутки за', self.day, \
              'дней', '\nтемпература от', self.tMin, 'до', \
              self.tMax, )


class Mars:
    g = 3.7
    day = 1
    tMax = 35
    tMin = -153

    def f(self):
        print(self.__class__.__name__)
        print('УСП', self.g, '\nсутки за', self.day, \
              'дней', '\nтемпература от', self.tMin, 'до', \
              self.tMax, )


class Jupiter:
    g = 24.8
    day = 0.41
    tMax = 35700
    tMin = -145

    def f(self):
        print(self.__class__.__name__)
        print('УСП', self.g, '\nсутки за', self.day, \
              'дней', '\nтемпература от', self.tMin, 'до', \
              self.tMax, )


M = Mercury();
M.f()
print('--------')
V = Venus();
V.f()
print('--------')
E = Earth();
E.f()
print('--------')
Ma = Mars();
Ma.f()
print('--------')
J = Jupiter();
J.f()
