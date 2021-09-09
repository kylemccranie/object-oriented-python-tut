
class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()
        
##class method, acts only on the class itself, does not access attributes of
##instances  but acts on class variables
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("tim")
p2 = Person("Jill")
print(Person.number_of_people_())
