# 继承

class Animal(object):
    def run(self):
        print('Animal is running~')


class Dog(Animal):
    def run(self):
        print('Dog is running~')


class Cat(Animal):
    pass


dog = Dog()
dog.run()


def return_twice(animal):
    animal.run()
    animal.run()


return_twice(Animal())
return_twice(Dog())
