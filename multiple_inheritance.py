# 多重继承

class Runnable(object):
    def run(self):
        print("Running~")


class Flyable(object):
    def fly(self):
        print("Flying~")


class Animal(object):
    pass


# 大类
class Mammal(Animal, Runnable):  # 哺乳动物
    pass


class Bird(Animal, Flyable):  # 鸟类
    pass


# 小类
class Dog(Mammal):
    pass


class Cat(Mammal):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass

d = Dog()
d.run()

# 个人理解：MixIn就是将多重继承的思考方式简化了，不再需要考虑复杂的层次关系。只需要考虑单一继承链，然后再额外的功能类可以不考虑。
# 例如：男人类，单一继承链上他属于人类，如果还要为这个男人类添加其它功能，比如抽烟类，那就用MixIn的写法加进来，但是无需你考虑抽烟类和人类有什么关系。
