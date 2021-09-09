
class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f'I am {self.name} and i am {self.age} years old')


class Cat(Pet):
    def __init__(self,name,age,color):
        super().__init__(name,age)#calling parents class using super
        self.color = color
        
    def speak(self):
        print("meow")

    def show(self):
        print(f'I am {self.name} and i am {self.age} years old and I am {self.color}')

class Dog(Pet):
    def speak(self):
        print("bark")


p = Pet("Tim", 19)
p.show()
c = Cat("Bill", 34, "brown")
c.show()
d = Dog("Jill", 25)
d.speak()
