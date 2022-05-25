CURRENT_YEAR = 2021

class Person:
    def __init__(self, name, year_born):
        self.name =  name
        self.year_born = year_born

    def getAge(self):
        return CURRENT_YEAR - self.year_born

    def __str__(self):
        return str(self.name) + " " + str(self.getAge())

class Student(Person):
    def __init__(self, name, year_born):
        Person.__init__(self, name, year_born )
        self.knowledge = 0

    def Study(self):
        self.knowledge += 1

    def __str__(self):
        return str(self.name) + " " + str(self.getAge()) + " -> " + str(self.knowledge)

class Teacher(Person):
    def __init__(self, name, year_born):
        Person.__init__(self, name, year_born)
        self.knowledge = 10

    def GiveClass(self):
        self.knowledge += 2




#Person
print(" __Person__")
alice = Person("Alice Smith", 1997)
print(alice)
print("")

# Student -> SOBRE CARGA DEL METODO INIT
print(" __Student__")
bruno = Student("bruno Smith", 2000)
bruno.Study()
print(bruno)
print("")

# Teacher
print(" __Teacher__")
siomara = Teacher("siomara roberts", 1985)
siomara.GiveClass()
print(siomara)
print("")

#
