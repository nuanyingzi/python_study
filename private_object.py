# 类的私有属性

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_grade(self):
        return self.__score

    def set_grade(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('error score')


bart = Student("Lisy", 100)
print(bart.get_grade())
bart.set_grade(10)
print(bart.get_grade())


# print(bart._Student__name)

# 练习
# 请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：

class Student1(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, string):
        if string in ('male', 'female'):
            self.__gender = string
        else:
            raise ValueError("Error value")
