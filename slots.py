# 使用__slots__

class Student(object):
    pass


s = Student()
s.name = 'Tom'
print(s.name)


def set_age(self, age):
    self.age = age


from types import MethodType

s.set_age = MethodType(set_age, s)
s.set_age(11)
print(s.age)


def set_score(self, score):
    self.score = score


Student.set_score = set_score

s.set_score(99)
print(s.score)


class Teacher(object):
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


t = Teacher("Tom", 19)
print(t.name)
t.score = 99
print(t.score)
print(t.age)
