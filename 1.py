class Stud:
    def setName(self, n):
        self.name = n

    def getName(self):
        try:
            return self.name
        except:
            print('No name')

    def func(self):
        print('Hello i\'m a student')

    def setYear(self, y):
        self.year = y

    def getYear(self):
        try:
            return self.year
        except:
            print('No year')


first = Stud()
first.setName('Anton')
first.setYear(1990)

second = Stud()
second.setName('Katya')
second.setYear(1992)

third = Stud()

print(first.getName())
print(second.getYear())
print(third.getName())
