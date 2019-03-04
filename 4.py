# Создать набор классов. Животные
class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Dog(Animal):
    def __init__(self, name, legs, tale, size):
        super().__init__(name)
        self.legs = legs;
        self.tale = tale;
        self.size = size

    def get_stick(self):
        print('собака принеси палку')
        print('===========  ну это типа палка')


dog1 = Dog("собака", 4, 1, "big")
print(dog1.get_name())
print('----------')
print(dog1.get_stick())


class Cat(Animal):
    def __init__(self, name, legs, tale, size):
        super().__init__(name)
        self.legs = legs;
        self.tale = tale;
        self.size = size

    def go_sleep(self):
        print('кисик иди спать')
        print('zzzzzzzzzzz  ну типа кисик спит')


cat1 = Cat('кисик', 4, 1, "small")
print(cat1.get_name())
print('---------')
print(cat1.go_sleep())


class Parrot(Animal):
    def __init__(self, name, legs, tale, size):
        super().__init__(name)
        self.legs = legs;
        self.tale = tale;
        self.size = size

    def talk(self):
        print('попка дурак')


parrot1 = Parrot("попугай", 2, 1, 'small')
print(parrot1.get_name())
print('----------')
print(parrot1.talk())
